import pickle
import time
import re
from requests.cookies import RequestsCookieJar
from selenium.webdriver.common.by import By
from selenium import webdriver
import requests
import json
import random
import datetime
import pymysql.cursors
from urllib import parse




#http://hotels.ctrip.com/Domestic/Tool/AjaxHotelList.aspx
url='http://hotels.ctrip.com/Domestic/Tool/AjaxHotelList.aspx'  #json数据没有价格
dq='北京'
city=parse.quote(dq)
for k in range(1,500):
    headers={
        'Content-Length': '1800',
        'Cache-Control': 'max-age=0',
        'Origin': 'http://hotels.ctrip.com',
        'If-Modified-Since': 'Thu, 01 Jan 1970 00:00:00 GMT',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': '*/*',
        'Referer': 'http://hotels.ctrip.com/domestic/hotel/beijing1',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    data={
        '__VIEWSTATEGENERATOR': 'DB1FBB6D',
        'cityName': city,
        'StartTime': '2018-08-14',
        'DepTime': '2018-08-15',
        'RoomGuestCount': '1,1,0',
        'txtkeyword': '',
        'Resource': '',
        'Room': '',
        'Paymentterm': '',
        'BRev': '',
        'Minstate': '',
        'PromoteType': '',
        'PromoteDate': '',
        'operationtype': 'NEWHOTELORDER',
        'PromoteStartDate': '',
        'PromoteEndDate': '',
        'OrderID': '',
        'RoomNum': '',
        'IsOnlyAirHotel': 'F',
        'cityId': '1',
        'cityPY': 'beijing',
        'cityCode': '010',
        'cityLat': '39.9105329229',
        'cityLng': '116.413784021',
        'positionArea': '',
        'positionId': '',
        'hotelposition': '',
        'keyword': '',
        'hotelId': '',
        'htlPageView': '0',
        'hotelType': 'F',
        'hasPKGHotel': 'F',
        'requestTravelMoney': 'F',
        'isusergiftcard': 'F',
        'useFG': 'F',
        'HotelEquipment': '',
        'priceRange': '-2',
        'hotelBrandId': '',
        'promotion': 'F',
        'prepay': 'F',
        'IsCanReserve': 'F',
        'OrderBy': '99',
        'OrderType': '',
        'k1': '',
        'k2': '',
        'CorpPayType': '',
        'viewType': '',
        'checkIn': '2018-08-17',
        'checkOut': '2018-08-18',
        'DealSale': '',
        'ulogin': '',
        'hidTestLat': '0%7C0',
        'AllHotelIds': '439311%2C452197%2C6410223%2C535615%2C1641390%2C374791%2C456474%2C469749%2C375265%2C939388%2C8105721%2C16094681%2C14095879%2C431617%2C14131570%2C375126%2C9293254%2C2231618%2C691682%2C7514902%2C444199%2C12052851%2C1563509%2C9557111%2C436066',
        'psid': '',
        'isfromlist': 'T',
        'ubt_price_key': 'htl_search_result_promotion',
        'showwindow': '',
        'defaultcoupon': '',
        'isHuaZhu': 'False',
        'hotelPriceLow': '',
        'htlFrom': 'hotellist',
        'unBookHotelTraceCode': '',
        'showTipFlg': '',
        'hotelIds': '439311_1_1,452197_2_1,6410223_3_1,535615_4_1,1641390_5_1,374791_6_1,456474_7_1,469749_8_1,375265_9_1,939388_10_1,8105721_11_1,16094681_12_1,14095879_13_1,431617_14_1,14131570_15_1,375126_16_1,9293254_17_1,2231618_18_1,691682_19_1,7514902_20_1,444199_21_1,12052851_22_1,1563509_23_1,9557111_24_1,436066_25_1',
        'markType': '0',
        'zone': '',
        'location': '',
        'type': '',
        'brand': '',
        'group': '',
        'feature': '',
        'equip': '',
        'bed': '',
        'breakfast': '',
        'other': '',
        'star': '',
        'sl': '',
        's': '',
        'l': '',
        'price': '',
        'a': '0',
        'keywordLat': '',
        'keywordLon': '',
        'contrast': '0',
        'PaymentType': '',
        'CtripService': '',
        'promotionf': '',
        'contyped': '0',
        'productcode': '',
        'page':k,
    }
    # time.sleep(random.randrange(1,10))
    r=requests.post(url, headers=headers, data=data)
    try:
        if r.json:
            text = r.text
            # <span class=\"J_price_lowList\">816</span>
            jg1 = re.findall(r'<span class=\\"J_price_lowList\\">(.*?)</span>', text)
            json_data=r.json()
            jdlist=json_data['hotelPositionJSON']
            for i in range(len(jdlist)):
                name = jdlist[i]['name']
                dq=dq
                pf = jdlist[i]['score']
                min_money = jg1[i]
                dd = jdlist[i]['address']
                lx = jdlist[i]['stardesc']
                dp = jdlist[i]['dpcount']
                tj = jdlist[i]['dpscore']
                print(min_money,name)
                    # 连接数据库
                conn = pymysql.connect(host="localhost", user="root", password="1234", db="xiecheng", port=3306, charset="utf8")
                # 获取游标  通过游标对象可以操作数据库
                cur = conn.cursor()
                sql = "insert into hotels(name,dq, pf, min_money, dd, lx, dp,tj) VALUES ('%s', '%s', '%s', '%s', '%s','%s','%s','%s')" %(name,dq, pf, min_money, dd, lx, dp,tj)
                # 执行sql操作
                cur.execute(sql)
                # 获取结果
                # 获取所有结果
                # 释放资源
                conn.commit()
                cur.close()
                conn.close()
    except :
        text=r.text
        names=re.findall('"name":"(.*?)"',text)
        pfs=re.findall('"score":"(.*?)"',text)
        dq=dq
        dds=re.findall('"address":"(.*?)"',text)
        lxs=re.findall('"stardesc":"(.*?)"',text)
        dps=re.findall('"dpcount":"(.*?)"',text)
        tjs=re.findall('"dpscore":"(.*?)"',text)
        jg1 = re.findall(r'<span class=\\"J_price_lowList\\">(.*?)</span>', text)
        for name, pf, min_money, dd, lx, dp,tj in zip(names, pfs, jg1, dds, lxs, dps,tjs):
            name=name
            pf=pf
            dd=dd
            lx=lx
            dp=dp
            tj=tj
            min_money=min_money
            dq=dq
            print(name,pf)
            conn = pymysql.connect(host="localhost", user="root", password="1234", db="xiecheng", port=3306,
                                   charset="utf8")
            # 获取游标  通过游标对象可以操作数据库
            cur = conn.cursor()
            sql = "insert into hotels(name,dq, pf, min_money, dd, lx, dp,tj) VALUES ('%s', '%s', '%s', '%s', '%s','%s','%s','%s')" % (
                name, dq, pf, min_money, dd, lx, dp, tj)
            # 执行sql操作
            cur.execute(sql)
            # 获取结果
            # 获取所有结果
            # 释放资源
            conn.commit()
            cur.close()
            conn.close()
