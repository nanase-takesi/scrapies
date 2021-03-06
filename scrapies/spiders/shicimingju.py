import scrapy
from urllib import parse
from scrapies.items import AuthorItem


class ShicimingjuSpider(scrapy.Spider):
    name = 'shicimingju'
    allowed_domains = ['www.shicimingju.com']
    start_urls = ['http://www.shicimingju.com/']

    def parse(self, response):
        yield scrapy.Request(url=parse.urljoin(response.url, '/category/all'), callback=self.parse_author_list, )

    def parse_author_list(self, response):
        author_list = response.xpath('//div[@id="main_left"]/div[@class="card zuozhe_card"]')
        for author in author_list:
            id = author.xpath('./div[@class="list_num_info"]/text()').extract_first()
            href = author.xpath('./div[@class="zuozhe_list_item"]//a/@href').extract_first()
            meta = {
                'id': id.strip(),
            }
            yield scrapy.Request(url=parse.urljoin(response.url, href), meta=meta, callback=self.parse_author_detail, )

        next_page_url = response.xpath('//div[@id="list_nav_part"]/a[text()="下一页"]/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(url=parse.urljoin(response.url, next_page_url), callback=self.parse_author_list, )

    def parse_author_detail(self, response):
        id = response.meta["id"]
        about_author = response.xpath('//div[@id="main_right"]/div[@class="card about_zuozhe"]')
        name = about_author.xpath('.//div/h4//text()').extract_first()
        descs = about_author.xpath('.//div[@class="des"]//text()').extract()
        dynasty = about_author.xpath('.//div[@class="aside_left"]/div[@class="aside_val"]//text()').extract_first()
        take_count = about_author.xpath('.//div[@class="aside_right"]/div[@class="aside_val"]//text()').extract_first()

        authorItem = AuthorItem()
        authorItem['name'] = name
        authorItem['desc'] = "".join(descs).strip()
        authorItem['dynasty'] = dynasty
        authorItem['take_count'] = take_count[0: -1]
        yield authorItem
