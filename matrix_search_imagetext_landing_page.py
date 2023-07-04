#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: myrequest.py
Author: zhushanbo
Date: 2023/4/21
Description:
"""

import requests
import urllib3
import json
import random
import datetime as dt
import matrix_search_result_page

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class SearchTomasDataRow(object):
    def __init__(self, dicti):
        # self.key0 = None
        self.event_day = dicti["event_day"]
        self.search_page = dicti["search_page"]
        self.soft_version = dicti["soft_version"]
        self.page_from_type = dicti["pageFromType"]
        self.quantile_80 = dicti["quantile_80"]
        self.pv = dicti["pv"]

class SearchTomasData(object):
    def __init__(self, dicti):
        self.rows = dicti["rows"] # arr

        tmp_arr = []
        for dic in self.rows:
            tomas_data_row = SearchTomasDataRow(dic)
            tmp_arr.append(tomas_data_row)
        self.rows = tmp_arr

class SearchTomas(object):
    def __init__(self, dicti):
        self.data = dicti["data"] # dict

        tomas_data = SearchTomasData(self.data)
        self.data = tomas_data # model

class Matrix(object):
    def __init__(self):
        pass

    def request_data(self, product, v_appid, app_id):
        today = dt.date.today()
        yesterday = today - dt.timedelta(days=1)
        # 相对于昨天的6天前日期
        week_ago = yesterday - dt.timedelta(days=6)
        end_date = str(yesterday)
        start_date = str(week_ago)
        date = start_date + "," + end_date
        print(app_id, "查询日期:", date)

        # 请求路径,请求参数
        url = "https://sugar.baidu-int.com/api/reportShare/c1ffe92cff8d2f20d8e62397bba9d84f/report/r_1013e-cdbk97i6-oq99mj/chart-data/c_1013e-2snvzla2-1j7b54"

        # print("请输入\"大字版\"查询日期后回车(输入格式如: 2023-04-28,2023-05-04):")
        # date = input()
        # if not date:
        #     print("未输入日期")
        #     exit(1)

        # 请求头
        header = {
            "Content-Type": "application/json",
            "Cookie": "SECURE_UUAP_P_TOKEN=PT-867494923821858816-cC5Wv6wHxh-uuap; SECURE_BSG_B_TOKEN=zEWgXpxO4xvG/2juMkPTf+B8C63lX09TVjyUebNzbIJ57tks6GWyFhX6E8AHb5Ye0yrkH8jsplnBAYYlyvTVzA==",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
        }

        # 请求体
        version = matrix_search_result_page.Matrix().request_version(product=product)
        body = {"conditions":[{"k":"dateRange","t":"dateRange","v":date},{"k":"event_day","t":"date","v":end_date},{"k":"compare_event_day","t":"date","v":end_date},{"k":"app_id","t":"select","v":v_appid},{"k":"os","t":"select","v":"ios"},{"k":"search_page","t":"select","v":"shybird"},{"k":"soft_version","t":"select","v":version},{"k":"pageFromType","t":"select","v":"A"},{"k":"net_type","t":"select","v":"all"}],"conditionsDisplayValue":{"app_id":app_id},"o":"performance.baidu.com","resourceHash":"c_1013e-2snvzla2-1j7b54","pageHash":"r_1013e-cdbk97i6-oq99mj"}

        # 请求方式
        resp = requests.post(url, json=body, headers=header, timeout=10, verify=False)

        # 解码
        content = str(resp.content, 'utf8')
        content_dict = json.loads(content)

        search = SearchTomas(content_dict)
        data_row = search.data.rows

        num = 0
        i = 0
        for row in data_row:
            # print("")
            # print("日期", row.event_day)
            # print("页面", row.search_page)
            # print("页面来源", row.page_from_type)
            # print("版本", row.soft_version)
            # print("80分位", row.quantile_80)
            # print("PV", row.pv)
            if product == "baiduboxlite" and (row.quantile_80 <= 0 or row.pv < 10000):
                continue
            if product == "tomas" and row.quantile_80 <= 0:
                continue
            if product == "baiduboxapp" and (row.quantile_80 <= 0 or row.pv < 10000):
                continue
            num += row.quantile_80
            i = i + 1
        # num = num / len(data_row)
        num = num / i
        # print("")
        print("百家号落地页速度7日均值", str(round(num)) + "ms", ", 最大pv版本", version)
        print("")

if __name__ == '__main__':
    ma = Matrix()
    # ma.request_data()
    ma.request_data(product="baiduboxlite", v_appid="10001", app_id="手百lite")
    ma.request_data(product="tomas", v_appid="12117", app_id="手百大字版")
    ma.request_data(product="baiduboxapp", v_appid="1", app_id="手百")
    print("==============================")