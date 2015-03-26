#!/bin/usr/env python

import scrapy

class MyItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    last_updated = scrapy.Field(serializer = str)

if __name__ == '__main__':
    item1 = MyItem(name = 'wjj', price = '1.0')
    item2 = MyItem(name = 'hll', price = '2.0')
    print item1
    print item2
    print item2.fields
