# -*- coding: utf-8 -*-
import scrapy


class ImdbV1Spider(scrapy.Spider):
    name = 'imdb_v1'
    allowed_domains = ['www.imdb.com/search/name?gender=male,female']
    start_urls = ['http://www.imdb.com/search/name?gender=male,female/']
    

    #global containers
    celeb_name = ""
    movie_list = []    
    celeb_colab_list = []


    #actor list page
    def parse(self, response):
        #parses all the names on the top list
        #response.xpath('//*[@class="lister-item-header"]/a/text()').extract()
        


        i = 0
        #capture all of the celebrities boxes
        #============================================
        celeb_boxes = response.xpath('//*[@class="lister-item mode-detail"]')
        for celeb in celeb_boxes:
            i++
            #scrape name
            celeb_name = celeb.xpath('.//*[@class="lister-item-header"]/a/text()').extract_first()  
            #scrape for celeb_page
            celeb_page_url = celeb.xpath('.//*[@class="lister-item-image"]/a/@href').extract_first()
            #fix the celeb_page_url by appending things
            celeb_page_url_final = response.urljoin(celeb_page_url)
            #jump to celeb page
            yield scrapy.Request(celeb_page_url_final, callback = self.parse_level2)		

            #timer to break out for testing purposes
            if i == 10:
                break


    #actor page
    #==================
    def parse_level2(self, response):

        #captures all the odd movies listings
        movies_odd = response.xpath('//*[@class="filmo-row odd"]')
        #captures all the even movies listings
        movies_even = response.xpath('//*[@class="filmo-row even"]')


        #iterate to each movies
        for movie in movies_odd:
            movie_titles = movie.xpath('.//a/text()').extract_first()
            movie_list.append(movie_titles)
            movie_page_url = movie.xpath('.//a/@href').extract_first()
            final_movie_page = response.urljoin(movie_page_url)
            
            #request to the movie page
            yield scrapy.Request(celeb_page_url_final, callback = self.parse_level2)





    def parse_level2(self, response)









