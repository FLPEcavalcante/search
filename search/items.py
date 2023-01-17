import scrapy


class SearchItem(scrapy.Item):
    """Define the fields for your item. 

    Args:
        scrapy (Web crawler): _description_
    """

    title = scrapy.Field()
    author = scrapy.Field()
    text = scrapy.Field()
    link = scrapy.Field()
    pass
