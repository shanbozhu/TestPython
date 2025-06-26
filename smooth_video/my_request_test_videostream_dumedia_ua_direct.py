#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import my_request_test_videocheck

# 获取毫秒时间戳
timestamp_ms = int(time.time() * 1000)
print(f"------------ 毫秒时间戳：{timestamp_ms}")

url = f'https://pan.baidu.com/api/wechat/videostream.m3u8?audiotoken={my_request_test_videocheck.request_audiotoken()}&isfull=1&channel=lite_rapid&time={timestamp_ms}&clienttype=291'
# 显式为 URL 添加双引号
safe_url = f'"{url}"'

user_agent = 'dumedia/7.84.0.7'
cookie = 'bd_logap_verify=1; BAIDUID=664A00F7C4834022CB3E7555003F820F:FG=1; BAIDUID_BFESS=664A00F7C4834022CB3E7555003F820F:FG=1; MBD_AT=1750402097; BDUSS=FdoVFlMTlhjVWRyVm1hS25RbWVZbDZKSlFrS05IdnRuYlBvd3lGTTk3ZVRPVzFtSVFBQUFBJCQAAAAAAAAAAAEAAAAKxaCGusPA1tTDztIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJOsRWaTrEVmb; BDUSS_BFESS=FdoVFlMTlhjVWRyVm1hS25RbWVZbDZKSlFrS05IdnRuYlBvd3lGTTk3ZVRPVzFtSVFBQUFBJCQAAAAAAAAAAAEAAAAKxaCGusPA1tTDztIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJOsRWaTrEVmb; BAIDUID_REF=664A00F7C4834022CB3E7555003F820F:FG=1; ZFY=8PWNrASMBq2aRnb22uOOvvzCKFITOYbB6nR:AUa9vIUc:C; SP_FW_VER=4.220.1; iadexlist=550025314305; iadlist=550025314305; BAIDULOCNEW=__100000_131_1750913214000_1; LOCNEWMATCH=1; WISE_HIS_PM=1; fontsize=1.00; BAIDUCUID=_i-6tj8nvig3u28n0aS7ijul28lLu-iNga2Ua_iU2800O2u5lu2EijtvWuJW8SRAM6UmA; matrixstyle=0; AFD_IP=111.206.214.59; ST=0; H_WISE_SIDS=110086_651902_652167_654362_655051_655450_655503_655569_655723_656055_656174_656329_656662_656670_656750_656754_656860_656826_654309_656989_657022_657155_657158_657243_657375_655414_657588_657543_657746_657916_657998_657968_8000057_8000112_8000133_8000138_8000159_8000173_8000177_8000185_8000188_8000193_15124244_11140507_12146075_13150508_12151490_14150919_12152599_16155615_12158505_12160204_11160673_12162270; delPer=0; PANPSC=9252556991766329456%3AnHZOtuqy9asH4fj%2B7KWFy1cS2d9ns3O5C61tf8CKQkjYtXp3nsOchiA9YKyMd6JEdizeA%2Fkln021kha5%2BjnnHeNHiOwr%2ByPWOg9ifdcaUVdPhKZ71rNELY%2FC%2BCpyx6sYJlOfPZFHq36ck0T9AttkQZI6enfTG9Rj9MIM%2BqH0qxOrJuzsaw5IYGKmXcvc2dd5bH2fO7vFsi%2FVw7Eb5p097mGEDFjChM8gPte2imWG2X4VRHILCAWxgnhTAIHjj%2FUP9wZUbAHk4MY%2B17aKZYbZfhVEcgsIBbGCeFMAgeOP9Q%2B46IdIMW%2BZ6pKxVlqrIDxM;'
os.system(f'ffplay -allowed_extensions ALL -protocol_whitelist "http,file,crypto,https,tcp,tls,data" -headers "User-Agent: {user_agent}\r\nCookie: {cookie}\r\n" -v debug ' + safe_url)

# 使用 VLC 播放视频，vlc太弱了，不好修复播放器内部网路请求的ua，没有ffmpeg强大。
# /Applications/VLC.app/Contents/MacOS/VLC --http-user-agent="dumedia/7.84.0.7" -vvv 'https://pan.baidu.com/api/wechat/videostream.m3u8?audiotoken=%2BG2KyPLJZmZc7WiYoHMY07oTuw5zNrnsFkgceyGs1duVexxoltit2VkO2DW7ClSt4ljQkJWYJhdmauTsGysRReLGRZGDSPQwAWKcwjrQDwz6q99BFHTgtR7%2BplUkle3wj3bTS1gi%2F%2BPWEgfdoK4MI9AWz635KVMdZo5YjNyn1Y%2FhmN%2FhWedGEScdu9KwNmJtcRGOgUTG77yaUukkIFU2p0J9%2F8K9kPc%2FJMjBLWAfRl9uGnoAajyx%2B2C3oLOG9r5P&isfull=1&channel=lite_rapid&time=1737030564793&version=1.3.2&clienttype=291&dp-logid=35681100369575570027'
# os.system('/Applications/VLC.app/Contents/MacOS/VLC --http-user-agent="dumedia/7.84.0.7" -vvv ' + safe_url)