# _*_ coding:utf8 _*_

import requests
import pandas as pd
import time

headers = {
    'cookie': '',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
}

user_data = []
def get_user_data(page):
    for i in range(page):
        url = 'https://www.zhihu.com/api/v4/members/excited-vczh/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset={}&limit=20'.format(i*20)
        response = requests.get(url, headers=headers).json()['data']
        user_data.extend(response)
        print("正在爬取第%s页" % str(i+1))
        time.sleep(1)

if __name__ == '__main__':
    get_user_data(10)
    df = pd.DataFrame.from_dict(user_data)
    df.to_csv('user.csv')