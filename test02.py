# -*- encoding:utf-8 -*-

line_url_list = ["https://baike.baidu.com/item/北京地铁1号线",
"https://baike.baidu.com/item/北京地铁2号线",
"https://baike.baidu.com/item/北京地铁4号线",
"https://baike.baidu.com/item/北京地铁5号线",
"https://baike.baidu.com/item/北京地铁6号线",
"https://baike.baidu.com/item/北京地铁7号线",
"https://baike.baidu.com/item/北京地铁8号线",
"https://baike.baidu.com/item/北京地铁9号线",
"https://baike.baidu.com/item/北京地铁10号线",
"https://baike.baidu.com/item/北京地铁13号线",
"https://baike.baidu.com/item/北京地铁14号线",
"https://baike.baidu.com/item/北京地铁15号线",
"https://baike.baidu.com/item/北京地铁16号线",
"https://baike.baidu.com/item/北京地铁昌平线",
"https://baike.baidu.com/item/北京地铁房山线",
"https://baike.baidu.com/item/北京地铁亦庄线",
"https://baike.baidu.com/item/北京地铁燕房线",
"https://baike.baidu.com/item/北京地铁机场线"]

from collections import defaultdict

subway_lineinfo = defaultdict(list)
linesitesinfo = defaultdict(list)

import requests

def getHTMLText(url):
    s = requests.Session()
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate, sdch, br',
               'Accept-Language': 'zh-CN,zh;q=0.8',
               'Connection': 'keep-alive',
               'Host': 'baike.baidu.com',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

    res = s.get(url, allow_redirects=False, headers=headers)
    res.encoding = res.apparent_encoding
    return res.text

from bs4 import BeautifulSoup
import bs4
import re

def getSites(text, table_class, find_tag, **kwargs):
    sites = []
    bsoup = BeautifulSoup(text, "html.parser")
    table = bsoup.find("table", class_=table_class)

    tds = table.find_all(find_tag,  attrs=kwargs)
    for td in tds:
        if not td: continue
        # print(td)
        sites.append(td.getText())
    return sites



# print(getHTMLText("https://baike.baidu.com/item/北京地铁1号线"))

from urllib.parse import quote, unquote
href="/item/%E9%AB%98%E4%BA%95%E7%AB%99"
print(unquote(href))






if __name__ == "__main__":

    html_text = getHTMLText("https://baike.baidu.com/item/北京地铁1号线")
    print(getSites(html_text, "one", "td", colspan="1", rowspan="1"))



