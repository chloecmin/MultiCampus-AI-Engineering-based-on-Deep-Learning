class LinearSearch:
    def __init__(self, data, key):
        self.list = data
        self.value = key
    def getSearchExist(self): #-->존재유무(True, False)
        if self.value in self.list:
            return True
        else:
            return False
    def getSearchCount(self): #-->개수반환(2)
        self.count = 0
        for self.l in self.list:
            if self.l == self.value:
                self.count += 1
        return self.count
    def getSearchElements(self): #-->[3, 3]
        self.ele_list = []
        for self.l in self.list:
            if self.l == self.value:
                self.ele_list.append(self.l)
        return self.ele_list
    def getSearchIndexes(self): #-->[1, 3]
        # self.idx_list = []
        # for i, self.l in enumerate(self.list):
        #     if self.l == self.value:
        #         self.idx_list.append(i)

        self.idx_list = [i for i, l in enumerate(self.list) if l == self.value]
        return self.idx_list

ls = LinearSearch([10, 3, 1, 3], 3)
print(ls.getSearchExist())
print(ls.getSearchCount())
print(ls.getSearchElements())
print(ls.getSearchIndexes())

