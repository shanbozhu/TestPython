#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: myrequest.py
Author: zhushanbo
Date: 2023/4/21
Description:

https://sugar.baidu-int.com/group/matrix/report/r_1013e-962sbne9-k6rm8k?__scp__=Baidu&conditions=%7B%22dateRange%22%3A%222023-01-25%2C2023-01-31%22%7D
"""

import requests
import urllib3
import json
import random
import datetime as DT
from Models.search import Search

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class SearchTomasDataRow:
    def __init__(self, dicti):
        # self.key0 = None
        self.eventDayay = dicti["event_day"]
        self.softVersion = dicti["soft_version"]
        self.onpagetimeP80 = dicti["onpagetimeP80"]
        self.pv = dicti["pv"]

class SearchTomasData:
    def __init__(self, dicti):
        self.rows = dicti["rows"] # arr

        tmpArr = []
        for dic in self.rows:
            tomasDataRow = SearchTomasDataRow(dic)
            tmpArr.append(tomasDataRow)
        self.rows = tmpArr

class SearchTomas:
    def __init__(self, dicti):
        self.data = dicti["data"] # dict

        tomasData = SearchTomasData(self.data)
        self.data = tomasData # model

class Matrix:
    def __init__(self):
        pass

    def requestData(self):
        today = DT.date.today()
        yesterday = today - DT.timedelta(days=1)
        # 相对于昨天的6天前日期
        week_ago = yesterday - DT.timedelta(days=6)
        end_date = str(yesterday)
        start_date = str(week_ago)
        date = start_date + "," + end_date
        print("\"大字版\"查询日期:", date)

        # 请求路径,请求参数
        url = "https://sugar.baidu-int.com/api/report/r_1013e-1ntg07be-kr4bje/chart-data/c_1013e-2s170c5r-k49mmb"

        # print("请输入\"大字版\"查询日期后回车(输入格式如: 2023-04-28,2023-05-04):")
        # date = input()
        # if not date:
        #     print("未输入日期")
        #     exit(1)

        # 请求头
        header = {
            "Content-Type": "application/json",
            "Cookie": "UUAP_TRACE_TOKEN=033821185ba45b8e95a4bc89711c8cd3; jsdk-uuid=5ca8089c-e694-43b9-9e7c-94f57a5e069c; sugar-company=Baidu; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22186c5bf5f33112-024e0771d9173f4-1f525634-2007040-186c5bf5f3534f%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%7D%2C%22%24device_id%22%3A%22186c5bf5f33112-024e0771d9173f4-1f525634-2007040-186c5bf5f3534f%22%7D; Hm_lvt_822e11c38954ecab94ff3f058fe8c079=1677655634,1679540732; jsdk-user=muBLyQjMmnC1/NTAncVKqA==; _csrf=n-amXNHnbyEb0vvBIWsEeRPG; SECURE_UUAP_P_TOKEN=PT-854704388101201922-2EJ2wOKQFq-uuap; UUAP_P_TOKEN=PT-854704388101201922-2EJ2wOKQFq-uuap; bdWikiBusinessUserGuid=16QIi08Fi0; sugarbisid=s%3ALiZIkCP7h8tkPlYX0NWeRHemwCC1Qdt3.uRJ17c2bNLy2Ota56HmRZF%2B67Tyb9d39rVG5rATMowM; RT=\"z=1&dm=baidu-int.com&si=744d22b3-88f4-4be3-99e7-c06798942e10&ss=lgxmsrce&sl=s&tt=fnz&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&nu=pp706064&cl=1jx0w&ld=1jxnl\"; UUAP_S_TOKEN=ST-858081831659601921-x2Acc-uuap",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
        }

        # 请求体
        # body = {"conditions":[{"k":"dateRange","t":"dateRange","v":"2023-04-28,2023-05-04"},{"k":"event_day","t":"date","v":"2023-05-04"},{"k":"compare_event_day","t":"date","v":"2023-05-04"},{"k":"app_id","t":"select","v":"12117"},{"k":"search_page","t":"select","v":"all"},{"k":"search_source","t":"select","v":"all"},{"k":"soft_version","t":"select","v":"2.1.0.11"},{"k":"net_type","t":"select","v":"all"},{"k":"device_level","t":"select","v":"all"}],"conditionsDisplayValue":{"app_id":"手百大字版"},"resourceHash":"c_1013e-2s170c5r-k49mmb","pageHash":"r_1013e-1ntg07be-kr4bje"}
        body = {"conditions": [{"k": "dateRange", "t": "dateRange", "v": date},
                               {"k": "event_day", "t": "date", "v": end_date},
                               {"k": "compare_event_day", "t": "date", "v": end_date},
                               {"k": "app_id", "t": "select", "v": "12117"},
                               {"k": "search_page", "t": "select", "v": "all"},
                               {"k": "search_source", "t": "select", "v": "all"},
                               {"k": "soft_version", "t": "select", "v": "2.1.0.11"},
                               {"k": "net_type", "t": "select", "v": "all"},
                               {"k": "device_level", "t": "select", "v": "all"}],
                "conditionsDisplayValue": {"app_id": "手百大字版"}, "resourceHash": "c_1013e-2s170c5r-k49mmb",
                "pageHash": "r_1013e-1ntg07be-kr4bje"}

        # 请求方式
        resp = requests.post(url, json=body, headers=header, timeout=10, verify=False)

        # 解码
        content = str(resp.content, 'utf8')
        contentDict = json.loads(content)

        # print('------c = ', content)

        # print('------contentDict = ', contentDict['data']['rows'][0])


        search = SearchTomas(contentDict)
        # print("search = ", search)

        # dataCol = search.data.columns
        dataRow = search.data.rows

        # print("dataCol = ", dataCol)
        # for col in dataCol:
        #     print("col.name", col.name)
        #     print("col.id", col.id)

        # print("dataRow = ", dataRow)
        num = 0
        for row in dataRow:
            print("")
            print("日期", row.eventDayay)
            print("版本", row.softVersion)
            print("80分位", row.onpagetimeP80)
            print("PV", row.pv)
            num += row.onpagetimeP80
        # print("dataRow = ", dataRow)
        num = num / len(dataRow)
        print("")
        print("Tomas - H5搜索结果页速度7日均值", num)

if __name__ == '__main__':
    ma = Matrix()
    ma.requestData()