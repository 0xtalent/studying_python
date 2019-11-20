# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test2'
    allowed_domains = ['blog.scrapinghub.com']
    start_urls = ['https://blog.scrapinghub.com/']

    def parse(self, response):
        """
        :param : response
        :return : Title Text
        """

        # 2가지 방법이 있어요(CSS Selector, XPath)
        # getall() <-> get(), extract <-> extract_first()

        # 예제1(CSS Selector로 해보기)
        for text in response.css('div.post-header h2 a::text').getall():
            # return Type : Request, BaseItem, Dictionary, None
            yield {
                'title': text
            }
