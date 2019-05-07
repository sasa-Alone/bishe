# -*- coding: utf-8 -*-
import scrapy
import random

import bs4
import requests

from house.items import HouseItem

class DankeSpider(scrapy.Spider):
    name = 'danke'
    
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
        url ='https://www.dankegongyu.com/room/hz'
        yield scrapy.Request(url=url, headers=self.headers, callback=self.parse,)

    def parse(self, response):
        for i in range(1, 400):
            url = response.url + '?page={}'.format(str(i))
            print(url)
            # try:
            contents = requests.get(url, headers=self.headers)
            contents.encoding = 'utf-8'
            html = contents.text
            content = bs4.BeautifulSoup(html, "lxml")
            houselist = content.findAll('div', {'class': 'r_lbx'})
            for house in houselist:
                #    try:
                item = HouseItem()
                temp = house.find('div',{'class':'r_lbx_cena'}) # 获取标题div
                item['platform'] = "蛋壳公寓"
                item['title'] = temp.find('a')['title'] # 获取标题
                item['area'] = item['title'].split(" ")[1] # 获取区域
                item['link'] = temp.find('a')['href'] # 获取详情链接
                item['address'] = temp.find('div',{'class':'r_lbx_cena'}).text.strip()
                details = house.find('div',{'class':'r_lbx_cenb'}).text.split('|')
                item['size']=details[0].strip()
                item['floor']=details[1].strip()
                item['model']=details[2].strip()
                item['type']=details[3].strip()[-1]+"租"
                item['orientations']=details[3].strip().splitlines()[0].strip()
                if house.find('div',{'class':'room_price'}):
                    item['firstMonthPrice']=house.find('span',{'class':'ty_b'}).text.strip()
                    item['price']=house.find('div',{'class':'room_price'}).find('em').text.strip()
                else:
                    item['price']=house.find('span',{'class':'ty_b'}).text.strip()
                    item['firstMonthPrice']=item['price']
                yield item