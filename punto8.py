presupuestoAnual = float(input("Por favor ingrese el presupuesto aual: "))

psiquiatria = float(input("Ingrese el porcentaje de presupuesto para psiquiatria: "))
pediatria = float(input("Ingrese el porcentaje de presupuesto para psiquiatria: "))
traumatologia = float(input("Ingrese el porcentaje de presupuesto para psiquiatria: "))

total = psiquiatria + pediatria + traumatologia

if total != 100:
    print("Error, la suma de los porcentajes debe ser igual a 100")
    
else:
    presupuesto_psiquiatria = presupuestoAnual * psiquiatria / 100
    print(f"Porcentaje para Psiquiatría: {psiquiatria}%")
    print(f"Presupuesto para Psiquiatría: ${presupuesto_psiquiatria:.2f}")
    
    presupuesto_pediatría = presupuestoAnual * pediatria / 100
    print(f"Porcentaje para Pediatría: {pediatria}%")
    print(f"Presupuesto para Pediatría: ${presupuesto_pediatría:.2f}")

    presupuesto_traumatologia = presupuestoAnual * traumatologia / 100
    print(f"Porcentaje para Traumatología: {traumatologia}%")
    print(f"Presupuesto para Traumatología: ${presupuesto_traumatologia:.2f}")

    