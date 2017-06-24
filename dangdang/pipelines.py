# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
#from db.product import save_product


class DangdangPipeline(object):

	def open_spider(self, spider):
		self.file = open('product3.csv', 'a')

	def close_spider(self, spider):
		self.file.close()


	def process_item(self, item, spider):
		item['title'] = item['title'].replace(',','，')
		cont = "{},{},{},{},{},{},{}\n".format(item['title'], item['isbn'],item['price'],item['photo'],item['publisher'],item['link'],item['sell_price'])
		self.file.write(cont)

		
