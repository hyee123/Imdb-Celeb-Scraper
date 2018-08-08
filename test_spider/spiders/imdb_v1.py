# -*- coding: utf-8 -*-
import scrapy


class ImdbV1Spider(scrapy.Spider):
    name = 'imdb_v1'
    allowed_domains = ['www.imdb.com/search/name?gender=male,female']
    start_urls = ['http://www.imdb.com/search/name?gender=male,female/']
	

	#actor list page
    def parse(self, response):
		#parses all the names on the top list
		#response.xpath('//*[@class="lister-item-header"]/a/text()').extract()
		

		#capture all of the celebrities boxes
		#============================================
		celeb_boxes = response.xpath('//*[@class="lister-item mode-detail"]')
		for celeb in celeb_boxes:
			#scrape name
			celeb_name = celeb.xpath('.//*[@class="lister-item-header"]/a/text()').extract_first()  
			#scrape for celeb_page
			celeb_page_url = celeb.xpath('.//*[@class="lister-item-image"]/a/@href').extract_first()

			#fix the celeb_page_url by appending things
			celeb_page_url_final = response.urljoin(celeb_page_url)

			#jump to celeb page
			yield scrapy.Request(celeb_page_url_final)		


	#actor page
	def parse_level2(self, response):
				










