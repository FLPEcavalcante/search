import scrapy


class TecnoblogSpider(scrapy.Spider):
    name = 'YouTube'
    allowed_domains = ['youtube.com']
    start_urls = ['http://youtube.com']

    def parse(self, response):
        for article in response.css("article"):
            link = article.css("div.texts h2 a::attr(href)").extract_first()
            title = article.css("div.texts h2 a::text").extract_first()
            author = article.css("div.texts div.info a::text").extract_first()

            yield {'link': link, 'title': title, 'author': author}