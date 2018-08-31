from urllib import parse
from urllib.parse import quote, urlencode

import requests




a='北京'
b=a.encode('GBK')
print(b)



# url='http://trains.ctrip.com/TrainBooking/Ajax/SearchListHandler.ashx?Action=searchColudTickets'
# headers={
#     'Content-Length': '62',
#     'Cache-Control': 'max-age=0',
#     'Origin': 'http://trains.ctrip.com',
#     'If-Modified-Since': 'Thu, 01 Jan 1970 00:00:00 GMT',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
#     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#     'Accept': '*/*',
#     'Referer': 'http://trains.ctrip.com/TrainBooking/Search.aspx?from=beijing&to=wuhan&day=2&fromCn=%B1%B1%BE%A9&toCn=%CE%E4%BA%BA',
#     'Accept-Encoding': 'gzip, deflate',
#     'Accept-Language': 'zh-CN,zh;q=0.9'
# }
# data={"dname":"北京",
#         "aname":"武汉",
#         "ddate":"2018-08-01"
#         }
# r=requests.post(url, headers=headers, data=data)
# text=r.text
# json_data=r.json()
