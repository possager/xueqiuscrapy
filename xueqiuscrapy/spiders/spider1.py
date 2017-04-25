import scrapy
from bs4 import BeautifulSoup



class spider1(scrapy.Spider):
    name = 'xueqiu'
    start_urls=['https://www.xueqiu.com/']

    def parse(self, response):
        print response.body