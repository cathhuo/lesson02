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
    a = "/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%81%E6%98%8C%E5%B9%B3%E7%BA%BF".encode("gbk")
    print(a)
































