from Models.SearchData import SearchData

class Search:
    # status = 0
    # msg = ""
    # data = {}
    def __init__(self, dicti):
        self.status = dicti["status"]
        self.msg = dicti["msg"]
        self.data = dicti["data"] # dicti

        searchData = SearchData(self.data)
        self.data = searchData
        # print("searchData = ", searchData.columns)