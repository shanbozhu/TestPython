from Models.SearchDataCol import SearchDataCol
from Models.SearchDataRow import  SearchDataRow

class SearchData:
    columns = []
    rows = []
    def __init__(self, dicti):
        self.columns = dicti["columns"] # arr
        self.rows = dicti["rows"] # arr

        tmpColArr = []
        for dic in self.columns:
            dataCol = SearchDataCol(dic)
            tmpColArr.append(dataCol)
        self.columns = tmpColArr

        tmpRowArr = []
        for dic in self.rows:
            dataRow = SearchDataRow(dic)
            tmpRowArr.append(dataRow)
        self.rows = tmpRowArr