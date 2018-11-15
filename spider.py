import requests

"""
r = requests.get('https://book.douban.com/subject/1084336/comments')
print(r.status_code)
print(r.text)
print(r.raise_for_status)
"""

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=20)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "There is an Exception."

if __name__ == '__main__':
    url = " "
    print(getHTMLText(url))
