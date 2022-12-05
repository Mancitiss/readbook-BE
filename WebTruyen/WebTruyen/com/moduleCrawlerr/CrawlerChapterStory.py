import requests
import csv
from bs4 import BeautifulSoup
import time
from backend.models import Chapter, Comment, Story


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
                    index = index + 1
                    objectItem = {}
                    objectItem['story'] = row['story_name']
                    objectItem['chapter_name'] = x.select_one(
                        'a').attrs['title']
                    objectItem['linkstory'] = x.select_one('a').attrs['href']
                    x = requests.get(objectItem['linkstory'])
                    soup = BeautifulSoup(x.text, "html.parser")
                    element = soup.select_one('#chapter-c')
                    objectItem['content'] = element.text
                    # print(objectItem)
                    arrayList.append(objectItem)
                    CrawlerChapterStory.inserData(
                        row['category_name'], objectItem)
                    print(objectItem)
                    # CrawlerChapterStory.getName(objectItem)

        except:
            print("An exception occurred")

    def inserData(name, data):
        print(data)
        try:
            print('run')
            oldKey = Chapter.objects.get(chapter_name=data['chapter_name'])
            print('key')
        except:
            topic1 = Chapter()
            item = Story.objects.filter(story_name="Bí Ẩn Đôi Long Phượng")

            Chapter.objects.bulk_create([
                Story(story_name="Bí Ẩn Đôi Long Phượng"),
                Chapter(chapter_name='chapter name'),
                Chapter(content='content'), ]
            )

            # topic1.story_id = 1
            topic1.story_name_id = 1

            # topic1.story.add(item)
            topic1.save()
