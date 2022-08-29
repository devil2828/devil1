def fibonacci(n):
    a=[0,1]
    for i in range(2,n+1):
        a.append(a[i-1] + a[i-2])
    return a
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(8))
print(fibonacci(9))
print(fibonacci(10))
print(fibonacci(11))
print(fibonacci(12))
print(fibonacci(13))
