# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ZhisousouPipeline(object):
    def process_item(self, item, spider):
        if spider.name != 'xuanjianghui':
            print(item)
            item.save_to_es()
            return item
        else:
            print(item)
            item.save_to_es()
            return item


