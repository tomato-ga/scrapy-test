import scrapy


class BooksBasicSpider(scrapy.Spider):
    name = 'books_basic'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html']

    def parse(self, response):
        books = response.xpath('//h3')

        for book in books:
            yield{
                'title': book.xpath('.//a/text()').get(),
                'url': book.xpath('.//a/@href').get()
            }


