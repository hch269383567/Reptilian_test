

import requests
import urllib3
urllib3.disable_warnings()
"""
分析
https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&tagAll=0&page=4
最大页数   json[data][totalpage]  102    Referer:https://www.huya.com/l








"""


# url='https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&tagAll=0&page=1'
a='\u6b63\u6052\u4e36\u72c2\u4eba'
b='QQ\u98de\u8f66'
print(a.encode().decode())
# url='https://www.douyu.com/directory/all'
url='https://www.huya.com/l'
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
#https://www.huya.com/sushan
# https://www.huya.com/14112544
#https://api.huya.com/subscribe/getSubscribeStatus?callback=jQuery1111045530185887842256_1532606725037&from_key=&from_type=1&to_key=1835662129&to_type=2&_=1532606725038
# url_json='https://www.douyu.com/member/recommlist/getfreshlistajax?bzdata=1&did=6fe60c1a1ca3b51568174c2400031501&type=0&show_num=4'
# headers={
#     'Referer':'https://www.douyu.com/directory/all'
# }
# r=s.get(url_json)
# json_data=r.json()
# nick=json_data['room']
# for i in nick:
#     nickname=i['nickname']
#     print(nickname)
# urlf='https://www.huya.com/cache1min.php?m=VipBarList&tid=1417613652&sid=1417613652'#首页
# base_url='https://www.douyu.com/gapi/rkc/directory/0_0/{}'
# https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&tagAll=0&page=5
# for i in range(1,130):
#     url2=base_url.format(i)
#     # headers={
    #     'Referer':'https://www.douyu.com/'
    # }
    # r = s.get(url2)
    # json_data = r.json()
    # kk=json_data['data']['rl']
    # for j in kk:
    #     name=j['nn']
    #     rn=j['rn']
    #     fangjianhao=j['rid']
    #     game=j['c2name']
    #     rq= j['ol']
    #     if j['ol']>999999:
    #         rq=j['ol']
    #     else:
    #         rq=j['ol']/10000
    #         url4='https//www.douyu.com/{}'.format(j['rid'])
    #         r = s.get(url)
    #         json_data = r.json()
    #         fans = json_data['data']['fans']
            # print(name)
            # print(rn)
            # print(fangjianhao)
            # print(rq)
            # print(game)
            # print("粉丝数:",fans)


