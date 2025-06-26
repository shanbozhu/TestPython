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
import os
import pyperclip
import segno
import my_request_test_videocheck

# 取消InsecureRequestWarning警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    'Host': 'pan.baidu.com',
    'Cookie': 'STOKEN=274bbadb8b283ac1f147a3324b0a80672bc624f708f3f37df65d2b2735b5a09b;BDCLND=;BAIDUID=7DFD709E625646F443E5C3BBBD3C46BC:FG=1;ndut_fmt=0AE12AD5E4D5E74972E39A2DF35B3797B21396A042BDE14359C829E20366E6E5;BDUSS=FdoVFlMTlhjVWRyVm1hS25RbWVZbDZKSlFrS05IdnRuYlBvd3lGTTk3ZVRPVzFtSVFBQUFBJCQAAAAAAAAAAAEAAAAKxaCGusPA1tTDztIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJOsRWaTrEVmb;',
    'devuid': 'NA',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Swan-Token': 'e03fef035919bfe994ecc0846b4a8a2f',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'X-Swan-Ts': '1736319281800',
    'X-Bd-Traceid': 'd0270be70c044dca9e8306e05bd1c675',
    'Accept': '*/*',
    'X-TurboNet-Info': '3.0.2051.348',
    'X-From-H3-TRNet': 'true',
    'Referer': 'https://smartapps.cn/OyIvf6LYVhKkbIHS1USP7xnSKYxc36SH/2.2.111/page-frame.html',
    'Accept-Language': 'zh-CN,zh',
}

# 获取毫秒时间戳
timestamp_ms = int(time.time() * 1000)
print(f"------------ 毫秒时间戳：{timestamp_ms}")

params = [
    ('isfull', '1'),
    ('channel', 'lite_rapid'),
    ('clienttype', '291'),
    ('time', f'{timestamp_ms}'),
    ('version', '1.3.2'),
    ('dp-logid', '35681100369575570027'),
]

# params会在内部自动进行url编码
# params = {
#     'isfull': '1',
#     'channel': 'netdisk_bdmin',
#     'time': f'{timestamp_ms}',
#     'version': '1.3.2',
#     'clienttype': '32',
#     'dp-logid': '35681100369575570027',
# }

response = requests.get('https://pan.baidu.com/api/wechat/videostream.m3u8?audiotoken=' + my_request_test_videocheck.request_audiotoken(), params=params, headers=headers)

print("------------ r.text =", response.text)
print("------------ r.url =", response.url)

# 生成二维码
qr = segno.make(response.url)
# 或保存为矢量格式（SVG 更适合打印或大尺寸展示）
qr.save("video_stream_qrcode.svg")

# 要拷贝到剪贴板的字符串
text = response.text
# 拷贝到剪贴板
pyperclip.copy(text)
# 从剪贴板获取内容（测试用）
pasted_text = pyperclip.paste()
print(f"------------ Pasted from clipboard: {pasted_text}")

# 显式为 URL 添加双引号
safe_url = f'"{response.url}"'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
os.system(f'ffplay -protocol_whitelist "http,file,crypto,https,tcp,tls,data" -headers "User-Agent: {user_agent}\r\n" -v debug ' + safe_url)

# -H 'Accept-Encoding: gzip, deflate' 输出的curl命令需要去掉这项，否则会提示"在终端输出二进制打乱终端显示"
# -H 'Content-Length: 13530' 输出的curl命令需要去掉这项
# curl_command = curlify.to_curl(response.request)
# print("------------ curl_command =", curl_command)
# print("------------ curl_command =", urllib.parse.unquote(curl_command))