import scrapy

from search.items import SearchItem


class Hex360(scrapy.Spider):
    """_summary_

    Args:
        scrapy (_type_): _description_

    Returns:
        _type_: _description_

    Yields:
        _type_: _description_
    """
    name = 'Hex360'
    allowed_domains = ['hex360.com.br']
    start_urls = ['https://www.hex360.com.br/']

    def parse(self, response):
        """Metho the extract

        Args:
            response (list): return response list in Json.

        Yields:
            _type_: _description_
        """

        for div in response.css('div'):

            link = div.css('h1.tit-base.solucoes::text').extract()
            title = div.css('div.slider-p-2.top::text').extract()
            text = div.css('div.slider-p-2.top::text').extract()

            yield {'link': link, 'title': title, 'text': text}
