def factorial(n):

    # handle the base case first
    if n == 0:
        return 1

    return n * factorial(n-1)

# test cases
print(factorial(0))
print(factorial(1))
print(factorial(5))
print(factorial(7))