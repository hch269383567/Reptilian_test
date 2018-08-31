from lxml import etree

import requests
import urllib3
urllib3.disable_warnings()
import re


# url='https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0' #首页
# url1='https://m.douban.com/rexxar/api/v2/gallery/subject_feed?start=0&count=4&subject_id=1292720&ck=null' #内容

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

#分页 https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=9920
#内容   https://m.douban.com/rexxar/api/v2/gallery/subject_feed?start=0&count=4&subject_id=1292052&ck=null

# a='\u8096\u7533\u514b\u7684\u6551\u8d4e'
# print(a.encode().decode())
base_url='https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start={}'

for i in range(1,9920,20):
    url2=base_url.format(i)
    r=s.get(url2)
    json_data=r.json()
    dd=json_data['data']
    for j in dd:
        directors=j['directors']
        move=j['title']
        casts=j['casts']
        rate=j['rate']
        id=j['id']
        print(move)
        print(directors)
        print(casts)
        print(rate)

url='https://movie.douban.com/subject/1295644'
r=s.get(url)
text=r.text
tree=etree.HTML(text)
leixing=tree.xpath('//span[@property="v:genre"]/text()')
diqu=re.search('<span class="pl">制片国家/地区:</span>(.*?)<br/>',text).group(1)
print(leixing)
print(diqu)


