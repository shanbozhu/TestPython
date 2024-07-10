#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: msearch_performance.py
Author: zhushanbo
Date: 2023/4/21
Description:
极速版 - 搜索结果页\h5落地页\百家号落地页上屏耗时
"""

import sys
import os

path = sys.path[0]
os.system("python3 " + path + "/matrix_search_result_page.py")
os.system("python3 " + path + "/matrix_search_imagetext_landing_page.py")
os.system("python3 " + path + "/matrix_search_h5_landing_page.py")