llamada = int(input("Ingrese el tiempo total de la llamda "))
tiempo = 200 / 2

if llamada <= 3:
    print("200 pesos")

elif llamada > 3:
    print(tiempo * llamada, "pesos")