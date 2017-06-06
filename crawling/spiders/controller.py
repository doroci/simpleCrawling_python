# -*- coding: utf-8 -*-
import scrapy
import time

from crawling.items import CrawlingItem
from datetime import datetime

class SportsNews(scrapy.Spider):

    name = "sportsNewsCrawl"

    def start_requests(self):

        page = 2
        sysdate = datetime.today().strftime("%Y%m%d")
        date = [sysdate]

        for day in date:
            for j in range(1, page, 1):
                yield scrapy.Request("http://media.daum.net/breakingnews/sports?page={0}&regDate={1}".format(page, day),
                                     self.parse_url)

    def parse_url(self, response):
        for path in response.xpath('//*[@id="mArticle"]/div[2]/ul/li/div'):
            yield scrapy.Request(path.xpath('strong[@class="tit_thumb"]/a/@href').extract()[0], self.parse_urlInfo)

    def parse_urlInfo(self, response):
        item = CrawlingItem()
        item['source'] = response.xpath('//*[@id="cSub"]/div[1]/em/a/img/@alt').extract()[0]
        item['title'] = response.xpath('//*[@id="cSub"]/div[1]/h3/text()').extract()[0]
        item['date'] = response.xpath('/html/head/meta[contains(@property, "og:regDate")]/@content').extract()[0][:8]
        item['contents'] = response.xpath('//*[@id="harmonyContainer"]/section/div[contains(@dmcf-ptype, "general")]/text()').extract()+\
                          response.xpath('//*[@id="harmonyContainer"]/section/p[contains(@dmcf-ptype, "general")]/text()').extract()

        # 5초마다 크롤링을 시도
        time.sleep(5)

        yield item