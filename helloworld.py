import requests
from lxml import etree

url = "https://book.douban.subject/1084336/comments/"
r = requests.get(url).text

s = etree.HTML(r)
print(s.xpath(''))  # 浏览器复制
