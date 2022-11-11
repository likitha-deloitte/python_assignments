#for printing diamond pattern
N = int(input("Enter total number of rows: "))
print("Diamond Pattern: ")
for i in range(N-1):
    for j in range(i, N):
        print("", end='  ')
    for j in range(i):
        print('*', end=' ')
    for j in range(i+1):
        print('*', end=' ')
    print()

for i in range(N):
    for j in range(i+1):
        print("", end='  ')
    for j in range(i, N-1):
        print('*', end=' ')
    for j in range(i, N):
        print('*', end=' ')
    print()


#for printing hollow right triangle
print("Hollow Right Triangle: ")
for i in range(1, N+1):
    for j in range(1, N+1):
        if(j == N) or (i == 1) or (j == i):
            print("*", end=" ")
        else:
            print("", end="  ")
    print()


#for printing hollow equilateral triangle
print("Hollow Equilateral Triangle: ")
for i in range(1, N + 1):
    for j in range(1, 2 * N):
        if (i == N) or (i + j == N + 1) or (j - i == N - 1):
            print("*", end=" ")
        else:
            print("", end="  ")
    print()









