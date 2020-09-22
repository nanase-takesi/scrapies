import scrapy
from scrapy_redis.spiders import RedisSpider


class DangdangSpider(RedisSpider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']
    redis_key = 'book_dangdang'

    # start_urls = ['http://book.dangdang.com/']

    def parse(self, response):
        level_one_list = response.xpath('//div[@class="con flq_body"]/div[position()>2]')
        for level_one in level_one_list:
            b_cate = level_one.xpath('./dl/dt//text()').extract()
            b_cate = [i.strip() for i in b_cate if len(i) > 0]
            dl_list = level_one.xpath('./div//dl[@class="inner_dl"]')
            for dl in dl_list:
                m_cate = dl.xpath('./dt//text()').extract()
                m_cate = [i.strip() for i in m_cate if len(i) > 0][0]
                href_a_list = dl.xpath('./dd/a')
                for href_a in href_a_list:
                    s_href = href_a.xpath('./@href').extract_first()
                    s_cate = href_a.xpath('./text()').extract_first()
                    item = {
                        's_cate': s_cate,
                        'm_cate': m_cate,
                        'b_cate': b_cate,
                    }
                    if s_href is not None:
                        yield scrapy.Request(url=s_href, meta={'item': item}, callback=self.parse_book_list, )

    def parse_book_list(self, response):
        item = response.meta['item']
        book_list = response.xpath('//ul[@id="component_59"]/li')
        for book in book_list:
            item['b_title'] = book.xpath('./p[@class="name"]//text()').extract_first()
            print(item)
            yield item
