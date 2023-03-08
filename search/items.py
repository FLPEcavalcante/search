import scrapy


class SearchItem(scrapy.Item):
    """Define the fields for your item. 

    Args:
        scrapy (Web crawler): Extract data from the variables below.
    """

    data = scrapy.Field()

    pass
