

import re

from urllib import parse
from lxml import etree
import scrapy

from scrapyjuzi.items import ScrapyjuziItem


class JuziSpider(scrapy.Spider):
    name = 'juzi'

    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
    }

    base_url = 'https://www.itjuzi.com/'

    def start_requests(self):
        url = 'https://www.itjuzi.com/user/login'
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        url = 'https://www.itjuzi.com/user/login?redirect=&flag=&radar_coupon='
        headers = {
            'Referer': 'https://www.itjuzi.com/user/login',
        }
        username = '16619969594'
        password = '951117hch'
        data = {
            'identity': username,
            'password': password,
            'submit': '',
            'page': '',
            'url': ''
        }
        yield scrapy.FormRequest(url, callback=self.jobs_list, headers=headers, formdata=data)

    def jobs_list(self, response):

        a = ['K12', '留学服务', '素质教育', '语言学习', '职业培训', '赛事IP', '赛事运营', '体育培训', '体育用品', '场馆']
        for i in a:
            aa = parse.quote(i)
            url1 = 'https://www.itjuzi.com/search?word={}'.format(aa)
            meta = {
                'kw': aa
            }
            yield scrapy.Request(url1, callback=self.jobs_b, meta=meta)

    # def jobs_a(self, response):
    #     i=response.meta['kw']
    #     url='https://www.itjuzi.com/search?word={}'.format(i)
    #     yield scrapy.Request(url, callback=self.jobs_b)

    def jobs_b(self, response):
        text = response.text
        list = re.findall('<a target="_blank" href="(https://.*/company/\d.*)">', text)
        for url in list:
            yield scrapy.Request(url, callback=self.job_item)

    def job_item(self, response):

        text = response.text
        tree = etree.HTML(text)

        company = re.search('<h2 class="seo-second-title margin-right50">(.*?)</h2>', text).group(1)

        print(company)
        institution = re.search('data-name="(.*?)"', text).group(1)
        print(institution)
        #
        if "暂未收录该公司融资信息" in text:
            print("没有融资信息")
            financing = re.search('table class="list-round-v2 empty-list" data-title="(.*?)"', text).group(1)
            print(financing)
            lunshu="无"
            money="无"
            time="无"
            print(lunshu)
            print(money)
            print(time)
        else:
            financing="有融资信息"
            lunshu = tree.xpath('//*[@id="invest-portfolio"]/div/table/tbody/tr/td[2]/span/a/text()')
            money = tree.xpath('//*[@id="invest-portfolio"]/div/table/tbody/tr/td[3]/span/a/text()')
            time = tree.xpath('//*[@id="invest-portfolio"]/div/table/tbody/tr/td[1]/span[1]/text()')
            print(lunshu)
            print(money)
            print(time)

        item=ScrapyjuziItem()
        item['company'] = company
        item['institution']=institution
        item['financing']=financing
        item['lunshu']=lunshu
        item['money']=money
        item['time']=time

        yield item




