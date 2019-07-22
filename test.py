# -*- encoding:utf-8 -*-

import requests

import re
import matplotlib
from collections import defaultdict

if __name__ == "__main__":

    coordination_source = """
        {name:'兰州', geoCoord:[103.73, 36.03]},
        {name:'成都', geoCoord:[104.06, 30.67]}
    """

    # pattern = re.compile(r"name:'(\w+)',\s+geoCoord:\[(\d+.\d+),\s(\d+.\d+)\]")
    # print(re.findall(pattern, coordination_source))
    # a = defaultdict(list)
    # a['aa'].append(22)
    # print(a)
    # pattern = r".*北京地铁.*线"
    # a = re.findall(pattern, "/北京item/地铁1号线")
    # print(a)



    str = '（下一站：<a target=_blank href="/item/%E7%A6%8F%E5%AF%BF%E5%B2%AD%E7%AB%99/1827061" data-lemmaid="1827061">福寿岭站</a>）</div>\r\n<div class="para" label-module="para">（预留车站，暂未启用）</div>\r\n</td><td align="center" valign="middle" colspan="3" rowspan="3"><div class="para" label-module="para"><a target=_blank href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%811%E5%8F%B7%E7%BA%BF/7646800" data-lemmaid="7646800">北京地铁1号线</a></div>\r\n</td><td align="center" valign="middle" colspan="3" rowspan="3"><div class="para" label-module="para">开往<a target=_blank href="/item/%E5%9B%9B%E6%83%A0%E4%B8%9C%E7%AB%99">四惠东站</a></div>\r\n<div class="para" label-module="para">（下一站：<a target=_blank href="/item/%E5%8F%A4%E5%9F%8E%E7%AB%99/2662893" data-lemmaid="2662893">古城站</a>）</div>\r\n<div class="para" label-module="para">距离2606米'

    # pattern = r".*?（下一站：<a.*?>(\w+)</a>）.*?(距离(\d+)米|(（\w+）)).*"
    # pattern = r".*（下一站：<a.*?>(\w+)</a>）.*(距离(\d+)米).*"
    # pattern = r".*(（下一站：.*）(.|\n)*(距离(\d+)米)).*"
    pattern = r"(.|\r\n)*（下一站：<a.*>(\w+)</a>）</div>(.|\r\n)*距离(\d+)米(.|\r\n)*"
    aa = re.findall(pattern, str)
    print(aa)
    # matches = re.finditer(pattern, str)
    # results = [match.group(1) for match in matches]
    # print(results)





























