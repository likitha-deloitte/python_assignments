from math import sqrt
print("Equation: ax**2 + bx +c")
Result = lambda a, b, c: ((-b + sqrt((b*b)-(4*a*c))) / (2*a), (-b - sqrt((b*b) - (4*a*c))) / (2*a))
print("The roots of given equation are :", Result(1, -6, -8))
print('')

# ----------------------------------------------------
list1 = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
list_A = list(map(lambda x: x.count("A"), list1))
list_a = list(map(lambda x: x.count("a"), list1))
result = map(lambda x, y: x + y, list_A, list_a)
print("Occurrence of both letters 'A' and 'a' are : ", list(result))
print('')

# ----------------------------------------------------
list1 = [-1000, 500, -600, 700, 5000, -90000, -17500]
new_list = list(filter(lambda x: True if x > 0 else False,
                       map(lambda x: x*-1, list1)))
print("Numbers converted from negative to positive are : ", new_list)
print('')

# ----------------------------------------------------
list1 = ["Netflix", "Hulu", "Sling", "Hbo"]
list2 = [198, 166, 237, 125]
result = dict(zip(list1, list2))
print(result)


































