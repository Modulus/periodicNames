import scrapy


class PeriodicSpider(scrapy.Spider):
    start_urls = ["http://www.lenntech.com/periodic/name/alphabetic.htm"]
    name = "periodicSpider"

    def parse(self, response):
        for strong in response.css("table tbody tr td:nth-child(2) strong"):
            name = strong.css("a ::text").extract_first()
            link = strong.css("a ::attr(href)").extract_first()
            if name and "http" in link:
                yield { "name": strong.css("a ::text").extract_first()}
