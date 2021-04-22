def find_optimal(n):
    # start writing your code here
    sub = n - 2
    checkmax = []

    for na in range(1, sub+1):
        v = sub - na
        key = na + v * na
        checkmax.append(key)

    print(checkmax)
    max=0

    for i in range(0, len(checkmax)-1):
        if checkmax[i] > max and (checkmax[i + 1] is not None):
            max = checkmax[i]

    return max


print(find_optimal(6))