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

def buscador_palindromos(s):
    n = len(s) #evaluates the string size
    for i in range(n):#this string size will be used to iterarte wihtin the hole string
        for j in range(i, n): #here we are going to select an especific section of the string
            subcadena = s[i:j+1] #this section will colect the range of the string, first iteraction range(0,1),range(0,2),range(0,3) etc
            if subcadena == subcadena[::-1]:#whenever we findout that the reversed section of the substring is equal to the substring we print the substring
                print(f"Se encontraron los siguientes palindromos dentro de la cadena: {subcadena}")

xxxxxxxx("abbaacc")
º         (11111111)-1=?
            111111
             11111
              1111
                11


def xxxxxxxxxxx(n):
    for i in range(1, n+1):
        if i % 2 == 0:
            print(" " * (n-i) + "*" * i)
        else:
            print("*" * i)

xxxxxxxxxxx(6)



>>>>>>> 9019f365d23efacb65d4a18230821fa23755874a

