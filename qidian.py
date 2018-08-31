#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from lxml import etree

__author__ = 'Terry'

import requests
import urllib3
urllib3.disable_warnings()

class QidianSpider:

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

        self.s = s

    def visit_index(self):
        url = 'https://www.qidian.com/'
        r = self.s.get(url)
        print('正确访问起点首页')

    def visit_dushi(self):
        url = 'https://www.qidian.com/dushi'
        headers = {
            'Referer': 'https://www.qidian.com/'
        }
        r = self.s.get(url, headers=headers)

    def visit_hotsales(self):
        url = 'https://www.qidian.com/rank/hotsales?chn=4'
        headers = {
            'Referer': 'https://www.qidian.com/dushi'
        }
        r = self.s.get(url, headers=headers)
        text = r.text
        html = etree.HTML(text)

        # page_max = re.search(r'data-pageMax="(.*?)"', text).group(1)
        page_max=html.xpath('//data-pageMax=')
        print(page_max)
        page_max = int(page_max)

        self.page_max = page_max

    def visit_hotsales_all_page(self):
        headers = {
            'Referer': 'https://www.qidian.com/rank/hotsales?chn=4'
        }
        for i in range(1, self.page_max+1):
            url = "https://www.qidian.com/rank/hotsales?chn=4&page={}".format(i)
            r = self.s.get(url, headers=headers)
            text = r.text

            urls = re.findall(r'class="book-img-box".*?href="(.*?)".*?data-eid="qd_C39"', text)

            for url in urls:
                # url 类似：//book.qidian.com/info/1005399587
                url = 'https:' + url
                self.visit_info(url)

    def visit_info(self, url):
        headers = {
            'Referer': 'https://www.qidian.com/rank/hotsales?chn=4'
        }

        r = self.s.get(url, headers=headers)
        text = r.text

        # book_name = re.search(r'class="book-info ".*?<em>(.*?)</em>', text, re.S).group(1)


        # auther = re.search(r'data-eid="qd_G08">(.*?)</a>', text).group(1)

        try:
            catalog_count = re.search(r'id="J-catalogCount">\((.*?)章\)</span>', text).group(1)
        except:
            catalog_count = '没有获取到章节数'

        with open('qidian.txt', 'a', encoding='UTF-8') as f:
            book_info = '------'.join([book_name, auther, catalog_count])
            print('获取到：', book_info)
            f.write(book_info)
            f.write('\n')


if __name__ == '__main__':
    qidian = QidianSpider()
    qidian.visit_index()
    qidian.visit_dushi()
    qidian.visit_hotsales()
    qidian.visit_hotsales_all_page()
