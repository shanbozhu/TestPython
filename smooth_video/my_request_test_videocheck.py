#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
参考文档:
https://blog.csdn.net/wanghao3616/article/details/127860811
https://stackoverflow.com/questions/44964529/how-to-send-urlencoded-parameters-in-post-request-in-python

临时更换安装源:
pip3 install requests -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

File: my_request.py
Author: zhushanbo
Date: 2023/4/21
Description: 通用请求
"""

import requests
import urllib3
import json
import random
import curlify
import urllib.parse
import time

# 取消InsecureRequestWarning警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def request_audiotoken():
    headers = {
        'Host': 'pan.baidu.com',
        'Cookie': 'STOKEN=274bbadb8b283ac1f147a3324b0a80672bc624f708f3f37df65d2b2735b5a09b;BDCLND=;BAIDUID=7DFD709E625646F443E5C3BBBD3C46BC:FG=1;ndut_fmt=0AE12AD5E4D5E74972E39A2DF35B3797B21396A042BDE14359C829E20366E6E5;BDUSS=FdoVFlMTlhjVWRyVm1hS25RbWVZbDZKSlFrS05IdnRuYlBvd3lGTTk3ZVRPVzFtSVFBQUFBJCQAAAAAAAAAAAEAAAAKxaCGusPA1tTDztIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJOsRWaTrEVmb;',
        'devuid': 'NA',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Swan-Token': '7c8e61f5c14e6724df96ed7c4dafee78',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16C104 swan/3.16.0 swan-bdlite/6.42.0.3 bdlite/6.42.0.3 (Baidu; P2 12.1.2) isFMPArrived:0',
        'X-Swan-Ts': '1736319280496',
        'X-Bd-Traceid': '5ab06d93fe1b400d811e36303ac4eff4',
        'Accept': '*/*',
        'X-TurboNet-Info': '3.0.2051.348',
        'X-From-H3-TRNet': 'true',
        'Referer': 'https://smartapps.cn/OyIvf6LYVhKkbIHS1USP7xnSKYxc36SH/2.2.111/page-frame.html',
        'Accept-Language': 'zh-CN,zh',
    }

    # 获取毫秒时间戳
    timestamp_ms = int(time.time() * 1000)
    print(f"------------ 毫秒时间戳：{timestamp_ms}")

    params = {
        'path': '/来自：流畅播视频/正在播放国产剧《欢乐颂》第01集-免费在线观看全集无广告完整版-飞飞影视(1).mp4',
        'type': 'M3U8_AUTO_1080',
        'fromuk': '',
        'channel': 'lite_rapid',
        'clienttype': '291',
        'time': f'{timestamp_ms}',
        'version': '1.3.2',
        'dp-logid': '35681100369575570019',
    }

    response = requests.get('https://pan.baidu.com/api/wechat/videocheck', params=params, headers=headers)

    print("------------ r.url =", response.url)
    print("------------ r.text =", response.text)

    # curl_command = curlify.to_curl(response.request)
    # print("------------ curl_command =", curl_command)
    # print("------------ curl_command =", urllib.parse.unquote(curl_command))

    return json.loads(response.text)['audiotoken']

if __name__ == '__main__':
    request_audiotoken()
