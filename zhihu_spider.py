# _*_ coding:utf8 _*_

import requests
import pandas as pd
import time

headers = {
    'cookie': 'd_c0="AICA7nYyrgmPTlEujltKkMdwhVGsJ1uoDxo=|1459088993"; __utma=51854390.700995760.1392106379.1483076446.1483422422.3; __utmv=51854390.100-1|2=registration_date=20111115=1^3=entry_date=20111115=1; q_c1=c835f85eb0f74d36a7f5e0ad4c63d912|1508319179000|1401874015000; __DAYU_PP=uaaBZZnFiByEmmJ7u3NAfffffffff3edfb1b6ccf; _xsrf=gcjTk6KobflKgrsnDuYyQC1Hg6q0x49V; _zap=212818ea-9bf6-482b-83cc-db9e91f3c79f; capsion_ticket="2|1:0|10:1540966657|14:capsion_ticket|44:ZjZhOTdkZWMwYzM1NDVkOTkxNTI3ZGVmYTdjZjQ0MmM=|354cf00c6f46f246045a51d3be8c27c7dd417a53009abf4194b649104c914ef6"; z_c0="2|1:0|10:1540966659|4:z_c0|92:Mi4xRVF3Q0FBQUFBQUFBZ0lEdWRqS3VDU1lBQUFCZ0FsVk5BNWZHWEFDY1ByZXRGU1NmRThBREJwQ3VfcXVvaFJVVEZ3|a7a31621abe3814050bf9c66a047944ef10927ca5b8f03762f8547c4e57fbf10"; tst=r; q_c1=c835f85eb0f74d36a7f5e0ad4c63d912|1542260075000|1401874015000; tgw_l7_route=23ddf1acd85bb5988efef95d7382daa0',
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