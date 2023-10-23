import time
from jwt import decode
import requests
from functools import lru_cache
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.x509 import load_pem_x509_certificate

@lru_cache(maxsize=1)
def get_google_public_keys():
    """Gets the Google public keys."""

    response = requests.get('https://www.googleapis.com/oauth2/v1/certs')
    # Check the status code.
    if response.status_code != 200:
        return None

    # response is json containing multiple keys, transform them into a list
    keys = []
    for key in response.json().values():
        cert_obj = load_pem_x509_certificate(key.encode())
        public_key = cert_obj.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode('utf-8')
        keys.append(public_key)
        #keys.append(serialization.load_pem_public_key(
        #    key.encode(), backend=default_backend()))
    return keys


def verify_google_credential_jwt(jwt_token):
    """Verifies a Google credential JWT using PyJWT.

    Args:
        jwt_token (str): The JWT token to verify.

    Returns:
        dict: The claims in the JWT token.
    """

    try:
        # Try to decode the JWT using the cached public keys.
        keys = get_google_public_keys()
        claims = None
        for key in keys:
            try:
                claims = decode(jwt_token, key, algorithms=['RS256'] , audience='786308916007-cm24heo3ecdro7amptnhe81shi0aoet2.apps.googleusercontent.com', issuer='https://accounts.google.com')
                break
            except Exception as e:
                print(e)
                continue
        if claims is None:
            raise Exception('no keys work')
    except Exception as e:
        print(e)
        # If the decode fails, refresh the public keys and try again.
        # save the current cache in case the refresh fails.
        old_cache = get_google_public_keys.cache_info()
        get_google_public_keys.cache_clear()
        new_key = get_google_public_keys()
        # check if new key is none
        if new_key is None:
            # if new key is none, restore the old cache
            get_google_public_keys.cache_clear()
            get_google_public_keys.cache_info(old_cache)
            return None
        try:
            claims = decode(jwt_token, get_google_public_keys())
        except:
            # if decode fails again, return none
            return None
    return claims


# Example usage:

# jwt_token = '...'

# claims = verify_google_credential_jwt(jwt_token)

# The user is now authenticated.