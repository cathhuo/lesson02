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
    a = defaultdict(list)
    a['aa'].append(22)
    print(a)





























