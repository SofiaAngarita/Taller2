distancia = float(input("Ingrese la distancia a recorrer: "))
diasEstancia = int(input("Ingrese los dias de estancia: "))

precioSinDescuento = distancia * 2.5
if diasEstancia >= 7 and distancia > 800:
        descuento = precioSinDescuento * 0.3
        precioFinal = precioSinDescuento - descuento
else:
    precioFinal = precioSinDescuento
   

print(f"El precio del tiquete de ida y vuelta es de ${precioFinal:.2f}")