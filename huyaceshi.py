
import requests
import re

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

url='https://www.huya.com/15886279'
r=s.get(url)

text=r.text
#"fans":10389
aa=re.search('"fans":(.*?),',text).group(1)
print(aa)

# https://www.douyu.com/swf_api/h5room/2136878?v=220120180725&did=6993ca0405c567f5e07cf30000051501&tt=25541990&sign=4102200c72b6dfafa506f3cf4677fb4c&cdn=&nofan=yes&_t=25541990
url='https://www.douyu.com/swf_api/h5room/2136878'
r=s.get(url)
json_data = r.json()
fans=json_data['data']['fans']
# https://www.douyu.com/2136878
# https://www.douyu.com/4417046