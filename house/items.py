# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class HouseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 标签  小区  户型   面积   关注人数  观看人数  发布时间  价格   均价  详情链接  经纬度 地址
    platform = scrapy.Field()
    title = scrapy.Field()
    #community = scrapy.Field()
    type = scrapy.Field() # 出租类型
    model = scrapy.Field() # 户型
    area = scrapy.Field()  # 区域
    size = scrapy.Field() # 面积
    orientations = scrapy.Field() # 朝向
    floor = scrapy.Field() # 楼层
    renovation = scrapy.Field() # 装修
    #focus_num = scrapy.Field()
    #watch_num = scrapy.Field()
    #time = scrapy.Field()
    price = scrapy.Field()  # 价格
    firstMonthPrice = scrapy.Field()  # 首月价格
    average_price = scrapy.Field()  # 平均价格
    link = scrapy.Field()   # 详情链接
    Latitude = scrapy.Field()   # 经纬度
    address = scrapy.Field()    # 地址
    special = scrapy.Field()  # 特色
    pass