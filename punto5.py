
conejosNegros = int(input("Cuantos conejos negros desea comprar: ")) 
conejosBlancos = int(input("Cuantos conejos blancos desea comprar: ")) 

print (conejosNegros + conejosBlancos, "conejos")

p1 = int(input("Ingrese el precio de los conejos negros: "))
p2 = int(input("Ingrese el precio de los conejos blancos: "))
pt = (p1 * conejosNegros) + (p2 * conejosBlancos)

print (pt)

if conejosNegros > conejosBlancos:
    print("Se vendieron mas conejos negros.")

elif conejosBlancos > conejosNegros:
    print("Se vendieron mas conejos blancos.")

else:
    print("Se vendieron la misma cantidad de conejos de cada color.")