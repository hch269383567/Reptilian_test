#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from lxml import etree

__author__ = 'Terry'

import requests
import urllib3
urllib3.disable_warnings()


s = requests.session()
s.verify = False
s.trust_env = False



url2="https://www.23us.so/list/1_280.html"
r=s.get(url2)
text1=r.text
cc="<strong>(.*?)</strong>"
page_max = re.search(cc,text1).group(1)
# print(page_max)
for i in  range(1,int(page_max)+1):
    url3 ="https://www.23us.so/list/1_{}.html".format(i)
    r2=s.get(url3)
    text2=r2.text
    # print(url3)
    url4=url3
    r3=s.get(url4)
    text3=r3.text
    # print(text3)
    book_name = re.findall('<a href=".*/xiaoshuo/.*\.html">(.*?)</a>', text3)
    aa=re.findall('<td class="C">(.*?)</td>',text3)
    auther=aa[0]
    print(auther)
    # zs=re.findall('<')
    #
    # re3=r'<a href="(.*?xiaoshuo.*?.html)">'
    # urls=re.findall(re3,text3)
    # for urlq in urls:
    #     # print(urlq)
    #     rq = s.get(urlq)
    #     textq=rq.text
    #     textq=textq.encode('ISO-8859-1').decode("utf-8")
    #     # print(textq)
    #     re4='<td>&nbsp;(.*?)</td>'
    #     aa=re.findall(re4,textq,re.MULTILINE|re.DOTALL)
    #     # print(aa)
    #     zz=aa[1]
    #     lz=aa[2]
    #     gx=aa[5]
    #     dj=aa[6]
    #     lb=re.search('<td>&nbsp;<a .*?>(.*?)</a></td>',textq).group(1)
    #
    #
    #
    #
    #     xs=re.search('<dd><h1>(.*?) 全文阅读</h1></dd>',textq).group(1)
    #     # print(xs)
    #
    #     with open('dingdian.txt', 'a', encoding='UTF-8') as f:
    #         book_info = '------'.join(["小说:"+xs,"作者:"+zz,"类别："+lb,"状态："+lz,"跟新："+gx,"点击数:"+dj])
    #         print('获取到：', book_info)
    #         f.write(book_info)
    #         f.write('\n')

