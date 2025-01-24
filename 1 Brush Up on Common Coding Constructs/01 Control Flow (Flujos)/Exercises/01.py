def xxxxxx(n):
    suma = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            suma += i * j
    return suma

print(xxxxxx(5))