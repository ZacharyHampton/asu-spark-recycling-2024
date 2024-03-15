import scrapy
from ..items import Product
import json


class BestbuySpider(scrapy.Spider):
    name = 'bestbuy'
    headers = {
        "Accept": "application/madness+json, text/plain, */*"
    }

    def start_requests(self):
        yield scrapy.Request("https://tradein.bestbuy.com/catalog/categories", callback=self.parse,
                             headers=self.headers, method="GET")

    def parse(self, response: scrapy.http.Response):
        data = json.loads(response.body)

        for category in data['items']:
            for subcategory in category['subcategories']:
                yield scrapy.Request(subcategory['uri'], callback=self.parse_category, headers=self.headers)

    def parse_category(self, response: scrapy.http.Response):
        data = json.loads(response.body)

        for item in data['results']:
            yield Product(title=item['title'], image_url=item['icon']['uri'], product_url=item['uri'])

        if data.get('more'):
            yield scrapy.Request(data['more']['uri'], callback=self.parse_category, headers=self.headers)
