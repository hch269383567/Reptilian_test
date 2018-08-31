import requests
from lxml import etree
import re
from urllib.request import urlretrieve


url="https://www.qidian.com/rank/hotsales?chn=4"
html = requests.get(url).text
html = etree.HTML(html)
# <a href="//book.qidian.com/info/1010191960"
# target="_blank" data-eid="qd_C40" data-bid="1010191960">大王饶命</a>
a='<a href=(.*?)target="_blank" data-eid="qd_C40"'
c=re.findall(a,html)
