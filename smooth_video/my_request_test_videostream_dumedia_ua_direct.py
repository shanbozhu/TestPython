#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import my_request_test_videocheck

# 获取毫秒时间戳
timestamp_ms = int(time.time() * 1000)
print(f"------------ 毫秒时间戳：{timestamp_ms}")

url = f'https://pan.baidu.com/api/wechat/videostream.m3u8?audiotoken={my_request_test_videocheck.request_audiotoken()}&isfull=1&channel=lite_rapid&time={timestamp_ms}&version=1.3.2&clienttype=291&dp-logid=35681100369575570022'
# 显式为 URL 添加双引号
safe_url = f'"{url}"'

user_agent = 'dumedia/7.84.0.7'
os.system(f'ffplay -allowed_extensions ALL -protocol_whitelist "http,file,crypto,https,tcp,tls,data" -headers "User-Agent: {user_agent}\r\n" -v debug ' + safe_url)

# 使用 VLC 播放视频，vlc太弱了，不好修复播放器内部网路请求的ua，没有ffmpeg强大。
# /Applications/VLC.app/Contents/MacOS/VLC --http-user-agent="dumedia/7.84.0.7" -vvv 'https://pan.baidu.com/api/wechat/videostream.m3u8?audiotoken=%2BG2KyPLJZmZc7WiYoHMY07oTuw5zNrnsFkgceyGs1duVexxoltit2VkO2DW7ClSt4ljQkJWYJhdmauTsGysRReLGRZGDSPQwAWKcwjrQDwz6q99BFHTgtR7%2BplUkle3wj3bTS1gi%2F%2BPWEgfdoK4MI9AWz635KVMdZo5YjNyn1Y%2FhmN%2FhWedGEScdu9KwNmJtcRGOgUTG77yaUukkIFU2p0J9%2F8K9kPc%2FJMjBLWAfRl9uGnoAajyx%2B2C3oLOG9r5P&isfull=1&channel=lite_rapid&time=1737030564793&version=1.3.2&clienttype=291&dp-logid=35681100369575570027'
# os.system('/Applications/VLC.app/Contents/MacOS/VLC --http-user-agent="dumedia/7.84.0.7" -vvv ' + safe_url)