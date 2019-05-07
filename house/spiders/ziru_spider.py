# -*- coding: utf-8 -*-
import scrapy
import random

import bs4
import re
import requests

from house.items import HouseItem

class ZiruSpider(scrapy.Spider):
    name = 'ziru'
    
    user_agent = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36',
    'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)',
    ]

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'User-Agent': user_agent[random.randint(0, 5)]
    }
    def start_requests(self):
        url = 'http://hz.ziroom.com/z/nl/z3.html'
        yield scrapy.Request(url=url, headers=self.headers, callback=self.parse,)

    def parse(self, response):
        contents = requests.get(response.url, headers=self.headers)
        contents.encoding = 'utf-8'
        html = contents.text
        content = bs4.BeautifulSoup(html, "lxml")
        page = content.find('div', {'id': 'page'}).findAll('span')[1].text.strip()
        pagesRange = int(re.findall(r"\d+\.?\d*", page)[0])
        for i in range(1, pagesRange):
            url = response.url + '?p={}'.format(str(i))
            # try:
            contents = requests.get(url, headers=self.headers)
            contents.encoding = 'utf-8'
            html = contents.text
            content = bs4.BeautifulSoup(html, "lxml")
            houselist = content.find('ul', {'id': 'houseList'}).findAll('li')
            for house in houselist:
                #    try:
                item = HouseItem()
                txt = house.find('div', {'class': 'txt'})  # 获取标题div
                item['platform'] = "自如"
                item['title'] = txt.find('h3').text.strip()  # 获取标题
                item['link'] = txt.find('h3').find('a')['href']  # 获取详情链接
                item['special'] = []
                if txt.find('h3').find('span', {'class', 'shx_icon'}):
                    item['special'].append('shxicon')
                specials = txt.find('h4').findAll('span')
                for special in specials:
                    item['special'].append(special.text.strip())
                details = txt.find('div', {'class': 'detail'}).findAll('span')
                item['area'] = details[0].text.strip()
                item['floor'] = details[1].text.strip()
                item['model'] = details[2].text.strip()
                item['address'] = details[3].text.strip()
                tags = txt.find('p', {'class': 'room_tags clearfix'}).findAll('span')
                for tag in tags:
                    item['special'].append(tag.text.strip())
                priceDetail = house.find('div', {'class': 'priceDetail'})
                item['price'] = priceDetail.find('p', {'class': 'price'}).text.strip()
                yield item