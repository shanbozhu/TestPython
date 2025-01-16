#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
参考文档：
https://blog.csdn.net/wanghao3616/article/details/127860811
https://stackoverflow.com/questions/44964529/how-to-send-urlencoded-parameters-in-post-request-in-python

临时更换安装源：
pip3 install requests -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

File: my_request_x-www-form-urlencoded.py
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

# 取消InsecureRequestWarning警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 请求路径、请求参数
url = "https://mbd.baidu.com/icomment/v1/comment/rlist?appname=baiduboxlite&cfrom=1005640h&ds_lv=4&ds_stc=0.7740&from=1005640h&fv=13.30.0.10&matrixstyle=0&mps=154326807&mpv=1&network=1_0&sid=34836_3-8319_19556-56196_2-8313_19529-56785_2-56115_2-34064_2-35158_1-5760_9013-34999_8-35148_1-35262_2-107862_3-32205_2-56359_4-55371_1-35215_2-5280_7494-56512_4-9619_2-8321_19560-33923_6-9451_2-9618_2-8083_18570-5644_8666-56430_2-35223_1-5153_7043-34731_2-35072_2-56076_3&st=0&ua=828_1792_iphone_6.1.0.3_0&uid=45D34CA04432AE7FB8F806F7483DB2F06B58F8588FMMDBHJSRH&zid=Nz1vfc_o7oN3ci-TIwM1lwW9-GqQg2jHJyLNp9nVbRIFAsQJxD06HMqQTcbu6Y9x0StTFnWsNpHkiJhkxPtHb6Q&sdkversion=1.1.2"

# 请求参数。可以单独传，最终会附加在url后面
# params里的参数值会默认进行url编码，即使已经url编码过
params = {
    "xxx": "12345你好/世界"
}

# cookie可以单独传，request库会在内部自动将其放到headers里，不用手动放到headers里
cookies = {
    'BAIDUCUID': 'gaS98giPH8_fu28xli2yu0PjHt_RaS8V_O2Ca0aMH8_ui2tY0O2NtYi2QP0z8WPCbWHmA',
    'MBD_AT': '1611037261',
    '__yjs_duid': '1_16ef112911fea7f8f85861dd4cd865d61611037267886',
    'BDUSS': 'o4dG9PbFUyaHJ6YmlJUXFUV1htNlNnQVBvWVV1TkJZcXlocWYwRlEwWVd6VmhmSVFBQUFBJCQAAAAAAAAAAAEAAAAKxaCGusPA1tTDztIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABZAMV8WQDFfU0',
    'BAIDUID': '5C8D78D64E6848E8E66D846DD5DFFE60:FG=1',
    'fnizebra_b': 'P0lhrcN53vdMUS%2F6i6Jqke1DYnu1Bk7BKyn22Lr1OiSJcdkcuIE5QRexh80u3Q0CHAwYzANIhkgioe4D%2FK5Sa7%2BwWEa0CsRrSUcPM4pO%2FvjxvQAdf9qVcn5mRMjr6xQqsgdHPQGIyAFdR6CUMsb5axYXkySjX0%2BtBF7OsuEKruY%3D',
    'SP_FW_VER': '3.240.16',
    'iadlist': '49153',
    'fontsize': '1.10',
    'H_WISE_SIDS': '107314_110086_114551_127969_144966_154214_156286_156306_161278_162187_162203_162898_163115_163274_163390_163581_163808_163933_164043_164110_164164_164214_164216_164296_164692_164865_164880_164941_164992_165071_165135_165144_165327_165345_165591_165737_166055_166147_166180_166184_166255_166597_166599_166825_166987_167303_167388_167537_167571_167744_167771_167781_167926_167980_168034_168073_168215_168402',
    'WISE_HIS_PM': '1',
    'BCLID': '9140690592728723096',
    'BDSFRCVID': 'JYKOJeCinR3Chr6eBYNMUON2YgKX8jRTH60oY2ODlwB_I7JoXeN5EG0P8x8g0KubrAb4ogKK0eOTHkCF_2uxOjjg8UtVJeC6EG0Ptf8g0f5',
    'H_BDCLCKID_SF': 'tbCD_KK5JKD3HtJxKITHKb8jbeT22-usWH5i2hcH0bT_VCOJMbK-bfD4X4cPWMCHyCvihIn_Lfb1MCJvWj5cQ-AWLRnAtMTyyITw_l5TtUtWJKnTDMRh-RDF-GOyKMnitIT9-pno0hQrh459XP68bTkA5bjZKxtq3mkjbPbDfn02eCKu-n5jHjoWjajP',
    'ST': '0',
    'BAIDULOC': '13538033.981942_3634594.7065378_1000_289_1611659203826',
    'ab_sr': '1.0.0_MDg2OTViODUwYzI5ZDIwYmRjMmYyNjRhMmQyMWU0Y2JlMTRlOThhNDc5MzUyN2NjYjkzYzE4ZmYzYzQ1YjE3NmIwN2FiNTcxMDZjNjMwZTNiYTExMzhiNzQwMmY5ZmY3',
    'x-logic-no': '2',
}

