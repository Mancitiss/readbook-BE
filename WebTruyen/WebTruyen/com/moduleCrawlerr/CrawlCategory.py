

import os
import sys
from bs4 import BeautifulSoup
import requests
import csv
from .CrawlerNameStory import CrawlerNameStory
from backend.models import Category, Chapter, Comment


class CralwerCategory():
    listArray = []

    def init():
        CralwerCategory.crawlerType()

    def crawlerType():
        print('crawler init')
        x = requests.get('https://truyenfull.vn/')
        soup = BeautifulSoup(x.text, "html.parser")
        elements = soup.select('#hot-select option')
        array = []
        index = 0
        for item in elements:
            objItem = {}
            if index <= 5:
                index = index + 1
                if (item.attrs['value'] != 'all'):
                    objItem['name'] = item.text
                    objItem['id'] = item.attrs['value']
                    array.append(objItem)
                    print('---- Get name Category', objItem['name'],'----')
                    CralwerCategory.inserData(objItem)
                    CrawlerNameStory.getName(objItem)

    def inserData(row):
        try:
            oldKey = Category.objects.get(category_name=row['name'])
        except:
            if (row['name']):
                try:
                    topic = Category()
                    Category.objects.create(category_name=row['name'])
                    topic.save()
                except:
                    print('')
