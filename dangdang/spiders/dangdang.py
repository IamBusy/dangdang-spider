# -*- coding: utf-8 -*

import scrapy
from dangdang.items import Product

class DangSpider(scrapy.Spider):
    name = "dangdang"
    allowed_domains = ["dangdang.com"]
    start_urls = [
        "http://category.dangdang.com/pg1-cp01.49.01.00.00.00-f0%7C0%7C0%7C0%7C0%7C1%7C0%7C0%7C0%7C0%7C0%7C0%7C0%7C.html"
    ]

    categories = [
        "cp01.49.01.00.00.00",
        "cp01.49.05.00.00.00",
        "cp01.49.08.00.00.00",
        "cp01.49.30.00.00.00",
        "cp01.49.07.00.00.00",
        "cp01.49.06.00.00.00",
        "cp01.49.90.00.00.00",
    ]

    curCateIdx = 0


    def isValid(self,selector):
        category = selector.xpath('//div[@id="breadcrumb"]//b/text()').extract_first()
        if(category==u'图书'):
            return True
        return False

    
    def nextPage(self,num):
        num = int(num)+1
        return "http://product.dangdang.com/"+str(num)+".html"

    def nextPageByCategory(self,num):
        print(self.categories)
        num = int(num) + 1
        if num > 100:
            self.curCateIdx = self.curCateIdx+1
            num=1
        if self.curCateIdx >= len(self.categories):
            return ''
        return "http://category.dangdang.com/pg"+str(num)+ "-" + self.categories[self.curCateIdx] + "-f0%7C0%7C0%7C0%7C0%7C1%7C0%7C0%7C0%7C0%7C0%7C0%7C0%7C.html"


    def parse(self, response):
        number = response.url.split("/")[-1].split("-")[0][2:]

        filename = response.url.split(".")[0]
        lis = response.selector.xpath('//ul[@class="bigimg"]/li')
        items = []
        print(lis)
        for li in lis:
            # try:
            #     item = Product()
            #     item['link'] = li.xpath('./a/@href').extract()[0]
            #     item['photo'] = li.xpath('./a/img/@src').extract()[0]
            #     item['title'] = li.xpath('./p[@class="name"]/a/@title').extract()[0]
            #     item['sell_price'] = li.xpath('./p[@class="price"]/span[@class="search_now_price"]/text()').extract()[0][1:]
            #     item['price'] = li.xpath('./p[@class="price"]/span[@class="search_pre_price"]/text()').extract()[0][1:]

            #     equest = scrapy.Request(item['link'], callback = self.parseDetail)
            #     request.meta['item'] = item
            #     yield request
            # except:
            #     continue
            item = Product()
            item['link'] = li.xpath('./a/@href').extract()[0]
            item['photo'] = li.xpath('./a/img/@src').extract()[0]
            item['title'] = li.xpath('./p[@class="name"]/a/@title').extract()[0]
            item['sell_price'] = li.xpath('./p[@class="price"]/span[@class="search_now_price"]/text()').extract()[0][1:]
            item['price'] = li.xpath('./p[@class="price"]/span[@class="search_pre_price"]/text()').extract()[0][1:]

            request = scrapy.Request(item['link'], callback = self.parseDetail)
            request.meta['item'] = item
            yield request

        nextPg = self.nextPageByCategory(number)
        if nextPg != "" :
            yield scrapy.Request(nextPg, callback=self.parse)

    def parseDetail(self, response):
        item = response.meta['item']
        for tx in response.xpath('//div[@id="detail_describe"]/ul[@class="key clearfix"]/li/text()').extract():
            if tx.find('ISBN')>0 or tx.find('isbn')>0:
                item['isbn'] = tx.split("：")[1]
        item['publisher'] = response.xpath('//div[@class="messbox_info"]/span[@dd_name="出版社"]/a/text()').extract()[0]
        yield item
    

