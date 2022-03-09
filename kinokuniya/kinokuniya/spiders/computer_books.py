import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import logging

class ComputerBooksSpider(CrawlSpider):
    name = 'computer_books'
    allowed_domains = ['www.kinokuniya.co.jp']
    start_urls = ['https://www.kinokuniya.co.jp/f/dsd-101001037028005-06-']

    rules = (
        # 詳細ページへのリンク
        Rule(LinkExtractor(restrict_xpaths=('//h3[@class="heightLine-2"]/a')), callback='parse_item', follow=False),
        # 次のページへのリンク
        Rule(LinkExtractor(restrict_xpaths=('(//a[contains(text(),"次へ")])[1]')),),
    )

    def get_title(self, title):
        if title:
            return ' '.join(title).lstrip()
        return title

    def get_price(self, price):
        if price:
            return int(price.replace('¥', '').replace(',', ''))
        return 0

    def get_size(self, size):
        if size:
            return size.split('／')[0].replace('サイズ ', '').replace('判', '')
        return size

    def get_page(self, page):
        if page:
            return int(page.split('／')[1].replace('ページ数 ', '').replace('p', ''))
        return 0

    def get_code(self, code):
        if code:
            return int(code.replace('商品コード ', ''))
        return code

    def parse_item(self, response):
        logging.info(response.url)

        yield {
            'title': self.get_title(response.xpath('//h3[@itemprop="name"]/text()').getall()),
            'author': response.xpath('//div[@class="infobox ml10 mt10"]/ul/li[1]/a/text()').get(),
            'price': self.get_price(response.xpath('//span[@class="sale_price"]/text()').get()),
            'publisher': response.xpath('//a[contains(@href,"publisher-key")]/text()').get(),
            'size': self.get_size(response.xpath('normalize-space(//div[@class="infbox dotted ml10 mt05 pt05"]/ul/li/text())').get()),
            'page': self.get_page(response.xpath('normalize-space(//div[@class="infbox dotted ml10 mt05 pt05"]/ul/li/text())').get()),
            'code': self.get_code(response.xpath('//div[@class="infbox dotted ml10 mt05 pt05"]/ul/li[@itemprop="identifier"]/text()').get()),
            'summary': response.xpath('//div[@class="career_box"]/p/text()').get()
        }
