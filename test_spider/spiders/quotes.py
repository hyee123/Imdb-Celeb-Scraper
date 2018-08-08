# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']
    def parse(self, response):
        quote = response.xpath('//*[@class="quote"]')
        next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        text = quote.xpath('.//*[@class="text"]/text()').extract_first()
        author = quote.xpath('.//*[@class="author"]/text()').extract_first()
        tags = quote.xpath('.//*[@itemprop="keywords"]/@content').extract_first()
        next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        print(text)
        print(author)
        yield scrapy.Request(absolute_next_page_url, callback = self.parse2)



    def parse2(self, response):
        quote = response.xpath('//*[@class="quote"]')
        next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        text = quote.xpath('.//*[@class="text"]/text()').extract_first()
        author = quote.xpath('.//*[@class="author"]/text()').extract_first()
        tags = quote.xpath('.//*[@itemprop="keywords"]/@content').extract_first()
        next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        print(text)
        print(author)
