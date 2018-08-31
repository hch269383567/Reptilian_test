import re
from urllib import parse
import scrapy

from dingscrapy.items import DingdianItem


class DingdianSpider(scrapy.Spider):
    name = 'dingdian'

    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9'}
    }

    base_url = 'https://www.23us.so/list/{}_{}.html'

    def start_requests(self):
        """
            访问 初始页
        :return:
        """
        url = 'https://www.23us.so/list/1_1.html'
        yield scrapy.Request(url,callback=self.parse)

    def parse(self, response):
        text = response.text
        for i in range(1,10):
            url=self.base_url.format(i,1)
            print(url)
            meta={
                'a': i
            }
            yield scrapy.Request(url, callback=self.parse_next, meta=meta,dont_filter=True )
    def parse_next(self,response):
        text = response.text
        a=response.meta['a']
        page_max=re.search('<a href=".*\.html" class="last">(.*?)</a>', text).group(1)
        print('最大页数:',page_max)
        for j in range(1,int(page_max)+1):
            url=self.base_url.format(a,j)
            yield scrapy.Request(url, callback=self.parse_item)

    def parse_item(self, response):
        text = response.text
        # 获取书名
        book_name = re.findall('<a href=".*/xiaoshuo/.*\.html">(.*?)</a>', text)
        aa = re.findall('<td class="C">(.*?)</td>', text)
        # 获取字数
        zs = re.findall('<td class="R">(.*?)</td>', text)
        # 获取作者
        zz = []
        for i in range(0, len(aa), 3):
            zz.append(aa[i])
        # 获取跟新时间
        gx = []
        for i in range(1, len(aa), 3):
            gx.append(aa[i])

        for book_name, zz, gx, zs in zip(book_name, zz, gx, zs):
            Item = DingdianItem()
            Item['book_name'] = book_name
            Item['zz'] = zz
            Item['gx'] = gx
            Item['zs'] = zs
            yield Item
