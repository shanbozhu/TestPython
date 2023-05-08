from Models.search_data import SearchData

class Search:
    # status = 0
    # msg = ""
    # data = {}

    def __init__(self, dicti):
        self.status = dicti["status"]
        self.msg = dicti["msg"]
        self.data = dicti["data"] # dict

        searchData = SearchData(self.data)
        self.data = searchData # model
        # print("searchData = ", searchData.columns)