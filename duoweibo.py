#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from lxml import etree
import time
__author__ = 'Terry'

import requests
import urllib3

urllib3.disable_warnings()


class xinlangSpider:
    def __init__(self):
        s = requests.session()
        s.verify = False
        s.trust_env = False
        s.proxies = {
            'http': '127.0.0.1:8888'
        }
        s.headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9'
        }
        self.s = s

    def first(self):
        url = 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F'
        r = self.s.get(url)
        print("正在访问")

    def log_in(self):
        url = "https://passport.weibo.cn/sso/login"
        headers = {
            "Referer": "https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F"
        }
        date = {
            'username': '269383567@qq.com',
            'password': '951117hch00000',
            'savestate': '1',
            'r': 'http://m.weibo.cn/',
            'ec': '0',
            'pagerefer': '',
            'entry': 'mweibo',
            'wentry': '',
            'loginfrom': '',
            'client_id': '',
            'code': '',
            'qq': '',
            'mainpageflag': '1',
            'hff': '',
            'hfp': ''
        }
        r = self.s.post(url, data=date, headers=headers)
        json_date = r.json()
        retcode = json_date['retcode']
        if 20000000 == retcode:
            print('登录成功')
        else:
            print('登录失败')

    """
    评论页面
    需要参数： mid  : 4262351936577407  https://m.weibo.cn/api/container/getIndex?containerid=102803&openApp=0  12.26  json
                st : 5ef099     https://m.weibo.cn/   re匹配   12.24
                content  :写的内容

    """

    def next(self):
        url = 'https://m.weibo.cn/'
        r = self.s.get(url)
        text = r.text
        # print(text)
        # st: 'e222fa',
        self.st = re.search("st: '(.*?)'", text).group(1)
        # print(self.st)

    def next_n(self):
        url = 'https://m.weibo.cn/feed/friends?'
        headers = {
            'Referer': 'https://m.weibo.cn/'
        }
        r = self.s.get(url)
        json_data = r.json()
        a=[]
        for i in range(1,6):
            statuses= json_data['data']['statuses']
            a.append(statuses[i]['mid'])
        return a

    def pinlun(self, li , a):
        url = 'https://m.weibo.cn/api/comments/create'
        headers = {
            'Referer':'https://m.weibo.cn/detail/{}'.format(a)
        }
        data = {
            'content':li,
            'mid':a,
            'st':self.st
        }
        r = self.s.post(url, headers=headers, data=data)
        json_date = r.json()
        ok = json_date['ok']
        if ok == 1:
            print('发送成功')
        else:
            print("评论失败")


if __name__ == '__main__':
    xinlang=xinlangSpider()
    xinlang.first()
    xinlang.log_in()
    xinlang.next()
    xinlang.next_n()
    li=["爱你哟","快乐","么么哒","加油","国足123"]
    a=xinlang.next_n()
    print(a)
    for i in range(5):
        xinlang.pinlun(li[i],a[i])
        time.sleep(2)
