import scrapy
from sreality_scrapper.items import SrealityScrapperItem


class SrealityImageSpider(scrapy.Spider):
    name = 'sreality_image'
    allowed_domains = ['sreality.cz']
    start_urls = ['https://www.sreality.cz/hledani/prodej/byty?strana=']
    max_pages = 25

    def start_requests(self):
        
        url_prefix = self.start_urls[0]
        for page in range(self.max_pages):
            url = f"{url_prefix}{page + 1}"
            yield scrapy.Request(
                url, 
                meta={
                    "playwright": True,
                    }
                )

    def parse(self, response):
        
        flat_nodes = response.xpath('//div[@class="dir-property-list"]/div[@class="property ng-scope"]')
        for flat_node in flat_nodes:
            image_url = flat_node.xpath('.//img/@src')[0].get()
            title = flat_node.xpath('.//h2/a[@class="title"]/span/text()').get().strip()
            self.log(f"Scrapped {title}.")
            yield SrealityScrapperItem(image_url=image_url, title=title)
            