'''
Crear una Clase Producto con los siguientes atributos:
- codigo
- nombre
- precio
Además, agregarle un atributo más a su elección pero que tengan relación a un producto.
Ejemplo: código: 1
Nombre: Ketchup ByB
Precio: 12
Marca: ByB
Crearla con su función __init__().
Agregar un método presentacion donde ustedes imprimen el nombre del producto con alguna frase si
así lo desean, ejemplo: “Ketchup ByB, dos veces Bueno”
Agregar un método llamada calcular_total, donde le pasaremos unas unidades y nos debe calcular el
costo total de los productos.
Ejemplo: obj.calcular_total(5) => resultado = 60.
'''
class Producto:
    def __init__(self, codigo, nombre, precio, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo

    def presentacion(self):
        print(self.nombre,"El producto que siempre quiso")

    def calcular_total(self,cantidad):
        total = cantidad * self.precio
        print('resultado = ',total)


while True:
    print("------- Menu Principal --------")
    print("1. Ingresar productos")
    print("2. Salir")
    opcion = int(input("Ingrese una opcion: "))  # recibe la opcion ingresada y la guarda como entero
    print()
    if opcion == 1:
        print("Ingrese los siguientes datos del producto")
        cod = int(input("codigo: "))
        nom = input("nombre: ")
        prec = float(input("precio: "))
        tip = input("tipo de producto:")
        cantid = int(input("cantidad: "))

        product = Producto(cod, nom, prec, tip)
        product.presentacion()
        product.calcular_total(cantid)
    elif opcion == 2:
        break
    else:
        print("Ingrese una opcion correcta")
print()
