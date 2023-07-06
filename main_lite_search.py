#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: main_lite_search.py
Author: zhushanbo
Date: 2023/4/21
Description:
极速版 - 搜索结果页\h5落地页\百家号落地页上屏耗时
"""

import json
import datetime as dt
from models.search import Search

import os # os为内置模块，是一定存在的
count = 3 # 最大检测次数，即第一次检测不存在则安装，若安装失败，则再来一次
while count:
    try:
        import requests # 三方模块
        import urllib3
        # print ('模块已安装')
        break
    except:
        print ('模块未安装，现在开始安装')
        os.system('pip3 install requests -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com')
        os.system('pip3 install urllib3 -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com')
        count -= 1
        continue

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Matrix(object):
    def __init__(self):
        pass

    def request_data(self):
        today = dt.date.today()
        yesterday = today - dt.timedelta(days=1)
        # 相对于昨天的6天前日期
        week_ago = yesterday - dt.timedelta(days=6)
        end_date = str(yesterday)
        start_date = str(week_ago)
        date = start_date + "," + end_date
        print("\"极速版和主板\"查询日期:", date)

        # 请求路径,请求参数
        url = "https://sugar.baidu-int.com/api/report/r_1013e-962sbne9-k6rm8k/chart-data/c_1013e-3x5owwj5-1d246m"
        # 请求头
        header = {
            "Content-Type": "application/json",
            "Cookie": "UUAP_TRACE_TOKEN=033821185ba45b8e95a4bc89711c8cd3; jsdk-uuid=5ca8089c-e694-43b9-9e7c-94f57a5e069c; sugar-company=Baidu; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22186c5bf5f33112-024e0771d9173f4-1f525634-2007040-186c5bf5f3534f%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%7D%2C%22%24device_id%22%3A%22186c5bf5f33112-024e0771d9173f4-1f525634-2007040-186c5bf5f3534f%22%7D; Hm_lvt_822e11c38954ecab94ff3f058fe8c079=1677655634,1679540732; jsdk-user=muBLyQjMmnC1/NTAncVKqA==; _csrf=n-amXNHnbyEb0vvBIWsEeRPG; SECURE_UUAP_P_TOKEN=PT-854704388101201922-2EJ2wOKQFq-uuap; UUAP_P_TOKEN=PT-854704388101201922-2EJ2wOKQFq-uuap; bdWikiBusinessUserGuid=16QIi08Fi0; sugarbisid=s%3ALiZIkCP7h8tkPlYX0NWeRHemwCC1Qdt3.uRJ17c2bNLy2Ota56HmRZF%2B67Tyb9d39rVG5rATMowM; RT=\"z=1&dm=baidu-int.com&si=744d22b3-88f4-4be3-99e7-c06798942e10&ss=lgxmsrce&sl=s&tt=fnz&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&nu=pp706064&cl=1jx0w&ld=1jxnl\"; UUAP_S_TOKEN=ST-858081831659601921-x2Acc-uuap",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
        }
        # 请求体
        body = {"conditions": [{"k": "dateRange", "t": "dateRange", "v": date}],
                "resourceHash": "c_1013e-3x5owwj5-1d246m", "pageHash": "r_1013e-962sbne9-k6rm8k"}
        # 请求方式
        resp = requests.post(url, json=body, headers=header, timeout=10, verify=False)

        # 解码
        content = str(resp.content, 'utf-8')
        content_dict = json.loads(content)

        search = Search(content_dict)
        data_row = search.data.rows

        for row in data_row:
            if row.name == "对比":
                continue
            if row.name == "版本-Lite" or row.name == "版本-主线":
                print("")
                print(row.name, "iOS")
                print("版本", row.key0.split('/')[1])
                continue
            print("")
            print(row.name, "iOS")
            print("搜索结果页", row.key0.split('/')[1])
            print("搜索H5落地页", row.key1.split('/')[1])
            print("搜索NA落地页（百家号）", row.key2.split('/')[1])
        print("==============================")

if __name__ == '__main__':
    ma = Matrix()
    ma.request_data()