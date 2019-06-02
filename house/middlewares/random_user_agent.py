# -*- coding: utf-8 -*-
import random
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
import logging


class RandomUserAgentMiddleware(object):
    # the default user_agent_list composes chrome,I E,firefox,Mozilla,opera,netscape
    # for more user agent strings,you can find it in http://www.useragentstring.com/pages/useragentstring.php
    user_agent_list = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
        "User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.6 Safari/537.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_0) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.22 (KHTML, like Gecko) Chrome/19.0.1047.0 Safari/535.22",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.45 Safari/535.19",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.45 Safari/535.19",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_8) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_4) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_6) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.112 Safari/534.30",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_4) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.112 Safari/534.30",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.100 Safari/534.30",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_4) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.100 Safari/534.30"
    ]

    def __init__(self, user_agent=''):
        self.logger = logging.getLogger("spider.middlewares.random_user_agent")
        self.user_agent = user_agent

    def process_request(self, request, spider):
        ua = random.choice(self.user_agent_list)
        if request.headers.get('USER_AGENT') is not None:
            return
        request.headers.setdefault('USER_AGENT', ua)
        self.logger.info("process request %s using random ua: %s" % (request, ua))


# import requests
# import threading
# from lxml import etree
# from bs4 import BeautifulSoup
# from queue import Queue
# out_queue=Queue()
# def get_html(url1):
#     #url='https://www.doutula.com/article/list/?page=1'
#     header={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36 Core/1.47.516.400 QQBrowser/9.4.8186.400'}
#     request=requests.get(url=url1,headers=header)
#     response=request.content
#     return response
# class threadDownload(threading.Thread):
#     def __init__(self,que,no):
#         threading.Thread.__init__(self)
#         self.que = que
#         self.no = no
#     def run(self):
#         while True:
#             if not self.que.empty():
#                    save(self.que.get()[0])
#             else:
#                 break
# def get_html(html1):
#     y=[]
#     soup=BeautifulSoup(html1,'lxml')
#     for hrefs in soup.find_all('a',class_='list-group-item random_list'):
#         y.append(hrefs.get('href'))
#     return y
#
# def get(html2):
#     html=get_html(html2)
#     soup=etree.HTML(html)
#     items=soup.xpath('//div[@class="artile_des"]')
#     for item in items:
#         imgurl_list=item.xpath('table/tbody/tr/td/a/img/@onerror')
#         out_queue.put(item.xpath('table/tbody/tr/td/a/img/@onerror'))
#     for a in range(0,imgurl_list.__len__()):
#         threadD = threadDownload(out_queue,a)
#         threadD.start()
# x=1
# def save(url):
#     global x
#     x+=1
#     url1 =url.split('=')[-1][1:-2]
#     # print u'正在下载'+'http:'+img_url1
#     img_content=requests.get('http:'+url1).content
#     with open('doutu/%s.jpg'% x,'wb') as f:
#         f.write(img_content)
#
#
#
# def main():
#     start_url='https://www.dankegongyu.com/room/hz?page='
#     for j in range(1,5):
#         start_html=get_html(start_url+str(j))
#         b=get_html(start_html)
#         for i in b:
#             get(i)
# if __name__=='__main__':
#     main()