import scrapy


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

    async def parse(self, response):
        """_summary_

        Args:
            response (list): return response list in Json.

        Yields:
            _type_: _description_
        """
        for div in response.css("div"):

            text_hex = div.css('div.slider-p-2::text').getall()

            yield {'text': text_hex}
