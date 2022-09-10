import scrapy


#class SrealityScrapperItem(scrapy.Item):
#    title = scrapy.Field()
#    image_url = scrapy.Field()

from dataclasses import dataclass

@dataclass
class SrealityScrapperItem:
    title: str
    image_url: str
