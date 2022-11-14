def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b
x = int(input("Enter number: "))
print("Fibonacci Sequence: ", list(fibonacci(x)))


