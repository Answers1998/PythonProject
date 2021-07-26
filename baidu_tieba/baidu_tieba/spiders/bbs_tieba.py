import scrapy


class BbsTiebaSpider(scrapy.Spider):
    name = 'bbs_tieba'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
