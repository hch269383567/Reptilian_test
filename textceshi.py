import re
from urllib import parse
from lxml import etree
import requests



s = requests.session()
s.trust_env = False
s.verify = False
s.headers={
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}
# url='https://www.itjuzi.com/user/login'


url='https://www.itjuzi.com/user/login?redirect=&flag=&radar_coupon='
headers={
    'Content-Length': '58',
    'Cache-Control': 'max-age=0',
    'Origin': 'https://www.itjuzi.com',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'https://www.itjuzi.com/user/login',
}
username ='16619969594'
password ='951117hch'
data={
    'identity': username ,
    'password': password ,
    'submit': '',
    'page': '2',
    'url': ''
}
r=s.post(url, headers=headers, data=data)
text=r.text
# print(text)
#https://www.itjuzi.com/search?word=%E7%95%99%E5%AD%A6%E6%9C%8D%E5%8A%A1
# a='留学服务'
a=['K12', '留学服务', '素质教育', '语言学习', '职业培训', '赛事IP', '赛事运营', '体育培训', '体育用品', '场馆']
for i in a:
    aa=parse.quote(i)
    url='https://www.itjuzi.com/search?word={}'.format(aa)
    r=s.get(url)
    text1=r.text
    # print(text)
    # <a target="_blank" href="https://www.itjuzi.com/company/68987">
    gs=re.findall('<a target="_blank" href="(https://.*/company/\d.*)">',text1)
    for i in gs:
        r=s.get(i)
        text=r.text
        tree = etree.HTML(text)
        # print(text)
        pt=re.search('<h2 class="seo-second-title margin-right50">(.*?)</h2>',text).group(1)
        # pt=tree.xpath()
        print(pt)
        mc=re.search('data-name="(.*?)"',text).group(1)
        print(mc)
        #
        if "暂未收录该公司融资信息" in text:
            print("没有融资信息")
            rz = re.search('table class="list-round-v2 empty-list" data-title="(.*?)"', text).group(1)
            print(rz)
        else:
            ls=tree.xpath('//*[@id="invest-portfolio"]/div/table/tbody/tr/td[2]/span/a/text()')
            je=tree.xpath('//*[@id="invest-portfolio"]/div/table/tbody/tr/td[3]/span/a/text()')
            sj = tree.xpath('//*[@id="invest-portfolio"]/div/table/tbody/tr/td[1]/span[1]/text()')
            print(ls)
            print(je)
            print(sj)




