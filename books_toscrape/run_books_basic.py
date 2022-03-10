import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from books_toscrape.spiders.books_basic import BooksBasicSpider

process = CrawlerProcess(settings=get_project_settings())
process.crawl(BooksBasicSpider)
process.start()