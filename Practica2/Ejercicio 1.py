'''
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo con el sexo y el nombre. El
grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre
posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y
sexo, y muestre por pantalla el grupo que le corresponde.
Ejemplo:
Nombre: Francisco, Sexo: Hombre => Grupo B
Nombre: Heather, Sexo: Mujer => Grupo A
Nombre: Pablo, Sexo: Hombre => Grupo A
Nombre: María, Sexo: Mujer => Grupo B
'''
# A --> Mujeres con nombre anterior a la M Y Hombres con nombre posterior a la N
# B --> Mujeres con nombre posterior a la N y Hombres con nombre anterior a la M
while True:
    print("-------- Menu Principal --------")
    print("1. Grupo A o B")
    print("2. Salir")
    opcion = int(input("Ingrese una opcion: "))  # recibe la opcion ingresada y la guarda como entero
    print()

    if opcion == 1:
        #Iniciales para el grupo A
        grupoAM = ['A','B','C','D','E','F','G','H','I','J','K','L']
        grupoAH = ['Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        #Iniciales para el grupo B
        grupoBH = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N']
        grupoBM = ['M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']

        #Preguntar nombre y sexo
        print("Ingrese los datos con la letra inicial en mayúscula")
        nombre = input('Ingrese su nombre: ')
        sexo = input('Ingrese su sexo (Hombre o Mujer): ')

        letraInicial = nombre[0]
        #si es mujer y la letra inicial del nombre esta entre A-M pertenece al grupo A
        #si es hombre y la letra inicial del nombre esta entre N-Z pertenece al grupo A
        #si es hombre y la letra inicial del nombre esta entre A-M pertenece al grupo B
        #si es mujer y la letra inicial del nombre esta entre N-Z pertenece al grupo B

        if sexo == 'Mujer':
            for i in grupoAM:
                if letraInicial == i:
                    print('Nombre: ' +nombre + ', Sexo: '+ sexo + '=> Grupo A')
                    break
            for h in grupoBM:
                if letraInicial == h:
                    print('Nombre: ' + nombre + ', Sexo: ' + sexo + '=> Grupo B')
                    break
        elif sexo =='Hombre':
            for j in grupoAH:
                if letraInicial == j:
                    print('Nombre: ' + nombre + ', Sexo: ' + sexo + '=> Grupo A')
                    break
            for k in grupoBH:
                if letraInicial == k:
                    print('Nombre: ' + nombre + ', Sexo: ' + sexo + '=> Grupo B')
                    break
        print()
    if opcion == 2:
        break
    else:
        print('Ingrese una opcion correcta')