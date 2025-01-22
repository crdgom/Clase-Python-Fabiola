def parse_formula(formula):
    elements = {} #es una tupla vacia 
    i = 0
    while i < len(formula):#mientras i sea menor a la longitud de la formula, osea que va a recorrer cada elemento de la formula
    
        if formula[i].isupper():#Me imagino que isupper es una funcion que evalua si es mayuscula
            element = formula[i]#En caso de que sea mayus va a guardar ese elemento en la tupla element
            i += 1 #umentamos el valor de i
            if i < len(formula) and formula[i].islower: #En el siguiente bucle vamos a evaluar/recorrer al siguiente elemento de la formula concatenando los elemento si es minuscula hasta al final, pienos esto porque las cadenas cuando se suman en verdad se concatenan, ademas tiene un error porque necesitamos el parentesis para lamar a la funcion 
                element += formula[i]
                i += 1
            count = ""
            while i < len(formula) and formula[i].isdigit:#Mientas que el siguiente elemento sea un numero: (aqui tambien necesitamos los parentesis para mandar a llamar a la funcion)
                count += formula[i]#Aqui se va a agregar a la variable count todos los numeros que vaya encontrando uno por uno porque incrementa i cada vez 
                i += 1 
            if count == "":#Si no encuentra digitos entonces count es igual a 1
                #Aqui me surge la duda, si declaramos a count como string y leugo le quiermos asignar un uno va a dar error yo parsearia el count a string antes de agregarle el 1 str(count)
                count = 1
            elements[element] = int(count)#Llena la lista con los numeros que encontro despues de haberlos pasado a enteros
        else: #Aqui no encuntro como los esta mostrando dberia concatenar la cantidad del los elemtnos al final 
            i += 1
    return elements

"""No veo que se este llamadno a la funcion, osea que no tiene valor la variable formaula"""
