def xxxxxxx(n):
    for i in range(n):
        coef = 1
        for j in range(i+1):
            print(coef, end=" ")
            coef = coef * (i - j) // (j + 1)
        print()

xxxxxxx(6)



""" def xxxxxxxx(s):
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            subcadena = s[i:j+1]
            if subcadena == subcadena[::-1]:
                print(f"salida: {subcadena}")

xxxxxxxx("abbaacc")



def xxxxxxxxx(n):
    matriz = [[0] * n for _ in range(n)]
    val = n * n
    top, bottom, left, right = 0, n - 1, 0, n - 1

    while val > 0:
        for i in range(right, left - 1, -1):
            matriz[top][i] = val
            val -= 1
        top += 1
        for i in range(top, bottom + 1):
            matriz[i][left] = val
            val -= 1
        left += 1
        for i in range(left, right + 1):
            matriz[bottom][i] = val
            val -= 1
        bottom -= 1
        for i in range(bottom, top - 1, -1):
            matriz[i][right] = val
            val -= 1
        right -= 1

    for fila in matriz:
        print(fila)

xxxxxxxxx(4)




def xxxxxxxxxx(n):
    secuencia = "1"
    for _ in range(n):
        print(secuencia)
        siguiente = ""
        i = 0
        while i < len(secuencia):
            count = 1
            while i + 1 < len(secuencia) and secuencia[i] == secuencia[i+1]:
                i += 1
                count += 1
            siguiente += str(count) + secuencia[i]
            i += 1
        secuencia = siguiente

xxxxxxxxxx(5)



def xxxxxxxxxxx(n):
    for i in range(1, n+1):
        if i % 2 == 0:
            print(" " * (n-i) + "*" * i)
        else:
            print("*" * i)

xxxxxxxxxxx(6)



def xxxxxxxxxxxx(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if (i + j) % 2 == 0:
                print(f"{i*j:3}", end=" ")
            else:
                print(" - ", end=" ")
        print()

xxxxxxxxxxxx(5)



def xxxxxxxxxxxxx(n):
    for i in range(n):
        print(" " * (n-i-1) + "*" + " " * (2*i) + "*")
    for i in range(n-2, -1, -1):
        print(" " * (n-i-1) + "*" + " " * (2*i) + "*")

xxxxxxxxxxxxx(5)



def xxxxxxxxxxxxxx(hasta):
    primos = []
    for i in range(2, hasta + 1):
        es_primo = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(i)
    return primos

print(xxxxxxxxxxxxxx(50))




def xxxxxxxxxxxxxxx(n):
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    for num in reversed(fib):
        print(num, end=" ")

xxxxxxxxxxxxxxx(10)
 """