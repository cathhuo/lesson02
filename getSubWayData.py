# -*- encoding:utf-8 -*-

import requests
import urllib
from bs4 import BeautifulSoup
s = requests.Session()
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate, sdch, br',
'Accept-Language': 'zh-CN,zh;q=0.8',
'Connection': 'keep-alive',
'Host': 'baike.baidu.com',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}


res = s.get("https://baike.baidu.com/item/北京地铁/408485", allow_redirects=False, headers=headers)

r = res.text
print(requests.utils.get_encodings_from_content(r)[0])
res_encoded = r.encode("ISO-8859-1").decode(requests.utils.get_encodings_from_content(r)[0])
# res_encoded = res_encoded.encode('utf-8')

print("-------------------------------------------------------------------------------")

soup = BeautifulSoup(res_encoded, "html.parser")

a_str = soup.select("a")
# """
#     <a ="/hrefitem/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%811%E5%8F%B7%E7%BA%BF" target="_blank">北京地铁1号线</a>
# """
# pattern = '\<a\s* href="(/item/\w+)"\s*target="_blank"\>(\w+)\<\/a\>'

import re
from urllib.parse import unquote
for a_s in a_str:
    pattern = r".*北京地铁.*线"
    url = a_s.attrs.get("href")
    if not url: continue
    url = unquote(url)

    print('************************************************')

    subway_line = re.findall(pattern, url)
    if not subway_line: continue
    print(subway_line)




