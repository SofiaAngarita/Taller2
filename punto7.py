articulo1 = input("Por favor ingrese el nombre del articulo que desea comprar: ")

precio = int(input("Por favor ingrese el precio del articulo ingresado: "))

clave = int(input("Por favor ingrese la clave (1 o 2): "))

if clave == 1:
    print(precio - (precio * 0.10))

elif clave == 2:
    print(precio - (precio * 0.20))
