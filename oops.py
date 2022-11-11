class StringClass:
    def __init__(self):
        self.strings = self

    def stringlength(self):
        print(len(self.strings));

    def converttolist(self):
        listdata = []
        listdata[:0] = self.strings
        return listdata;

class PairsPossible(StringClass):
    def __init__(self):
        self.strings = input("Enter string: ")

    def getcombinations(self):
        from itertools import combinations
        list1 = list(self.strings)
        res = list(combinations(list1, 2))
        return res
    def printlist(self,lists):
        print(lists);

x = PairsPossible()
x.stringlength()
x.converttolist()
list1 = x.getcombinations()
x.printlist(list1);



