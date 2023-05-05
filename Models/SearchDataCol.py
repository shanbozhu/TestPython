class SearchDataCol:
    # name = ""
    # id = ""
    # accuracy = 0
    # autoWrap = 0

    def __init__(self, dicti):
        self.name = dicti["name"]
        self.id = dicti["id"]
        self.accuracy = dicti["accuracy"]
        self.autoWrap = dicti["autoWrap"]