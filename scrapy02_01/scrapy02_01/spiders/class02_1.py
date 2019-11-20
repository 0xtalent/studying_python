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

        # 출력 옵션
        # scrapy crawl test2 -o result.jl -t jsonlines
        # -o: 파일명,확장, -t: 파일 타입(json, jsonlines, jl, csv, sml, marshal, pickle)
        for text in response.css('div.post-header h2 a::text').getall():
            # return Type : Request, BaseItem, Dictionary, None
            yield {
                'title': text
            }

        # 예제2(XPath)
        # for i, text in enumerate(response.xpath('//div[@class="post-header"]/h2/a/text()').getall()):
        #     yield {
        #         'number': i,
        #         'title': text
        #     }
