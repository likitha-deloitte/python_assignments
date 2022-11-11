class StringClass:

    def stringlength(self):
        print(len(self.strings))

    def converttolist(self):
        return list(self.strings);

class PairsPossible(StringClass):

    def getcombinations(self):
        from itertools import combinations
        res = list(combinations(list(self.pairstring),2))
        return res
    def printlist(self,lists):
        print(lists);

class SearchCommonElements(PairsPossible):
    def __init__(self,newstring):
        self.strings = input('Enter String: ')
        self.pairstring= newstring

    def commoncharacters(self):
        from collections import Counter
        d1 = Counter(self.pairstring)
        d2 = Counter(self.strings)
        common_dict = d1 & d2
        if len(common_dict) == 0:
            return "No common Characters.";
        else:
            return list(common_dict)


x = SearchCommonElements('334455')
x.stringlength()
print(x.converttolist())
pairs = x.getcombinations()
x.printlist(pairs)
print(x.commoncharacters())




