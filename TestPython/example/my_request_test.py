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

# 取消InsecureRequestWarning警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import requests

cookies = {
    'ST': '2',
    'bd_logap_verify': '1',
    'BAIDUID': 'BCBA998E4BCBC2CEF12D83D131F05C18:FG=1',
    'BAIDUCUID': '_i-6tj8nvig3u28n0aS7ijul28lLu-iNga2Ua_iU2800O2u5lu2EijtvWuJW8SRAM6UmA',
    'fontsize': '1.16',
    'AFD_IP': '211.95.58.9',
    'WISE_HIS_PM': '0',
    'BAIDULOCNEW': '13523298.869980_3641065.962499_100000.00_289_1719380562000_1',
    'H_WISE_SIDS': '110085_295986_298192_299594_500207_603328_298696_301026_282466_295818_607981_307086_608074_608717_608883_305467_607534_608324_609053_608769_609098_609161_609183_609178_609245_609295_609307_609222_609392_609510_609527_609576_607111_307653_609647_608152_609592_609743_608028_607027_609921_277936_609804_610002_609316_609769_609606_610121_610128_610110_610265_301668_610427_610454_610120_610593_610630_610687_607725_295151_610760_610695',
}

headers = {
    'Accept': '*/*',
    # 'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16C104 matrixstyle/1 SP-engine/2.82.0 bdapp/1.0 (tomas; tomas) tomas/2.29.0.5 (Baidu; P2 12.1.2)',
    # 'Cookie': 'ST=2; bd_logap_verify=1; BAIDUID=BCBA998E4BCBC2CEF12D83D131F05C18:FG=1; BAIDUCUID=_i-6tj8nvig3u28n0aS7ijul28lLu-iNga2Ua_iU2800O2u5lu2EijtvWuJW8SRAM6UmA; fontsize=1.16; AFD_IP=211.95.58.9; WISE_HIS_PM=0; BAIDULOCNEW=13523298.869980_3641065.962499_100000.00_289_1719380562000_1; H_WISE_SIDS=110085_295986_298192_299594_500207_603328_298696_301026_282466_295818_607981_307086_608074_608717_608883_305467_607534_608324_609053_608769_609098_609161_609183_609178_609245_609295_609307_609222_609392_609510_609527_609576_607111_307653_609647_608152_609592_609743_608028_607027_609921_277936_609804_610002_609316_609769_609606_610121_610128_610110_610265_301668_610427_610454_610120_610593_610630_610687_607725_295151_610760_610695',
}

params = {
    'action': 'update',
    'uuid': '31CD314763DEA42D303223ED424BC8BF42EF12',
    'appname': 'tomas',
    'branchname': 'tomas',
    'cfrom': '1025512a',
    'ds_lv': '4',
    'ds_stc': '0.7740',
    'from': '1025512a',
    'fv': '13.44.0.19',
    'matrixstyle': '1',
    'mps': '154326807',
    'mpv': '1',
    'network': '1_0',
    'osbranch': 'i7',
    'osname': 'baiduboxapp',
    'service': 'bdbox',
    'sid': '35713_3-74953_5-78031_3-71741_6-35809_3-35412_1-77907_1-35776_12-35790_1-35839_1-35832_3-35870_1-35827_1-78029_3-105949_1-75947_2-35864_1-35510_4-35719_1-5301_7550-75001_1-35821_4-103916_8-78752_3-78709_3-35779_3-79203_3-78040_1-73147_2-33497_1-78713_1-71552_5-75663_5-77832_4-35873_10',
    'st': '2',
    'submatrix': 'Tomas',
    'ua': '828_1792_iphone_2.29.0.5_0',
    'uid': '6D989E434574A6D38712A794674F6D74C81FC7309OLFQBBSCCC',
    'zid': 'ZCN2NlJSeiAAAAACVAP6I28BawJl8TAg_DxJSnRBTVBnZWZnMGRjamdqa2BnZmIxNDBiZGdrYWYwYGRqYmprM35jXDVQAAAAAGZ7qlI8VX0',
    'lst': '0',
    'protocol': 'json',
    'pv': '1',
}

