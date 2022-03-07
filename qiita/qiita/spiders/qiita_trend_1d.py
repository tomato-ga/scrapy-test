from unicodedata import category
import scrapy


class QiitaTrend1dSpider(scrapy.Spider):
    name = 'qiita_trend_1d'
    allowed_domains = ['qiita.com']
    start_urls = ['http://qiita.com/']

    def parse(self, response):
        # 取得したい要素をparse関数のあとにかく
        category = response.xpath('//a[@class="st-NewHeader_mainNavigationItem is-active"]/text()').get()
        titles = response.xpath('//h2/a/text()').getall()
        urls = response.xpath('//h2/a/@href').getall()

        yield {
            'category': category,
            'titles': titles,
            'urls': urls
        }