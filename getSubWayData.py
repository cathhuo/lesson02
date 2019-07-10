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
# print(res.encoding)
# print(res.apparent_encoding)
r = res.text
# print(requests.utils.get_encodings_from_content(r)[0])
res_encoded = r.encode("ISO-8859-1").decode(requests.utils.get_encodings_from_content(r)[0])

print("-------------------------------------------------------------------------------")
# b = r.encode("ISo-8859-1").decode(res.apparent_encoding)
# print(b)
import re
soup = BeautifulSoup(res_encoded, "html.parser")
pattern = r'<a\s+href="(.*?)"\s+target="_blank">\s+(\w+).*>'
# ss = soup.find_all(re.compile(pattern))

# print(ss)

a_str = soup.select("a")
# """
#     <a href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%811%E5%8F%B7%E7%BA%BF" target="_blank">北京地铁1号线</a>
# """
# pattern = '\<a\s* href="(/item/\w+)"\s*target="_blank"\>(\w+)\<\/a\>'
# import re
for a_s in a_str:
    sss = re.findall(pattern, a_s)
    if not sss:continue
    print(sss)


