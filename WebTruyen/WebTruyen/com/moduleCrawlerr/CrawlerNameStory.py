import requests
import csv
from bs4 import BeautifulSoup
import time
from .CrawlerChapterStory import CrawlerChapterStory


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

                # time.sleep(1)

    def getName(row):
        url = "https://truyenfull.vn/ajax.php?type=hot_select&id="+row['id']
        try:
            x = requests.get(url)
            soup = BeautifulSoup(x.text, "html.parser")
            elements = soup.select('.item')
            arrayList = []
            index = 0
            for x in elements:
                if index <= 5:
                    index = index +1
                    print(x.text)
                    objectItem = {}
                    objectItem['story_name'] = x.text
                    objectItem['category_name'] = row['id']
                    objectItem['linkstory'] = x.select_one('a').attrs['href']
                    objectItem['image'] = x.select_one('img').attrs['src']
                    arrayList.append(objectItem)
                    CrawlerChapterStory.getName(objectItem)
            CrawlerNameStory.inserData(arrayList)

        except:
            print('Exception')

    def inserData(data):
        with open('storyname.csv', 'a', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(
                f, fieldnames=CrawlerNameStory.fieldNameStory)
            for row in data:
                writer.writerow(row)
