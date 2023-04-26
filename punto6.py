print("A continuacion ingrese la nota correspondiente teniendo en cuenta que la minima es 1.0 y la maxima es 5.0.")

p1 = float(input("Ingrese la nota de la primera evaluacion: "))
p2 = float(input("Ingrese la nota de la segunda evaluacion: "))
p3 = float(input("Ingrese la nota de la tercera evaluacion: "))

previos = (p1 + p2 + p3) / 3 * 0.60

print ("El promedio de los previos es: ", previos)

t1 = float(input("Ingrese la nota de el primer trabajo: "))
t2 = float(input("Ingrese la nota de el segundo trabajo: "))

trabajos = (t1 + t2) / 2 * 0.40

print ("El promedio de los trabajos es: ", trabajos)

notaFinal = (previos + trabajos)

print("Su nota final es: ", notaFinal)
