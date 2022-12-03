

import os
import sys
from bs4 import BeautifulSoup
import requests
import csv
from .CrawlerNameStory import CrawlerNameStory


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
        for x in elements:
            objItem = {}
            if index <= 5:
                index = index + 1
                if (x.attrs['value'] != 'all'):
                    objItem['name'] = x.text
                    objItem['id'] = x.attrs['value']
                    array.append(objItem)
                    print('Get name Category')
                    print(objItem['name'])
                    CrawlerNameStory.getName(objItem)
        CralwerCategory.inserData(array)

    def inserData(data):
        fieldnames = ['id', 'name']
        with open('category.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
