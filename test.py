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


    str = '<div class="para" label-module="para">（下一站：<a target=_blank href="/item/%E7%A6%8F%E5%AF%BF%E5%B2%AD%E7%AB%99/1827061" data-lemmaid="1827061">福寿岭站</a>）</div>' \
          '<div class="para" label-module="para">距离2606米</div>'
    pattern = r".*\（下一站：<a.*>(\w+)</a>\）.*距离(\d+)米.*"
    aa = re.findall(pattern, str)
    print(aa)





























