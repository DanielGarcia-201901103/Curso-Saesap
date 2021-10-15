'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número
primo o no
'''
while True:
    print("\t Menu Principal")
    print("1. Ejercicio 1: Triangulo")
    print("2. Ejercicio 2: Cuenta regresiva")
    print("3. Ejercicio 3: Numero primo")
    print("4. Salir")
    opcion = int(input("Ingrese una opcion: "))
    print()

    if opcion ==1:
        entrada = input('Introduzca un numero entero positivo: ')
        numero = int(entrada)
        i = 1

        if numero > 0:
            while numero >= i:
                mensaje = '*' * i
                print(mensaje)
                i += 1

        elif numero < 0 or numero == 0:
            print('Por favor ingrese un numero mayor a 0')
    elif opcion == 2:
        #recibe el valor entero
        entrada1 = input('Introduzca un numero entero positivo: ')
        #convierte el valor a int
        numero1 = int(entrada1)
        #valua si el numero es mayor que 0
        if numero1 > 0:
            # crea arreglo para guardar los datos
            listaNumeros = []
            i = numero1
            # guardamos los valores en la lista
            while i >= 0:
                listaNumeros.append(i)
                i -= 1
            #Imprimimos los valores
            j=0
            for j in listaNumeros:
                print(j,end=",")
        elif numero1 < 0 and numero1 ==0:
            print('Los números negativos no son permitidos')
        print()
    elif opcion == 3:
        # recibe el valor entero
        entrada2 = input('Introduzca un numero entero positivo: ')
        # convierte el valor a int
        numero2 = int(entrada2)
        if numero1 > 0:
            k=0
            if numero1 % 1 ==0 and numero1 % numero1 == 0  :
                print("El numero: ",numero1," es un numero primo")
            elif numero1%1
        elif numero1 < 0 and numero1 ==0:
            print('Los números negativos no son permitidos')
        print()

    elif opcion == 4:
        break
    else:
        print("Ingrese una opcion correcta")
print()

