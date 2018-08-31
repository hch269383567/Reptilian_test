import requests
from lxml import etree
import re
from urllib.request import urlretrieve


def download():
    url="http://www.pearvideo.com/category_9"
    html=requests.get(url).text
    html=etree.HTML(html)


    video_id=html.xpath('//div[@class="vervideo-bd"]/a/@href')

    video_url=[]
    starturl="http://www.pearvideo.com"


    for id in video_id:
        newurl=starturl+'/'+id
        video_url.append(newurl)

    for playurl in video_url:
        html=requests.get(playurl).text
        req='srcUrl="(.*?)"'
        purl=re.findall(req,html)
        req='<h1 class="video-tt">(.*?)</h1>'
        pname=re.findall(req,html)
        print("正在下载视屏:%s" %pname[0])
        urlretrieve(purl[0],'d:/video/%s.mp4'%pname[0])
download()