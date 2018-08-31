#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from lxml import etree

__author__ = 'Terry'

import requests
import urllib3
urllib3.disable_warnings()


class DingdianSpider:

    def __init__(self):
        s = requests.session()
        s.verify = False
        s.trust_env = False
        s.proxies = {
            'http': '127.0.0.1:8888'
        }
        s.headers = {
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            # 'Host': 'www.qidian.com',   # host和 content-length 这2个参数，不需要提交
            # 'Content-length': 158     # host和 content-length 这2个参数，不需要提交
        }
        self.s=s

    def first(self):
        url = 'https://www.23us.so/'
        r = self.s.get(url)
        print('正确访问起点首页')

    def visit_xuanhuan(self):
        url = 'https://www.23us.so/list/1_1.html'
        r=self.s.get(url)

    def visit_last(self):
        url='https://www.23us.so/list/1_280.html'
        r=self.s.get(url)
        text=r.text
        page_max = re.search('<strong>(.*?)</strong>',text).group(1)
        page_max=int(page_max)
        self.page_max=page_max

    def hq_page(self):
        for i in (1,self.page_max+1):
            url='https://www.23us.so/list/1_{}.html'.format(i)
            r=self.s.get(url)
            text=r.text
            urls=re.findall(r'<a href="(.*?xiaoshuo.*?.html)">', text)
            for url in urls:
                # self.visit_info(url)
                from concurrent import futures
                with futures.ThreadPoolExecutor(max_workers=4) as executor:
                    executor.submit(self.visit_info, url)

    def visit_info(self,url):
        r = self.s.get(url)
        text = r.text
        text1=text.encode('ISO-8859-1').decode('utf-8')
        book_name=re.search('<dd><h1>(.*?) 全文阅读</h1></dd>',text1).group(1)
        aa=re.findall('<td>&nbsp;(.*?)</td>',text1)
        zz=aa[1]
        lz = aa[2]
        gx = aa[5]
        dj = aa[6]
        book_lb=re.search('<td>&nbsp;<a .*?>(.*?)</a></td>',text1).group(1)

        with open('dingdian.txt', 'a', encoding='UTF-8') as f:
            book_info = '------'.join([book_name,book_lb,zz,lz,gx,dj])
            print('获取到：', book_info)
            f.write(book_info)
            f.write('\n')


















if __name__ == '__main__':
    dingdian = DingdianSpider()
    dingdian.first()
    dingdian.visit_xuanhuan()
    dingdian.visit_last()
    dingdian.hq_page()
    dingdian.visit_info()


