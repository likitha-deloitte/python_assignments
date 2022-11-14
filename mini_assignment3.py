list = [[1, 1, 3, 2], [9, 8, 8, 1], [0, 4, 5, 0, 0, 1, 4]]
print("Duplicate values from the list are : ")
for y in list:
    for j in set(y):
        value = y.count(j)
        if(value > 1):
            print(str(j)+'->'+str(value))
print('')

# -------------------------------------------------
arr = ["Hello ", "take "]
arr2 = ["Dear", "Sir"]
arr3 = []
for v in arr:
    for v2 in arr2:
        arr3.append(v+v2)
print(arr3)
print('')

# --------------------------------------------------
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
list1[2][1][2].extend(sub_list)
print("New list is : ", list1)
print('')

# -------------------------------------------------
Keys = ['Ten', 'Twenty', 'Thirty']
Value = [10, 20, 30]
dictionary = {}
for i in range(0, len(Keys)):
    dictionary[Keys[i]] = Value[i]
print("Dictionary after mapping: ", dictionary)
print('')

# ---------------------------------------------------
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}
dict1.update(dict2)
print("Dictionary after merging: ", dict1)
print('')

# -------------------------------------------------------
sampleDict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
sampleDict["location"] = sampleDict.pop("city")
print("Dictionary after renaming: ", sampleDict)
print('')

# -------------------------------------------------------
dict = {'HuEx': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
list = []
for keys, values in dict.items():
    list.append([keys] + values)
print("Converted List from Dictionary: ", list)