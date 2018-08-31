import json
import re
import scrapy

from scrapyhuya.items import ScrapyhuyaItem


class HuyaSpider(scrapy.Spider):
    name = 'huya'

    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
    }
    base_url='https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&tagAll=0&page={}'

    def start_requests(self):
        for i in range(1,10):
            url=self.base_url.format(i)
            yield scrapy.Request(url, callback=self.get_json)

    def get_json(self,response):
        text = response.text
        json_data = json.loads(text)
        kk=json_data['data']
        list=kk['datas']
        for i in list:
            meta={
            'name':i['nick'],
            'biaoti':i['introduction'],
            'fangjianhao':i['profileRoom'],
            'hot':i['totalCount'],
            'game':i['gameFullName']}
            url='https://www.huya.com/{}'.format(i['profileRoom'])
            yield scrapy.Request(url,callback=self.get_fans,meta=meta)

    def get_fans(self,response):
        text = response.text
        fans=re.search(',"fans":(.*?),',text).group(1)
        item=ScrapyhuyaItem()
        item['name']=response.meta['name']
        item['fangjianhao']=response.meta['fangjianhao']
        item['hot']=response.meta['hot']
        item['biaoti']=response.meta['biaoti']
        item['game']=response.meta['game']
        item['fans']=fans
        yield  item
