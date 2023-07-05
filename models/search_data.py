#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from models.search_data_col import SearchDataCol
from models.search_data_row import  SearchDataRow

class SearchData(object):

    def __init__(self, dicti):
        self.columns = dicti["columns"] # arr
        self.rows = dicti["rows"] # arr

        tmp_col_arr = []
        for dic in self.columns:
            data_col = SearchDataCol(dic)
            tmp_col_arr.append(data_col)
        self.columns = tmp_col_arr

        tmp_row_arr = []
        for dic in self.rows:
            data_row = SearchDataRow(dic)
            tmp_row_arr.append(data_row)
        self.rows = tmp_row_arr