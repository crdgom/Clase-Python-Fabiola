def xxxxxx(n):
    suma = 0
    for i in range(1, n+1):
        print("i vale: ", i)
        for j in range(1, i+1):
            print("j vale: ", j)
            suma += i * j
            print("suma vale: ", suma)
    return suma

print(xxxxxx(5))