import json
import re
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
import secrets
import string
import datetime

import pytz
from backend.models import User
from backend.utils import verify_google_credential_jwt
from oauth2_provider.models import get_access_token_model, get_application_model
from oauth2_provider.settings import oauth2_settings
from oauth2_provider.models import AccessToken

import os
import requests

class GoogleLoginMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if re.match('^/login/', request.path):
            print("login")
            # check if request is post
            if request.method == 'POST':
                print('post')
                # check if request is from google
                if request.POST.get('provider') == 'google':
                    # check if token is valid
                    result = verify_google_credential_jwt(request.POST.get('credential'))
                    print('google')
                    if result is None:
                        response = HttpResponse()
                        response.status_code = 401
                        return response
                    # user is valid, check if user is in database, if not create account, if yes, return user
                    # check if user is in database
                    try:
                        user = User.objects.get(email=result['email'])
                    except Exception as e:
                        print(e)
                        # create new user
                        user = User.objects.create_user(
                            username=result['email'],
                            email=result['email'],
                            # password = secure random string, use the random string of python
                            password=''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(8)),
                            first_name=result['given_name'],
                            last_name=result['family_name'],
                        )
                        user.save()
                    finally:
                        response = HttpResponse()
                        response.status_code = 200
                        response['Access-Control-Allow-Origin'] = request.META.get('HTTP_ORIGIN')
                        try:
                            dicts = {}
                            dicts['username'] = user.username
                            dicts['email'] = user.email
                            dicts['first_name'] = user.first_name
                            dicts['last_name'] = user.last_name
                            dicts['is_active'] = user.is_active
                            dicts['is_staff'] = user.is_staff
                            dicts['is_superuser'] = user.is_superuser
                            dicts['last_login'] = user.last_login
                            dicts['date_joined'] = user.date_joined.strftime("%Y-%m-%d %H:%M:%S")
                            token = self.create_access_token(user)
                            dicts['access_token'] = token
                            print(dicts)
                            response.content = json.dumps(dicts, skipkeys=True, allow_nan=True)
                        except Exception as e:
                            print(e)
                        print('im not alive')
                        return response
                elif request.POST.get('provider') == 'facebook':
                    print("facebook")
                    #get environment variable in user environment with the name "fb_secret"
                    params = { 
                        "client_id": os.getenv("fbapp_id", ""), 
                        "client_secret": os.getenv("fbapp_secret", ""),
                        "grant_type": "client_credentials",
                        }
                    response = requests.get("https://graph.facebook.com/oauth/access_token", params=params)
                    print(response.content)
                    json_object = json.loads(response.content)
                    server_access_token = json_object["access_token"]
                    user_access_token = request.POST.get('credential')
                    params = {
                        "input_token": user_access_token,
                        "access_token": server_access_token,
                        }
                    response = requests.get("https://graph.facebook.com/debug_token", params=params)
                    print(response.content)
                    json_object = json.loads(response.content)
                    if json_object["data"]["is_valid"] == False:
                        response = HttpResponse()
                        response.status_code = 401
                        return response
                    else:
                        params = {
                            "fields": "id,name,email,first_name,last_name",
                            "access_token": user_access_token,
                            }
                        response = requests.get("https://graph.facebook.com/me", params=params)
                        json_object = json.loads(response.content)
                        try:
                            user = User.objects.get(email=json_object['email'])
                        except Exception as e:
                            print(e)
                            # create new user
                            user = User.objects.create_user(
                                username=json_object['email'],
                                email=json_object['email'],
                                # password = secure random string, use the random string of python
                                password=''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(8)),
                                first_name=json_object['first_name'],
                                last_name=json_object['last_name'],
                            )
                            user.save()
                        finally:
                            response = HttpResponse()
                            response.status_code = 200
                            response['Access-Control-Allow-Origin'] = request.META.get('HTTP_ORIGIN')
                            try:
                                dicts = {}
                                dicts['username'] = user.username
                                dicts['email'] = user.email
                                dicts['first_name'] = user.first_name
                                dicts['last_name'] = user.last_name
                                dicts['is_active'] = user.is_active
                                dicts['is_staff'] = user.is_staff
                                dicts['is_superuser'] = user.is_superuser
                                dicts['last_login'] = user.last_login
                                dicts['date_joined'] = user.date_joined.strftime("%Y-%m-%d %H:%M:%S")
                                token = self.create_access_token(user)
                                dicts['access_token'] = token
                                print(dicts)
                                response.content = json.dumps(dicts, skipkeys=True, allow_nan=True)
                            except Exception as e:
                                print(e)
                            print('im not alive')
                            return response
    
    def create_access_token(self, user):
        # Custom token creation logic
        # You can customize the token creation process here
        try:
            token_model = get_access_token_model()
            token: AccessToken = token_model.objects.get_or_create(
                user=user,
                application=get_application_model().objects.first(),
                expires=datetime.datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')) + datetime.timedelta(seconds=3600)
            )[0]
            print("token")
            print(token)
            if token.token == None or token.token == '':
                    token.token = secrets.token_urlsafe(30) 
                    token.expires = datetime.datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')) + datetime.timedelta(seconds=3600)
                    token.save()
            return token.token
        except Exception as e:
            for i in e.args:
                print(i, end='')
                print("*")
                if i == 'UNIQUE constraint failed: oauth2_provider_accesstoken.token':
                    print('hit')
                    token_model.objects.filter(user=user).delete()
                    token: AccessToken = token_model.objects.get_or_create(
                        user=user, 
                        application=get_application_model().objects.first(), 
                        expires=datetime.datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')) + datetime.timedelta(seconds=3600)
                    )[0]
                    if token.token == None or token.token == '':
                        token.token = secrets.token_urlsafe(30) 
                    token.expires = datetime.datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')) + datetime.timedelta(seconds=3600)
                    token.save()
                    return token.token