# 请求头
headers = {
    "Content-Type": "application/x-www-form-urlencoded", # 内容类型x-www-form-urlencoded
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16C104 SP-engine/2.24.0 matrixstyle/0 info baiduboxapp/5.1.1.10 (Baidu; P2 12.1.2)",
    # "Cookie": "BAIDUCUID=gaS98giPH8_fu28xli2yu0PjHt_RaS8V_O2Ca0aMH8_ui2tY0O2NtYi2QP0z8WPCbWHmA; MBD_AT=1611037261; __yjs_duid=1_16ef112911fea7f8f85861dd4cd865d61611037267886; BDUSS=o4dG9PbFUyaHJ6YmlJUXFUV1htNlNnQVBvWVV1TkJZcXlocWYwRlEwWVd6VmhmSVFBQUFBJCQAAAAAAAAAAAEAAAAKxaCGusPA1tTDztIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABZAMV8WQDFfU0; BAIDUID=5C8D78D64E6848E8E66D846DD5DFFE60:FG=1; fnizebra_b=P0lhrcN53vdMUS%2F6i6Jqke1DYnu1Bk7BKyn22Lr1OiSJcdkcuIE5QRexh80u3Q0CHAwYzANIhkgioe4D%2FK5Sa7%2BwWEa0CsRrSUcPM4pO%2FvjxvQAdf9qVcn5mRMjr6xQqsgdHPQGIyAFdR6CUMsb5axYXkySjX0%2BtBF7OsuEKruY%3D; SP_FW_VER=3.240.16; iadlist=49153; fontsize=1.10; H_WISE_SIDS=107314_110086_114551_127969_144966_154214_156286_156306_161278_162187_162203_162898_163115_163274_163390_163581_163808_163933_164043_164110_164164_164214_164216_164296_164692_164865_164880_164941_164992_165071_165135_165144_165327_165345_165591_165737_166055_166147_166180_166184_166255_166597_166599_166825_166987_167303_167388_167537_167571_167744_167771_167781_167926_167980_168034_168073_168215_168402; WISE_HIS_PM=1; BCLID=9140690592728723096; BDSFRCVID=JYKOJeCinR3Chr6eBYNMUON2YgKX8jRTH60oY2ODlwB_I7JoXeN5EG0P8x8g0KubrAb4ogKK0eOTHkCF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=tbCD_KK5JKD3HtJxKITHKb8jbeT22-usWH5i2hcH0bT_VCOJMbK-bfD4X4cPWMCHyCvihIn_Lfb1MCJvWj5cQ-AWLRnAtMTyyITw_l5TtUtWJKnTDMRh-RDF-GOyKMnitIT9-pno0hQrh459XP68bTkA5bjZKxtq3mkjbPbDfn02eCKu-n5jHjoWjajP; ST=0; BAIDULOC=13538033.981942_3634594.7065378_1000_289_1611659203826; ab_sr=1.0.0_MDg2OTViODUwYzI5ZDIwYmRjMmYyNjRhMmQyMWU0Y2JlMTRlOThhNDc5MzUyN2NjYjkzYzE4ZmYzYzQ1YjE3NmIwN2FiNTcxMDZjNjMwZTNiYTExMzhiNzQwMmY5ZmY3; x-logic-no=2"
}

# 请求体
ext = {
    "sortTime": "12345"
}
body = {
    "topic_id": "1000000056224844",
    "source": "channel_video_landing",
    "start": 0,
    "source_type": "baidumedia",
    "reply_id": "1122518916369402407",
    "request_id": "38383331323433303437373531393733353736",

    "extdata[origin]": "feed",
    "extdata[client_logid]": "E18940390F8EC74785570C5BE86236F8",
    "extdata[s_session]": "",

    "key": "1762683039161549402",
    "num": 20,
    "ext": json.dumps(ext),  # json字典转json字符串
    "msg_key": str(random.randint(0, 99999999999)),  # 随机值
}

# 请求方式
r = requests.post(
    url,
    params=params,
    cookies=cookies,
    headers=headers,
    data=body,
    timeout=2,
    verify=False
)

# utf-8解码
json_str = str(r.content, 'utf-8')
print("json_str =", json_str)

# r.encoding = 'utf-8'
print("r.text =", r.text)
print("r.url =", r.url)

# json转换
json_dict = json.loads(json_str)
print("loads for json_dict =", json_dict)
json_str = json.dumps(json_dict)
print("dumps for json_str =", json_str)

# to curl
# -H 'Accept-Encoding: gzip, deflate' 输出的curl命令需要去掉这项，否则会提示"在终端输出二进制打乱终端显示"
# -H 'Content-Length: 13530' 输出的curl命令需要去掉这项
curl_command = curlify.to_curl(r.request)
print("curl_command =", curl_command)
print("curl_command =", urllib.parse.unquote(curl_command)) # url解码
