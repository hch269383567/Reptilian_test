#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from lxml import etree

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
        text = r.text
        # print(text)
        # self.uid = re.search('"uid":"(.*?)"', text).group(1)

        url3='https://m.weibo.cn/message/msglist?page=1'
        headers = {
            'Referer': 'https://m.weibo.cn/message',
        }
        r=self.s.post(url3 ,headers=headers)
        json_data = r.json()
        retcode = json_data['data'][1]
        self.uid = retcode['user']['id']
        url2 = 'https://m.weibo.cn/api/config'
        r = self.s.get(url2)
        text = r.text
        # print(text)
        self.st = re.search('"st":"(.*?)"', text).group(1)

    #
    def xx(self,msg):
        # url1='https://m.weibo.cn/api/chat/list?uid=1642909335&count=10&unfollowing=0'
        url1 = 'https://m.weibo.cn/api/chat/send'
        headers = {
            'Referer': 'https://m.weibo.cn/message/chat?uid={}&name=msgbox'.format(self.uid),
        }
        date = {
            'uid': self.uid,
            'content': msg,
            'st': self.st,
        }
        r = self.s.post(url1, headers=headers, data=date)
        json_date = r.json()
        ok=json_date['ok']
        if ok==1:
            print('发送成功')
        # print(json_date)
        # sender_id=json_date['date']['msgs']['0']['sender_id']
        # print(sender_id)

        # i=
        # url="https://m.weibo.cn/message/chat?uid={i}&name=msgbox"
        # # \u5fae\u535a\u5c0f\u79d8\u4e66   微博小秘书


if __name__ == '__main__':
    xinlang = xinlangSpider()
    xinlang.first()
    xinlang.log_in()
    msg="ceshifasongshuju"
    xinlang.xx(msg)
