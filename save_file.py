import requests
import pandas as pd
from lxml import etree

url = "https://book.douban.com/subject/1084336/comments/"
r = requests.get(url).text

s = etree.HTML(r)
file = s.xpath('//div[@class="comment"]/p/span/text()')

df = pd.DataFrame(file)
print(df.head())
df.to_excel('pinglun.xlsx')