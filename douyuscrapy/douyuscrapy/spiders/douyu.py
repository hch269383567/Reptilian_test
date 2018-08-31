import json
import re

from urllib import parse, response

import time
from lxml import etree
import scrapy
import random
from douyuscrapy.items import DouyuscrapyItem


class DouyuSpider(scrapy.Spider):
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

    base_url='https://www.douyu.com/gapi/rkc/directory/0_0/{}'

    def start_requests(self):
        for i in range(2,3):
            url=self.base_url.format(i)
            yield scrapy.Request(url, callback=self.get_json)

    def get_json(self, response):
        text=response.text
        json_data = json.loads(text)
        kk = json_data['data']['rl']
        for j in kk:
            meta={
            'name' :j['nn'],
            'biaoti' : j['rn'],
            'fangjianhao' : j['rid'],
            'game' : j['c2name'],
            'hot' :j['ol']}
            if j['ol'] > 999999:
                rq = j['ol']
            else:
                rq = j['ol'] / 10000
            url='https://www.douyu.com/swf_api/h5room/{}'.format(j['rid'])
            yield scrapy.Request(url,callback=self.get_fans,meta=meta)

    def get_fans(self, response):
        text = response.text
        json_data = json.loads(text)
        try:
            if json_data['data']['fans']:
                fans=json_data['data']['fans']
                item = DouyuscrapyItem()
                item['name'] = response.meta['name']
                item['biaoti'] = response.meta['biaoti']
                item['fangjianhao'] = response.meta['fangjianhao']
                item['game'] = response.meta['game']
                item['hot'] = response.meta['hot']
                item['fans'] = fans
                yield item
        except:
            fans=''
            item = DouyuscrapyItem()
            item['name'] = response.meta['name']
            item['biaoti'] = response.meta['biaoti']
            item['fangjianhao'] = response.meta['fangjianhao']
            item['game'] = response.meta['game']
            item['hot'] = response.meta['hot']
            item['fans']=fans
            yield item