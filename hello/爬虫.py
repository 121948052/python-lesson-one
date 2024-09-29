'''
Author: Bug Router
Date: 2024-09-29 11:05:32
Description: Default
'''
from urllib.request import urlopen, Request



headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'}

req = Request("https://baijiahao.baidu.com/s?id=1802074684289117381&wfr=spider&for=pc", headers=headers)

html = urlopen(req)

html_text = bytes.decode(html.read())

print(html_text)