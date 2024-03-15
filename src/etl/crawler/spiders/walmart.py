import scrapy
from ..items import Product


class WalmartSpider(scrapy.Spider):
    name = 'walmart'
    start_urls = ['https://walmart.cexchange.com/online/home/index.rails']

    def parse(self, response: scrapy.http.Response):
        for href in response.css('#navbar > ul.nav.navbar-nav.desktop-nav > li.dropdown > ul > li > a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_category)

    def parse_category(self, response: scrapy.http.Response):
        container = response.css('#Container')

        for div in container.css('div'):
            element = div.css('div::attr(onclick)').extract_first()

            if element:
                url = response.urljoin(element.split("'")[1])

                conditional = url.split('/Online/')[1].split('.rails')[0]

                match conditional:
                    case "Home/ManufacturerSelectedPaged":
                        yield scrapy.Request(url, callback=self.parse_category)
                    case "Home/ModelSelected":
                        yield scrapy.Request(url, callback=self.parse_category)
                    case "Cart/BeginAppraisal-ShowAppraisalForm":
                        yield scrapy.Request(url, callback=self.parse_product, cb_kwargs={'product_url': url})

        if next_page := response.css('#PageBarNext::attr(href)'):
            yield scrapy.Request(response.urljoin(next_page.extract_first()), callback=self.parse_category)

    def parse_product(self, response: scrapy.http.Response, product_url: str):
        product_name = response.css('#appraisal-name::text').extract_first()
        image_url = response.css('#form1 > div.col-md-5 > img::attr(src)').extract_first()

        yield Product(title=product_name, image_url=image_url, product_url=product_url)


