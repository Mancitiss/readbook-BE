import requests
import csv
from bs4 import BeautifulSoup
import time


class CrawlerChapterStory():
    fieldNameStory = ['story', 'chapter_name', 'content', 'linkstory']

    def init():
        with open('chapter.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(
                f, fieldnames=CrawlerChapterStory.fieldNameStory)
            writer.writeheader()
        CrawlerChapterStory.getNameStoryUserCategory()

    def getNameStoryUserCategory():

        with open('storyname.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for (row) in csv_reader:
                CrawlerChapterStory.getName(row)
                time.sleep(1)

    def getName(row):
        index = 0
        url = row['linkstory']
        try:
            x = requests.get(url)

            soup = BeautifulSoup(x.text, "html.parser")
            elements = soup.select('#list-chapter .row .list-chapter li')
            arrayList = []
            for x in elements:
                if (index <= 5):
                    index = index +1
                    objectItem = {}
                    objectItem['story'] = row['story_name']
                    objectItem['chapter_name'] = x.select_one('a').attrs['title']
                    objectItem['linkstory'] = x.select_one('a').attrs['href']
                    x = requests.get(objectItem['linkstory'])
                    soup = BeautifulSoup(x.text, "html.parser")
                    element = soup.select_one('#chapter-c')
                    objectItem['content'] = element.text
                    # print(objectItem)
                    arrayList.append(objectItem)
                    CrawlerChapterStory.getName(objectItem)
            CrawlerChapterStory.inserData(arrayList)
                   
        except:
            print("An exception occurred")

    def inserData(data):
        with open('chapter.csv', 'a', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(
                f, fieldnames=CrawlerChapterStory.fieldNameStory)
            for row in data:
                writer.writerow(row)
