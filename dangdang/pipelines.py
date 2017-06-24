# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
#from db.product import save_product

f = open("product.csv",'a')
print(f)

class DangdangPipeline(object):


	def process_item(self, item, spider):
		item['title'] = item['title'].replace(',','，')
		cont = "{},{},{},{},{},{},{}\n".format(item['title'], item['isbn'],item['price'],item['photo'],item['publisher'],item['link'],item['sell_price'])
		f.write(cont)
		