json_data = {
    'version': '{"novel":{"tingshu_default_home":"0","tingshu_beginner_guide":"0","tingshu_top_tab":"0","novel_auto_play":"0"},"flowvideo":{"flowvideo_conf":"0"},"scheme":{"no_trace":"0","desc_patch":"0"},"searchVideo":{"searchvideo_flowvideo":"0"},"account":{"menu_login_tips":"0","accsrc":"0"},"personal_center":{"chest_personal_bar":"0","clear_cache":"0","alert_img":"0","home_img":"0","setting_dsp_ad":"0"},"usersetting":{"diskclean_guide":"0"},"bottom_bar_big_font":{"bottom_bar_big_font":"0"},"feed":{"feed_conf":"0","push_config":"0","landing_page_task_unregister":"0","bear_pow_tips":"0","feedtab":"0","feed_dislike_toast":"0","fancy_operation":"0","tts_conf":"0","note_banner":"0","feed_operation_conf":"0","feed_interest_selection":"0","h2_domain":"0","homepage_feed":"0","h2_domain_network":"0","kanting_conf":"0","feed_personalise_guide":"0","pull_refresh_info":"0"},"bottom_bar_red":{"bottom_bar_red":"0"},"location":{"location":"0"},"abtest":{"abtest":"0"},"share":{"share_banner":"0","share_operation":"0"},"video":{"nid_check":"0","videoconf":"0","videoautoplay":"0"},"operation":{"tomas_emo_toast":"0","skinlogo":"0","tomas_bar_bubble":"0","shake":"0","home_resource":"0"},"mission_task":{"mission_ab_switch":"0","index_kit":"0"},"individuation":{"st":"0"},"bottom_bar":{"bottom_bar":"0"},"home":{"light_framework":"0","new_home_ctrl":"0","user_model":"0","custom_skin_update":"0","search_frame_bar":"0","tomas_user_info":"0","launch_tab":"0","user_channel_tomas":"0","servicediamond":"0","search_input_toast":"0","tomas_fourth_tab":"0","callback_info":"0","rtplus":"0","home_live_enter_op":"0","hotwordcard":"0","v1_tab":"0","index_tips_new":"0","v1_tab_operation":"0","lite_search_bottom_tip":"0","index_guide":"0","task_register":"0","tab_text":"0","newbusinesslink":"0","task_popover":"0","business_link":"0","bubble_bar_tomas":"0","home_live_enter":"0"},"new_member":{"new_member":"0"},"network":{"request_control":"0"},"new_feature":{"spotlight_blacklist":"0","appscore":"0"},"hotdiscussion":{"hotdiscussion_conf":"0"},"umdata":{"umdata_conf":"0"},"word_command":{"is_silencescan":"0"},"hybrid":{"hybridTpl":"0"},"search":{"search_ernie":"0","search_ernie_op":"0","videotab_query":"0","dynamic_query":"0","search_ernie_bar":"0","hot_search":"0"},"splash":{"splash":"0"}}',
    'data': '{"hybrid":{"hybridTpl":{"injectjs":"20170614112922","feed":"0","profile":"20171102143659","weather":"20170427154844"}},"splash":{"splash":{"is_block_shake_gesture":"0","download_size_material":"00","ipdx":"","new_install_launch":"1","query":"-2qAC","feed_news":"-2qAC","sys_ua":"Mozilla\\/5.0 (iPhone; CPU iPhone OS 12_1_2 like Mac OS X) AppleWebKit\\/605.1.15 (KHTML, like Gecko) Mobile\\/16C104 matrixstyle\\/1 SP-engine\\/2.82.0","is_invoke":"0","diskInfo":{"quota":"80","size":"0"},"caidInfo":{"caid_valid":"0"},"search":"y_ZxCqqSB","download_size_zip":"00"}},"home":{"tab_text":{},"rtplus":{},"index_guide":{"id":"0"},"task_register":{"isActive":"1","isActiveSoundNovelTimer":"1","isActiveSearch":"1","isActiveSoundNovelFindBook":"1","isFindBookTargetUser":"1","productId":"14"},"newbusinesslink":{"list":{}},"new_home_ctrl":{"switch":"0","switchReason":""},"servicediamond":{"tipsVersion":"","groupsVersion":""},"search_input_toast":{"invokeChannel":""}},"feed":{"feedtab":{"isNewHomePage":"0","smartSortSwitch":"1","tabs":[{"status":"0","id":"32","newTip":"0","timestamp":"0","name":"小说","layout":""},{"status":"0","id":"8","newTip":"0","timestamp":"0","name":"热搜","layout":""},{"status":"0","newTip":"0","layout":"","id":"192","timestamp":"0","name":"视频","lastIntoTime":"1719380535"}],"isManualChangeCity":"0","bubbleVersion":{"channel":"0","plus":"0"},"newTipTapedNum":"0"}},"new_feature":{"appscore":{"app_V":"0","time":"0","choice":"0"}},"mission_task":{"index_kit":{"template":["goldenEggStatus"]}},"usersetting":{"diskclean_guide":{"device_disk_size":"64"}},"video":{"nid_check":{"nids":[]}}}',
    'pubdata': '{"mktcoord":"13523298.869980,3641065.962499","newNorm":"0","usrc":"1","location":"121.480539,31.235929,---,100000.000000,1","firstart":"1"}',
}

