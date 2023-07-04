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

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class SearchTomasDataRow(object):
    def __init__(self, dicti):
        # self.key0 = None
        self.event_day = dicti["event_day"]
        self.soft_version = dicti["soft_version"]
        self.onpagetimeP80 = dicti["onpagetimeP80"]
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

    def request_version(self, product):
        today = dt.date.today()
        yesterday = today - dt.timedelta(days=1)
        # 相对于昨天的6天前日期
        week_ago = yesterday - dt.timedelta(days=6)
        end_date = str(yesterday)
        start_date = str(week_ago)
        date = start_date + "," + end_date
        # print("\"大字版\"查询日期:", date)

        # 请求路径,请求参数
        url = "http://performance.baidu.com/performance/activeuser/activetrend"

        # 请求头
        header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "BIDUPSID=01D4B584E70E80FFF73FDB56BCE2C9E7; PSTM=1625018538; BDUSS=N5MWc4MElZdlJ4V3VCazlOUGoxNG5ZTkpBckZHWjFQRGVNemxLdXNHVnktUDVqRVFBQUFBJCQAAAAAAAAAAAEAAAAKxaCGusPA1tTDztIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHJr12Nya9djRT; BAIDUID=1DD99F25FC67FA7D44297EB3D1179345:SL=0:NR=10:FG=1; UUAP_P_TOKEN=PT-854704388101201922-2EJ2wOKQFq-uuap; UUAP_TRACE_TOKEN=033821185ba45b8e95a4bc89711c8cd3; H_WISE_SIDS=219946_234020_114550_219565_216838_213362_214790_219943_213033_230184_204904_230288_110085_236312_243706_243885_244725_240590_245412_245599_249908_247147_250737_250302_250888_251425_251878_252215_249893_252580_253019_234295_253481_249395_253879_253427_254471_254268_254729_248124_254748_251785_254864_251133_251976_253212_255287_255298_255448_254765_255651_255879_252129_255937_255959_255909_234484_253665_251460_256062_256093_256126_253152_256083_255804_253990_256121_255659_255475_256298_256316_254833_256024_256167_229154_255179_256392_253900_256222_256441_253569_256252_250841_256721_256317_256739_256763_251971_256229_254318_256862_256587_256858_257079_257048_107316_257091_257134_254075_256301_248243_254144_257277; newlogin=1; BSG_B_TOKEN=zEWgXpxO4xvG/2juMkPTf2BWNx+wEwEuBzzfOkxNKqs5m+ZsoUcjYNbPFZrp9UjssvnRFS0t/Wmum505+LshUw==; delPer=0; PSINO=5; ZD_ENTRY=baidu; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; __bid_n=187ead4a91768643427d1c; jsdk-user=muBLyQjMmnC1/NTAncVKqA==; BKMASKSID=25561beb28b48a58c15af0efbbc664f8; jsdk-uuid=8dd2d297-dd3d-477e-b7f6-07986b2f9517; ET_WHITELIST=etwhitelistintwodays; BDRCVFR[Gm3feW4UKgs]=I67x6TjHwwYf0; BA_HECTOR=0l0ga4ak8hah2l2k252l8k5q1i5jcp11m; BCLID=7758398180450468072; BDSFRCVID=bS0OJexroG0ikDOfSECxwxAbV9NbUdrTDYrEjGc3VtzSGYLVFsQ6EG0Pts1-dEub6j30ogKK0eOTHkCF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=JnkeVIKhtC-3j4I4qR7h5-I-qxbXqh5X22OZ0l8KttoAq-jNK4jcMxAA3tnwJf5r-DIqoR7mWIQthUb_QbJ6Ll_hjJbQ2frHfNv4KKJxQlCWeIJo5fcbQUKwhUJiB5O-Ban7BhOIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtnLhbC8lejuaj6bLep3K2D6aKC5bL6rJabC3_nK9XU6q2bDeQN30Jn0e5j7GaKnGBhuKs4T8-lofKl0vWq54afb2tacJXfOTylR4s4OhjxonDh83KNLLKUQtKJcBoKJO5hvvhb5O3M7OLUKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_EJ5K8tb-tVCLQ24OEfbKk-4QEbbQH-UnLq5vr3gOZ0l8Ktt5vMqACK4jo0UD_3tnwJfKHQJ6d0bOmWIQHDpjjWMntjxFQ5t6M0xc3BKT4KKJxW-PWeIJo5fcajU4khUJiB5O-Ban7BhOIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtnLhbC8lejuaj6bLeU5eetjK2CntsJOOaCvZHtbOy4oWK441DMrW0URhL2TmXP3y0Ro4bqrP3tOK3M04K4o9-hvT-54e2p3FBUQPqUDCQft20b0yDecb0RQaJDLeon7jWhk2eq72y-RTQlRX5q79atTMfNTJ-qcH0KQpsIJM5-DWbT8IjHCeJ6F8tRFfoCvMKRu_HRjYbb__-P4DeU5gJURZ56bHWh0M2RvU8nQbQfbW5nkF-RD8WtjP5TrnKUT-3RcnHIOK5b66QpFT34jeQ6543bRTLP8hHRbpfJ_CM6-2hP-UyN3-Wh37227lMKoaMp78jR093JO4y4Ldj4oxJpOJ5JbMopCafJOKHICwj5_a3j; Hm_lvt_0ab5c89c399def06d4442b16d361f1c1=1681190906,1682303695,1683600769; PHPSESSID=ST-862647409276420097-Q2S4R-uuap; BDRCVFR[S4-dAuiWMmn]=I67x6TjHwwYf0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lpvt_0ab5c89c399def06d4442b16d361f1c1=1683631068; RT=\"z=1&dm=baidu.com&si=1c61515c-2ba2-4fb7-9e2d-889a725146c5&ss=lhg6fmny&sl=6&tt=24c&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=1fhf&nu=29do3j86&cl=1eop\""
        }

        # 请求参数
        end_time = yesterday.strftime("%Y%m%d")
        params = {"app_version": "", "channel": "all", "end_time": end_time, "groupby": "event_day,app_version",
                  "hms_flag": "3", "orderby": "event_day,pv", "os_name": "ios", "proc_bit": "all", "product": product,
                  "sort": "DESC", "start_time": end_time}
        # 请求方式
        resp = requests.get(url, params=params, headers=header, timeout=10, verify=False)

        # 解码
        content = str(resp.content, 'utf8')
        # print(content)
        json_dict = json.loads(content)
        return json_dict["data"]["list"][0]["app_version"]


    def request_data(self, product, v_appid, app_id):
        # version = self.request_version()
        # print(version)

        today = dt.date.today()
        yesterday = today - dt.timedelta(days=1)
        # 相对于昨天的6天前日期
        week_ago = yesterday - dt.timedelta(days=6)
        end_date = str(yesterday)
        start_date = str(week_ago)
        date = start_date + "," + end_date
        print(app_id, "查询日期:", date)

        # 请求路径,请求参数
        url = "https://sugar.baidu-int.com/api/reportShare/325ba1e2445bc3cc51ac10d906d13dde/report/r_1013e-1ntg07be-kr4bje/chart-data/c_1013e-2s170c5r-k49mmb"

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
        version = self.request_version(product=product)
        body = {"conditions":[{"k":"dateRange","t":"dateRange","v":date},{"k":"event_day","t":"date","v":end_date},{"k":"compare_event_day","t":"date","v":end_date},{"k":"app_id","t":"select","v":v_appid},{"k":"search_page","t":"select","v":"all"},{"k":"search_source","t":"select","v":"all"},{"k":"soft_version","t":"select","v":version},{"k":"net_type","t":"select","v":"all"},{"k":"device_level","t":"select","v":"all"}],"conditionsDisplayValue":{"app_id":app_id},"o":"performance.baidu.com","resourceHash":"c_1013e-2s170c5r-k49mmb","pageHash":"r_1013e-1ntg07be-kr4bje"}

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
            # print("版本", row.soft_version)
            # print("80分位", row.onpagetimeP80)
            # print("PV", row.pv)
            if row.pv < 10000:
                continue
            num += row.onpagetimeP80
            i = i + 1
        # num = num / len(data_row)
        num = num / i
        # print("")
        #print("H5结果页速度7日均值", round(num, 2), ", 最大pv版本", version)
        print("H5结果页速度7日均值", str(round(num)) + "ms", ", 最大pv版本", version)
        print("")

if __name__ == '__main__':
    ma = Matrix()
    ma.request_data(product="baiduboxlite", v_appid="10001", app_id="手百lite")
    ma.request_data(product="tomas", v_appid="12117", app_id="手百大字版")
    ma.request_data(product="baiduboxapp", v_appid="1", app_id="手百")
    print("==============================")