def xxxxxxx(n):
    for i in range(n):#tomara valores de 0-5 
        coef = 1
        for j in range(i+1):#j=1 i=1+1=2 range(2)=1
            print(coef, end=" ") #va a imprimir el primer valor de coef=1  
            coef = coef * (i - j) // (j + 1) #este valor de coef ya no lo imprime hasta el ultimo
        print() #Me doy cuenta que hasta el final de la iteracion el valor que imprime es 1 y descarta el ultimo valor de coef 

xxxxxxx(6)
"""
1
1 1
1 2 1
1 3 3 1 

"""
