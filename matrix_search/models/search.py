#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from TestPython.matrix_search.models.search_data import SearchData

class Search(object):

    def __init__(self, dicti):
        self.status = dicti["status"]
        self.msg = dicti["msg"]
        self.data = dicti["data"] # dict

        search_data = SearchData(self.data)
        self.data = search_data # model