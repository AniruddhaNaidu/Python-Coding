def fibonacci(num):
    if (num == 0):
        return 0
    elif (num == 1):
        return 1
    else:
        return (fibonacci(num - 1) + fibonacci(num - 2))


print(fibonacci(5))
print(fibonacci(10))
print(fibonacci(30))
print(fibonacci(35))
print(fibonacci(40))
print(fibonacci(50))