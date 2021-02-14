import scrapy


class ThunderbrianSpider(scrapy.Spider):
    name = 'tb'
    allowed_domains = ['tb.py']
    start_urls = ['https://thunderbrian.tanahgao.synology.me/']

    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }

            Page_selector = '.next a ::attr(href)'
            next_page = response.css(Page_selector).extract_first()
            if next_page:
                yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
