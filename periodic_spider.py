import scrapy


class PeriodicSpider(scrapy.Spider):
    start_urls = ["http://www.lenntech.com/periodic/name/alphabetic.htm"]
    name = "periodicSpider"

    def parse(self, response):
        for element in response.css("table tbody tr"):
            name = element.css("td:nth-child(2) strong ::text").extract_first()
            code = element.css("td:nth-child(3) strong ::text").extract_first()
            number = element.css("td:nth-child(4) ::text").extract_first()

            """
            Middle part has rowspan, which means the elements here will start from index 1
            This section will compensate for this
            """
            if not number and not code:
                name = element.css("td:nth-child(1) strong ::text").extract_first()
                code = element.css("td:nth-child(2) strong ::text").extract_first()
                number = element.css("td:nth-child(3) ::text").extract_first()

            """
            Return if name code and number has value, this will skip empty and the first header row
            """
            if name and code and number:
                yield {"name": name, "code": code, "atomic_number": number}
