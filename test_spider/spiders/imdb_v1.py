# -*- coding: utf-8 -*-
import scrapy


class ImdbV1Spider(scrapy.Spider):
    name = 'imdb_v1'
    allowed_domains = ['www.imdb.com/search/name?gender=male,female']
    start_urls = ['http://www.imdb.com/search/name?gender=male,female/']

    def parse(self, response):
        pass
