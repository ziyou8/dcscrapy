import requests
from lxml import etree

url = "https://book.douban.com/subject/1084336/comments/"
r = requests.get(url).text

s = etree.HTML(r)
file = s.xpath('//div[@class="comment"]/p/span/text()')

with open('pinglun.txt', 'w', encoding='utf-8') as f:
    for i in file:
        f.write(i)
        f.write('/n')