# r = requests.post(url, params=params, cookies=cookies, headers=headers, json=body, timeout=2, verify=False) # 内容类型json

# response = requests.post('https://mbd.baidu.com/searchbox', params=params, cookies=cookies, headers=headers, json=json_data, timeout=2, verify=False)
#
# print("r.text =", response.text)


# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
data = '{"version":"{\\"novel\\":{\\"tingshu_default_home\\":\\"0\\",\\"tingshu_beginner_guide\\":\\"0\\",\\"tingshu_top_tab\\":\\"0\\",\\"novel_auto_play\\":\\"0\\"},\\"flowvideo\\":{\\"flowvideo_conf\\":\\"0\\"},\\"scheme\\":{\\"no_trace\\":\\"0\\",\\"desc_patch\\":\\"0\\"},\\"searchVideo\\":{\\"searchvideo_flowvideo\\":\\"0\\"},\\"account\\":{\\"menu_login_tips\\":\\"0\\",\\"accsrc\\":\\"0\\"},\\"personal_center\\":{\\"chest_personal_bar\\":\\"0\\",\\"clear_cache\\":\\"0\\",\\"alert_img\\":\\"0\\",\\"home_img\\":\\"0\\",\\"setting_dsp_ad\\":\\"0\\"},\\"usersetting\\":{\\"diskclean_guide\\":\\"0\\"},\\"bottom_bar_big_font\\":{\\"bottom_bar_big_font\\":\\"0\\"},\\"feed\\":{\\"feed_conf\\":\\"0\\",\\"push_config\\":\\"0\\",\\"landing_page_task_unregister\\":\\"0\\",\\"bear_pow_tips\\":\\"0\\",\\"feedtab\\":\\"0\\",\\"feed_dislike_toast\\":\\"0\\",\\"fancy_operation\\":\\"0\\",\\"tts_conf\\":\\"0\\",\\"note_banner\\":\\"0\\",\\"feed_operation_conf\\":\\"0\\",\\"feed_interest_selection\\":\\"0\\",\\"h2_domain\\":\\"0\\",\\"homepage_feed\\":\\"0\\",\\"h2_domain_network\\":\\"0\\",\\"kanting_conf\\":\\"0\\",\\"feed_personalise_guide\\":\\"0\\",\\"pull_refresh_info\\":\\"0\\"},\\"bottom_bar_red\\":{\\"bottom_bar_red\\":\\"0\\"},\\"location\\":{\\"location\\":\\"0\\"},\\"abtest\\":{\\"abtest\\":\\"0\\"},\\"share\\":{\\"share_banner\\":\\"0\\",\\"share_operation\\":\\"0\\"},\\"video\\":{\\"nid_check\\":\\"0\\",\\"videoconf\\":\\"0\\",\\"videoautoplay\\":\\"0\\"},\\"operation\\":{\\"tomas_emo_toast\\":\\"0\\",\\"skinlogo\\":\\"0\\",\\"tomas_bar_bubble\\":\\"0\\",\\"shake\\":\\"0\\",\\"home_resource\\":\\"0\\"},\\"mission_task\\":{\\"mission_ab_switch\\":\\"0\\",\\"index_kit\\":\\"0\\"},\\"individuation\\":{\\"st\\":\\"0\\"},\\"bottom_bar\\":{\\"bottom_bar\\":\\"0\\"},\\"home\\":{\\"light_framework\\":\\"0\\",\\"new_home_ctrl\\":\\"0\\",\\"user_model\\":\\"0\\",\\"custom_skin_update\\":\\"0\\",\\"search_frame_bar\\":\\"0\\",\\"tomas_user_info\\":\\"0\\",\\"launch_tab\\":\\"0\\",\\"user_channel_tomas\\":\\"0\\",\\"servicediamond\\":\\"0\\",\\"search_input_toast\\":\\"0\\",\\"tomas_fourth_tab\\":\\"0\\",\\"callback_info\\":\\"0\\",\\"rtplus\\":\\"0\\",\\"home_live_enter_op\\":\\"0\\",\\"hotwordcard\\":\\"0\\",\\"v1_tab\\":\\"0\\",\\"index_tips_new\\":\\"0\\",\\"v1_tab_operation\\":\\"0\\",\\"lite_search_bottom_tip\\":\\"0\\",\\"index_guide\\":\\"0\\",\\"task_register\\":\\"0\\",\\"tab_text\\":\\"0\\",\\"newbusinesslink\\":\\"0\\",\\"task_popover\\":\\"0\\",\\"business_link\\":\\"0\\",\\"bubble_bar_tomas\\":\\"0\\",\\"home_live_enter\\":\\"0\\"},\\"new_member\\":{\\"new_member\\":\\"0\\"},\\"network\\":{\\"request_control\\":\\"0\\"},\\"new_feature\\":{\\"spotlight_blacklist\\":\\"0\\",\\"appscore\\":\\"0\\"},\\"hotdiscussion\\":{\\"hotdiscussion_conf\\":\\"0\\"},\\"umdata\\":{\\"umdata_conf\\":\\"0\\"},\\"word_command\\":{\\"is_silencescan\\":\\"0\\"},\\"hybrid\\":{\\"hybridTpl\\":\\"0\\"},\\"search\\":{\\"search_ernie\\":\\"0\\",\\"search_ernie_op\\":\\"0\\",\\"videotab_query\\":\\"0\\",\\"dynamic_query\\":\\"0\\",\\"search_ernie_bar\\":\\"0\\",\\"hot_search\\":\\"0\\"},\\"splash\\":{\\"splash\\":\\"0\\"}}","data":"{\\"hybrid\\":{\\"hybridTpl\\":{\\"injectjs\\":\\"20170614112922\\",\\"feed\\":\\"0\\",\\"profile\\":\\"20171102143659\\",\\"weather\\":\\"20170427154844\\"}},\\"splash\\":{\\"splash\\":{\\"is_block_shake_gesture\\":\\"0\\",\\"download_size_material\\":\\"00\\",\\"ipdx\\":\\"\\",\\"new_install_launch\\":\\"1\\",\\"query\\":\\"-2qAC\\",\\"feed_news\\":\\"-2qAC\\",\\"sys_ua\\":\\"Mozilla\\\\\\/5.0 (iPhone; CPU iPhone OS 12_1_2 like Mac OS X) AppleWebKit\\\\\\/605.1.15 (KHTML, like Gecko) Mobile\\\\\\/16C104 matrixstyle\\\\\\/1 SP-engine\\\\\\/2.82.0\\",\\"is_invoke\\":\\"0\\",\\"diskInfo\\":{\\"quota\\":\\"80\\",\\"size\\":\\"0\\"},\\"caidInfo\\":{\\"caid_valid\\":\\"0\\"},\\"search\\":\\"y_ZxCqqSB\\",\\"download_size_zip\\":\\"00\\"}},\\"home\\":{\\"tab_text\\":{},\\"rtplus\\":{},\\"index_guide\\":{\\"id\\":\\"0\\"},\\"task_register\\":{\\"isActive\\":\\"1\\",\\"isActiveSoundNovelTimer\\":\\"1\\",\\"isActiveSearch\\":\\"1\\",\\"isActiveSoundNovelFindBook\\":\\"1\\",\\"isFindBookTargetUser\\":\\"1\\",\\"productId\\":\\"14\\"},\\"newbusinesslink\\":{\\"list\\":{}},\\"new_home_ctrl\\":{\\"switch\\":\\"0\\",\\"switchReason\\":\\"\\"},\\"servicediamond\\":{\\"tipsVersion\\":\\"\\",\\"groupsVersion\\":\\"\\"},\\"search_input_toast\\":{\\"invokeChannel\\":\\"\\"}},\\"feed\\":{\\"feedtab\\":{\\"isNewHomePage\\":\\"0\\",\\"smartSortSwitch\\":\\"1\\",\\"tabs\\":[{\\"status\\":\\"0\\",\\"id\\":\\"32\\",\\"newTip\\":\\"0\\",\\"timestamp\\":\\"0\\",\\"name\\":\\"小说\\",\\"layout\\":\\"\\"},{\\"status\\":\\"0\\",\\"id\\":\\"8\\",\\"newTip\\":\\"0\\",\\"timestamp\\":\\"0\\",\\"name\\":\\"热搜\\",\\"layout\\":\\"\\"},{\\"status\\":\\"0\\",\\"newTip\\":\\"0\\",\\"layout\\":\\"\\",\\"id\\":\\"192\\",\\"timestamp\\":\\"0\\",\\"name\\":\\"视频\\",\\"lastIntoTime\\":\\"1719380535\\"}],\\"isManualChangeCity\\":\\"0\\",\\"bubbleVersion\\":{\\"channel\\":\\"0\\",\\"plus\\":\\"0\\"},\\"newTipTapedNum\\":\\"0\\"}},\\"new_feature\\":{\\"appscore\\":{\\"app_V\\":\\"0\\",\\"time\\":\\"0\\",\\"choice\\":\\"0\\"}},\\"mission_task\\":{\\"index_kit\\":{\\"template\\":[\\"goldenEggStatus\\"]}},\\"usersetting\\":{\\"diskclean_guide\\":{\\"device_disk_size\\":\\"64\\"}},\\"video\\":{\\"nid_check\\":{\\"nids\\":[]}}}","pubdata":"{\\"mktcoord\\":\\"13523298.869980,3641065.962499\\",\\"newNorm\\":\\"0\\",\\"usrc\\":\\"1\\",\\"location\\":\\"121.480539,31.235929,---,100000.000000,1\\",\\"firstart\\":\\"1\\"}"}'
response = requests.post('https://mbd.baidu.com/searchbox', params=params, cookies=cookies, headers=headers, data=data, timeout=2, verify=False)
print("r.text =", response.text)

curl_command = curlify.to_curl(response.request) # -H 'Accept-Encoding: gzip, deflate' 输出的curl命令需要去掉这项，否则会提示"在终端输出二进制打乱终端的显示"
print("curl_command =", curl_command)