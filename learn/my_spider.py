#!/bin/usr/env python

import scrapy
class MySpider(scrapy.Spider):
    name = 'myspider'
    def __init__(self, category = None, *args, **kwargs):
        self.start_urls = ['http://www.example.com/categories/%s' % category]
    
    def parse(self, response):
        pass
