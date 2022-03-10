import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from amazonrank.spiders.amazon import AmazonSpider

process = CrawlerProcess(settings=get_project_settings())
process.crawl(AmazonSpider)
process.start()