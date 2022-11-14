N = int(input("Input integer: "))
list = []
for i in range(N):
    list1 = []
    for j in range(i+1):
        if j == 0 or j == i:
           list1.append(1)
        else:
           list1.append(list[i-1][j-1] + list[i-1][j])
    list.append(list1)

for i in range(N):
    for j in range(N-1):
        print(" ", end=" ")
    for j in range(i + 1):
        print(list[i][j], end=" ")
    print()