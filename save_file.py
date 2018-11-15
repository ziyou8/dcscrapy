import requests
from lxml import etree

url = "https://book.douban.com/subject/1084336/comments/"
r = requests.get(url).text

s = etree.HTML(r)
file = s.xpath('//div[@class="comment"]/p/span/text()')

import pandas as pd

df = pd.DataFrame(file)
print(df.head())
df.to_excel('pinglun.xlsx')