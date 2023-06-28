class SearchDataCol(object):

    def __init__(self, dicti):
        self.name = dicti["name"]
        self.id = dicti["id"]
        self.accuracy = dicti["accuracy"]
        self.autoWrap = dicti["autoWrap"]