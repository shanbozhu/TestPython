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
from Models.search import Search

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class SearchTomasDataRow(object):
    def __init__(self, dicti):
        # self.key0 = None
        self.eventDayay = dicti["event_day"]
        self.softVersion = dicti["soft_version"]
        self.onpagetimeP80 = dicti["onpagetimeP80"]
        self.pv = dicti["pv"]

class SearchTomasData(object):
    def __init__(self, dicti):
        self.rows = dicti["rows"] # arr

        tmpArr = []
        for dic in self.rows:
            tomasDataRow = SearchTomasDataRow(dic)
            tmpArr.append(tomasDataRow)
        self.rows = tmpArr

class SearchTomas(object):
    def __init__(self, dicti):
        self.data = dicti["data"] # dict

        tomasData = SearchTomasData(self.data)
        self.data = tomasData # model

class Matrix(object):
    def __init__(self):
        pass

    def requestData(self):
        # 请求路径,请求参数
        url = r"http://showx.baidu.com/api/group/156/report/47682/chart/132355?conditions=[%7B%22t%22:%22daterange%22,%22k%22:%22action_day%22,%22v%22:%222023-04-28,2023-05-04%22%7D,%7B%22t%22:%22select%22,%22k%22:%22os_name%22,%22v%22:%22iphone%22%7D,%7B%22t%22:%22select%22,%22k%22:%22app_version%22,%22v%22:%222.1.0.11%22%7D,%7B%22t%22:%22select%22,%22k%22:%22page%22,%22v%22:%22shybird%22%7D,%7B%22t%22:%22select%22,%22k%22:%22bhv_St%22,%22v%22:%220%22%7D,%7B%22t%22:%22select%22,%22k%22:%22data_desc%22,%22v%22:%22A%22%7D]"

        # print("请输入查询日期后回车(输入格式如: 2023-04-19,2023-04-25):")
        # date = input()
        # if not date:
        #     print("未输入日期")
        #     exit(1)

        # 请求头
        header = {
            "Content-Type": "application/x-www-form-urlencode",
            "Cookie": "BIDUPSID=01D4B584E70E80FFF73FDB56BCE2C9E7; PSTM=1625018538; BDUSS=N5MWc4MElZdlJ4V3VCazlOUGoxNG5ZTkpBckZHWjFQRGVNemxLdXNHVnktUDVqRVFBQUFBJCQAAAAAAAAAAAEAAAAKxaCGusPA1tTDztIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHJr12Nya9djRT; BAIDUID=1DD99F25FC67FA7D44297EB3D1179345:SL=0:NR=10:FG=1; UUAP_P_TOKEN=PT-854704388101201922-2EJ2wOKQFq-uuap; UUAP_TRACE_TOKEN=033821185ba45b8e95a4bc89711c8cd3; H_WISE_SIDS=219946_234020_114550_219565_216838_213362_214790_219943_213033_230184_204904_230288_110085_236312_243706_243885_244725_240590_245412_245599_249908_247147_250737_250302_250888_251425_251878_252215_249893_252580_253019_234295_253481_249395_253879_253427_254471_254268_254729_248124_254748_251785_254864_251133_251976_253212_255287_255298_255448_254765_255651_255879_252129_255937_255959_255909_234484_253665_251460_256062_256093_256126_253152_256083_255804_253990_256121_255659_255475_256298_256316_254833_256024_256167_229154_255179_256392_253900_256222_256441_253569_256252_250841_256721_256317_256739_256763_251971_256229_254318_256862_256587_256858_257079_257048_107316_257091_257134_254075_256301_248243_254144_257277; BDSFRCVID=_e8OJexroG0i0t3fsBK8UON2FyNbUdrTDYrEjGc3VtzSGYLVFsQ6EG0Pts1-dEub6j30ogKK0eOTHkCF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=JnkeVIKhtC-3j4I4qR7h5-I-qxbXqh5X22OZ0l8KttoAq-jNK4jcMxAA3tnwJf5r-DIqoR7mWIQthUb_QbJ6Ll_hjJbQ2frHfNv4KKJxQlCWeIJo5fcbQUKwhUJiB5O-Ban7BhOIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtnLhbC8lejuaj6bLep3K2D6aKC5bL6rJabC3_nK9XU6q2bDeQN30Jn0e5j7GaKnGBhuKs4T8-lofKl0vWq54afb2tacJXfOTylR4s4OhjxonDh83KNLLKUQtKJcBoKJO5hvvhb5O3M7OLUKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_E5bj2qRCHVC_X3f; newlogin=1; BSG_B_TOKEN=zEWgXpxO4xvG/2juMkPTf2BWNx+wEwEuBzzfOkxNKqs5m+ZsoUcjYNbPFZrp9UjssvnRFS0t/Wmum505+LshUw==; PHPSESSID=ST-860955524853948417-e9tBJ-uuap; delPer=0; PSINO=5; ZD_ENTRY=baidu; BA_HECTOR=0h81808l2100002h0184a0f11i598in1m; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; __bid_n=187ead4a91768643427d1c; RT=\"z=1&dm=baidu.com&si=1c61515c-2ba2-4fb7-9e2d-889a725146c5&ss=lha8p56e&sl=2&tt=2bt&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=c79&ul=jdv&hd=jg8\"; ___wk_scode_token=v%2FpdjGpAeuI8o8YsUatAVpatGaj7Cx5WcPTxBGmyano%3D; XSRF-TOKEN=eyJpdiI6IkpmTFpkZmJma0h2TGtIYk5RNStqTHc9PSIsInZhbHVlIjoiU2pqNVFKejBKTzJnNDBqTTlXT0NqY1Z0dlBPeVhqYURiQkpON2R4SkZpMlZzSVhLQnpIVWZGcFV5R1ltaHhkTVAxQTZSRStJRzJpb0RLWkhFRHVzZVE9PSIsIm1hYyI6ImZiZjlkODYzNzZmMjcyODllOTBkY2E4YzhkNGRhZGFmOTk1NzA2NGUxMjZiZThhYmE1MTExNTk0YmRmZWI1NzgifQ%3D%3D; showx_laravel_session=eyJpdiI6IithYklHc1FvZHhiNGh6QlFPYUx6T1E9PSIsInZhbHVlIjoiQXRlQkR5MHNIMXlVdzJCMEFOSFVYbExzSWY4V1pFaTIyYzZoV2U2RlpPcjNEbHBvME9YYWJmSXNTRTlmdzE2dlJQQW5DclZydk1MMzZXb25IQ2hicFE9PSIsIm1hYyI6Ijg0OThkYmY2MjI3ZmJlYzQwMzMxZDczZDEwZDNlOGMxM2Q1ZWIwNzUzZDk0OGFmMTdmYWU1YmQwZTA0ODZmZWIifQ%3D%3D",
            "Referer": "http://showx.baidu.com/group/searchfullflow/report/47682?conditions=%7B%22action_day%22%3A%222023-04-28%2C2023-05-04%22%2C%22os_name%22%3A%22iphone%22%2C%22app_version%22%3A%222.1.0.11%22%2C%22app_name%22%3A%22%22%7D"
        }

        # 请求体
        # body = {"conditions":[{"k":"dateRange","t":"dateRange","v":"2023-04-28,2023-05-04"},{"k":"event_day","t":"date","v":"2023-05-04"},{"k":"compare_event_day","t":"date","v":"2023-05-04"},{"k":"app_id","t":"select","v":"12117"},{"k":"search_page","t":"select","v":"all"},{"k":"search_source","t":"select","v":"all"},{"k":"soft_version","t":"select","v":"2.1.0.11"},{"k":"net_type","t":"select","v":"all"},{"k":"device_level","t":"select","v":"all"}],"conditionsDisplayValue":{"app_id":"手百大字版"},"resourceHash":"c_1013e-2s170c5r-k49mmb","pageHash":"r_1013e-1ntg07be-kr4bje"}

        # 请求方式
        resp = requests.get(url, headers=header, timeout=10, verify=False)

        # 解码
        content = str(resp.content, 'utf8')
        contentDict = json.loads(content)

        print('------c = ', content)

        resp.encoding = "utf-8"
        print('------t = ', resp.text)

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
        num = num / 7.0
        print("")
        print("Tomas - H5搜索结果页速度7日均值", num)

if __name__ == '__main__':
    ma = Matrix()
    ma.requestData()