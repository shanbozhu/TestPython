#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: matrix_search_h5_landing_page.py
Author: zhushanbo
Date: 2023/4/21
Description:
"""

import json
import datetime as dt
import matrix_search_result_page

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

product_baiduboxlite = "baiduboxlite"
product_tomas = "tomas"
product_baiduboxapp = "baiduboxapp"

class SearchTomasDataRow(object):
    def __init__(self, dicti):
        # self.key0 = None
        self.event_day = dicti["event_day"]
        self.search_page = dicti["search_page"]
        self.soft_version = dicti["soft_version"]
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

        tomasData = SearchTomasData(self.data)
        self.data = tomasData # model

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
        url = "https://sugar.baidu-int.com/api/reportShare/3a6c2f8b21f8a45927ecb1d95a1af23e/report/r_1013e-8ad82r3p-o8ll5x/chart-data/c_1013e-c254mx61-kepbl7"

        # 请求头
        header = {
            "Content-Type": "application/json",
            "Cookie": "SECURE_UUAP_P_TOKEN=PT-867494923821858816-cC5Wv6wHxh-uuap; SECURE_BSG_B_TOKEN=zEWgXpxO4xvG/2juMkPTf+B8C63lX09TVjyUebNzbIJ57tks6GWyFhX6E8AHb5Ye0yrkH8jsplnBAYYlyvTVzA==",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
        }
        # 请求体
        version = matrix_search_result_page.Matrix().request_version(product=product)
        body = {"conditions":[{"k":"dateRange","t":"dateRange","v":date},{"k":"event_day","t":"date","v":end_date},{"k":"compare_event_day","t":"date","v":end_date},{"k":"app_id","t":"select","v":v_appid},{"k":"search_page","t":"select","v":"all"},{"k":"soft_version","t":"select","v":version},{"k":"net_type","t":"select","v":"all"},{"k":"device_level","t":"select","v":"all"},{"k":"pd","t":"select","v":"all"},{"k":"atn","t":"select","v":"all"},{"k":"status","t":"select","v":"all"}],"conditionsDisplayValue":{"app_id":app_id},"o":"performance.baidu.com","resourceHash":"c_1013e-c254mx61-kepbl7","pageHash":"r_1013e-8ad82r3p-o8ll5x"}
        # 请求方式
        resp = requests.post(url, json=body, headers=header, timeout=10, verify=False)

        # 解码
        content = str(resp.content, 'utf-8')
        content_dict = json.loads(content)

        search = SearchTomas(content_dict)
        data_row = search.data.rows

        num = 0
        i = 0
        for row in data_row:
            # print("")
            # print("日期", row.event_day)
            # print("页面", row.search_page)
            # print("版本", row.soft_version)
            # print("80分位", row.quantile_80)
            # print("PV", row.pv)
            if product == product_baiduboxlite and (row.quantile_80 <= 0 or row.pv < 10000):
                continue
            if product == "tomas" and (row.quantile_80 <= 0 or row.pv < 4000):
                continue
            if product == "baiduboxapp" and (row.quantile_80 <= 0 or row.pv < 10000):
                continue
            num += row.quantile_80
            i = i + 1
        # num = num / len(data_row)
        num = num / i
        print("H5落地页速度7日平均值", str(round(num)) + "ms", ", 最大pv版本", version)
        print("")

if __name__ == '__main__':
    ma = Matrix()
    ma.request_data(product=product_baiduboxlite, v_appid="10001", app_id="手百lite")
    ma.request_data(product=product_tomas, v_appid="12117", app_id="手百大字版")
    ma.request_data(product=product_baiduboxapp, v_appid="1", app_id="手百")
    print("==============================")