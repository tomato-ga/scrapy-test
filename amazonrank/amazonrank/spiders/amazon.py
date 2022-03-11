import scrapy
from amazonrank.items import AmazonrankItem
from scrapy.loader import ItemLoader

"""response.follow: 商品ページのリンクに.get()を付け忘れていた
logging 入れたら動かない？"""


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['www.amazon.co.jp']
    start_urls = ['https://www.amazon.co.jp/gp/bestsellers/electronics/3371421']

    def parse(self, response):
        ranks = response.xpath('//div[contains(@class, "zg-grid-general-faceout")]')
        # logging.debug ({
        #     "response.status": response.url,
        #     "response.rank": response.rank
        # })

        for rank in ranks:
            # urls = rank.xpath('.//div[@class="zg-grid-general-faceout"]/div/a[1]/@href').get()
            # product = rank.xpath('.//img[@class="a-dynamic-image p13n-sc-dynamic-image p13n-product-image"]/@alt').getall()

            yield response.follow(url=rank.xpath('.//div/a/@href').get(), callback=self.parse_item) # #div[@class="zg-grid-general-faceout"]/div/a[1]/@href

    def get_name(self, title):
        if title:
            return title.strip()
        return title

    def get_price(self, price):
        if price:
            return int(price.replace(',', ''))
        return price

    def get_rating(self, rating):
        if rating:
            return rating.replace('個の評価', 'レビュー')
        return rating

    def parse_item(self, response):
        main_info = response.xpath('//div[@id="centerCol"]')

        loader = ItemLoader(item=AmazonrankItem(), response=response)
        loader.add_xpath('title',  "//span[@id='productTitle']/text()")
        loader.add_xpath('price', "//span[@class='a-price-whole']/text()")
        loader.add_xpath('rating', "//span[@id='acrCustomerReviewText']/text()")
        yield loader.load_item()

        # yield {
        #     'title': self.get_name(main_info.xpath(".//span[@id='productTitle']/text()").get()),
        #     'price': self.get_price(main_info.xpath(".//span[@class='a-price-whole']/text()").get()),
        #     'rating': self.get_rating(main_info.xpath(".//span[@id='acrCustomerReviewText']/text()").get())
        # }