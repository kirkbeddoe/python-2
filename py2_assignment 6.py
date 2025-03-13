def fibonacci(n):

    # handle the base cases first
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

# test cases
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(5))
print(fibonacci(7))
print(fibonacci(10))