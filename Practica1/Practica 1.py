while True: #realiza el bucle cada vez que termine de ejecutarse una opcion
    print("$$$$$$$$ Menu Principal $$$$$$$$")
    print("1. Ejercicio 1: Triangulo")
    print("2. Ejercicio 2: Cuenta regresiva")
    print("3. Ejercicio 3: Numero primo")
    print("4. Salir")
    opcion = int(input("Ingrese una opcion: "))                 #recibe la opcion ingresada y la guarda como entero
    print()

    if opcion ==1:                                              # realiza el ejercicio 1
        print("Ejercicio 1 : Triangulo ------------------------------------------------------------")
        entrada = input('Introduzca un numero entero positivo: ')   #recibe el numero entero
        numero = int(entrada)                                       #convierte el string recibido a int
        i = 1                                                       #inicializa la variable
        if numero > 0:                                              #Valua si el numero ingresado es entero positivo
            while numero >= i:                                      #si el numero es mayor o igual al iterador realiza el bucle
                mensaje = '*' * i                                   # multiplica los asteriscos por la cantidad correspondiente al iterador
                print(i,". ",mensaje)                                      #imprime la cantidad de asteriscos correspondiente
                i += 1                                              #aumenta en una unidad al iterador
        elif numero <= 0:                                           # Si el numero es menor o igual a 0
            print('Por favor ingrese un numero mayor a 0')          #imprime el texto

    elif opcion == 2:                                              #Realiza el ejercicio 2
        print("Ejercicio 2 : Cuenta regresiva ------------------------------------------------------------")
        entrada1 = input('Introduzca un numero entero positivo: ')  #recibe el valor entero
        numero1 = int(entrada1)                                     #convierte el valor a int
                                                      #valua si el numero es mayor que 0
        if numero1 > 0:
            # crea arreglo para guardar los datos
            listaNumeros = []
            i = numero1
            # guardamos los valores en la lista
            while i >= 0:
                listaNumeros.append(i)                #agrega el numero al arreglo
                i -= 1
                                                       #Imprimimos los valores de la lista
            j=0
            for j in listaNumeros:
                print(j,end=",")
        elif numero1 <=0:                              # si  el numero es menor o igual a 0
            print('Los números negativos no son permitidos')  #muestra el texto
        print()

    elif opcion == 3:                                               #Realiza el ejercicio numero 3
        print("Ejercicio 3 : Numero Primo ------------------------------------------------------------")
        entrada2 = input('Introduzca un numero entero positivo: ')  # recibe el valor entero
        numero2 = int(entrada2)                                     # convierte el valor a int
        pri = True                                                  # inicializa la variable como verdadera
        if numero2 > 0:                                             #valua si el numero es mayor a 0
            for num in range(2,numero2):                            #Realiza la iteracion desde el primer numero hasta el valor anterior del numero ingresado
               if numero2 % num == 0:                              #valua si el residuo deel numero dividido dentro del interador es igual a 0
                    print('El numero ',numero2,' no es un numero primo')   #si la condicion se cumple ingresa y imprime que no es numero primo
                    pri = False                                            #asigna false a la variable
                    break                                                  #termina la ejecucion del for
            if pri == True:                                                #Si la condicion anterior no se cumple entonces el numero es primo
                print('El numero ',numero2,' es un numero primo')
        elif numero2 <=0:                                            #valua si el numero es menor o igual a 0
            print('Los números negativos no son permitidos')
        print()

    elif opcion == 4:
        break
    else:
        print("Ingrese una opcion correcta")
print()

