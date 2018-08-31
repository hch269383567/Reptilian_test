import json
import re

from urllib import parse, response
from lxml import etree
import scrapy
import time
import random

from douyu1scrapy.items import Douyu1ScrapyItem


class Douyu1Spider(scrapy.Spider):
    name = 'douyu'

    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
    }
    base_url='https://www.douyu.com/gapi/rkc/directory/2_201/{}'
    #  https://www.douyu.com/gapi/rkc/directory/2_201/2
    def start_requests(self):
        for i in range(1,6):
            url=self.base_url.format(i)
            yield scrapy.Request(url, callback=self.get_json,dont_filter=True)

    def get_json(self, response):
        text = response.text
        json_data = json.loads(text)
        kk = json_data['data']['rl']
        for j in kk:
            meta={ 'tupian':j['rs1'],
            'name':j['nn'],
            'fangjianhao':j['rid'],
            'hot' : j['ol']}
            if j['ol'] > 999999:
                rq = j['ol']
            else:
                rq = j['ol'] / 10000
            url='https://www.douyu.com/swf_api/h5room/{}'.format(j['rid'])
            yield scrapy.Request(url,callback=self.get_fans,meta=meta)


    def get_fans(self,response):
        text = response.text
        json_data=json.loads(text)
        fans=json_data['data']['fans']
        item = Douyu1ScrapyItem()
        item['tupian'] = response.meta['tupian']
        item['name'] = response.meta['name']
        item['fangjianhao'] = response.meta['fangjianhao']
        item['hot']=response.meta['hot']
        item['fans']=fans
        yield item
