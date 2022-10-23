

import os
import sys
from bs4 import BeautifulSoup
import requests
import csv

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
        for x in elements:
            objItem = {}
            if (x.attrs['value'] != 'all'):
                objItem['name'] = x.text
                objItem['id'] = x.attrs['value']
                array.append(objItem)
        CralwerCategory.inserData(array)


    def inserData(data):
        fieldnames = ['id','name']
        with open('category.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
