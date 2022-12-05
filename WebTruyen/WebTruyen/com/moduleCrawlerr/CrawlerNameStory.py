import requests
import csv
from bs4 import BeautifulSoup
import time
from .CrawlerChapterStory import CrawlerChapterStory
from backend.models import Story, Category
from django.utils import timezone


class CrawlerNameStory():
    fieldNameStory = ['category_name', 'story_name', 'linkstory', 'image', 'create_date', 'author',
                      'total_chapters', 'user', 'showtimes', 'rating', 'views', 'introduce']

    def init():
        with open('storyname.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(
                f, fieldnames=CrawlerNameStory.fieldNameStory)
            writer.writeheader()
        CrawlerNameStory.getNameStoryUserCategory()

    def getNameStoryUserCategory():
        with open('category.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:

                CrawlerNameStory.getName(row)

                time.sleep(1)

    def getName(row):
        url = "https://truyenfull.vn/ajax.php?type=hot_select&id="+row['id']
        try:
            x = requests.get(url)
            soup = BeautifulSoup(x.text, "html.parser")
            elements = soup.select('.item')
            arrayList = []
            index = 0
            for x in elements:
                if index <= 10:
                    index = index + 1
                    print('Story name:', x.text)
                    objectItem = {}
                    objectItem['story_name'] = x.text
                    objectItem['category_name'] = row['id']
                    objectItem['linkstory'] = x.select_one('a').attrs['href']
                    objectItem['image'] = x.select_one('img').attrs['src']
                    arrayList.append(objectItem)
                    CrawlerNameStory.inserData(row['name'], objectItem)
                    CrawlerChapterStory.getName(objectItem)
                    time.sleep(1)

        except:
            print('Exception 1')

    def inserData(type, data):
        # print(type, data)

        try:
            existItem = Story.objects.get(story_name=data['story_name'])
            # print('errrrrrrrr')

        except:
            # print('error')
         
            topic1 = Story(story_name=data['story_name'],
                           user_id = 1,
                           author = "admin",
                           image = data['image'],
                           total_chapters = 50,
                           showtimes = '',
                           rating = 5,
                           views = 0,
                           introduce = '')
            topic1.save()
