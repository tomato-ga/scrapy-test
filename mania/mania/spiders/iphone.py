"""一応取得はできてるけど、1件ごとのリストにはなっていない"""

import scrapy

class IphoneSpider(scrapy.Spider):
    name = 'iphone'
    allowed_domains = ['iphone-mania.jp']
    start_urls = ['https://iphone-mania.jp/']

    def parse(self, response):
        tops = response.xpath("//div")

        for top in tops:

            yield {
                'title': top.xpath("./div[@class='main_new_content']/ul/li[@id='get_url']/a/h2/text()").get(),
                'url': top.xpath("./ul/li[@id='get_url']/a/@href").get()
            }

            # h2s = top.xpath(".//ul/li[@id='get_url']/a/h2/text()").get()
            # urls = top.xpath(".//ul/li[@id='get_url']/a/@href").get()