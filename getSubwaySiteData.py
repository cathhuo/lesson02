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


import requests

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, sdch, br',
           'Accept-Language': 'zh-CN,zh;q=0.8',
           'Connection': 'keep-alive',
           'Host': 'baike.baidu.com',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}


def getHTMLText(url):
    s = requests.Session()
    res = s.get(url, allow_redirects=False, headers=headers)
    res.encoding = res.apparent_encoding
    return res.text

from bs4 import BeautifulSoup
import bs4
import re

def getSites(text,  find_tag, **kwargs):
    sites = []
    bsoup = BeautifulSoup(text, "html.parser")
    tables = bsoup.find_all("table")
    find = False
    for table in tables:
        if re.findall(u"\w+首末车时刻表",table.getText()):
            find = True
            break


    if find:
        tds = table.find_all(find_tag,  attrs=kwargs)
        for td in tds:
            if not td: continue
            # print(td)
            pattern_2 = r'(?:(末|首)班车|车站名称|备注|开往.*|.*注.*)'
            if re.findall(pattern_2, td.getText()):
                continue
            if td.getText().strip()=="":continue
            sites.append(td.getText())
    return sites





from urllib.parse import quote, unquote
href="/item/%E9%AB%98%E4%BA%95%E7%AB%99"
print(unquote(href))


def getPerSiteInfo(site):
    fetch_url = "https://baike.baidu.com/item/{item}站".format(item=site)
    if site == "磁器口":
        fetch_url = "https://baike.baidu.com/item/{item}站/2485819".format(item=site)
    print(fetch_url)
    s = requests.Session()
    res = s.get(fetch_url, headers=headers)
    res.encoding = res.apparent_encoding
    # print(res.text)

    pattern_1 = r"（下一站：(?=<a.*>(\w+)</a>(?:.|\n|\r)*?距离(\d+)米)"    #********************

    pattern = r"（下一站：(?=(\w+)）\n距离(\d+)米)"
    # aa = re.findall(pattern, res.text)
    # print(aa)
    bf = BeautifulSoup(res.text, "html.parser")

    tables = bf.find_all("table")
    aa = []
    for table in tables:
        # print(table.getText())
        aa = re.findall(pattern, table.getText())
        if aa:
            break
    if not aa:
        aa = re.findall(pattern_1, res.text)
    print(aa)


subway_lineinfo = defaultdict(list)
linesitesinfo = defaultdict(list)

if __name__ == "__main__":

    # {'/item/北京地铁昌平线', '/item/北京地铁10号线', '/item/北京地铁16号线', '/item/北京地铁8号线', '/item/北京地铁5号线', '/item/北京地铁西郊线',
    #  '/item/北京地铁4号线', '/item/北京地铁八通线', '/item/北京地铁房山线', '/item/北京地铁14号线', '/item/北京地铁1号线', '/item/北京地铁9号线',
    #  '/item/北京地铁7号线', '/item/北京地铁大兴线', '/item/北京地铁燕房线', '/item/北京地铁S1线', '/item/北京地铁13号线', '/item/北京地铁15号线',
    #  '/item/北京地铁6号线', '/item/北京地铁2号线', '/item/北京地铁亦庄线', '/item/北京地铁机场线'}
    ################1号线##########################
    html_text = getHTMLText("https://baike.baidu.com/item/北京地铁1号线")
    one_line_site_list = getSites(html_text, "td", colspan="1", rowspan="1")
    for index, site in enumerate(one_line_site_list):
        getPerSiteInfo(site)

    ################5号线###################################
    # html_text = getHTMLText("https://baike.baidu.com/item/北京地铁5号线")
    # line_site_list = getSites(html_text, "th")
    # for index, site in enumerate(line_site_list):
    #     getPerSiteInfo(site)
    ###################################/item/北京地铁昌平线####################
    # html_text = getHTMLText("https://baike.baidu.com/item/北京地铁昌平线")
    # line_site_list = getSites(html_text, "th")
    # print(line_site_list)
    # for index, site in enumerate(line_site_list):
    #     getPerSiteInfo(site)

    #百度百科南邵站信息错误









