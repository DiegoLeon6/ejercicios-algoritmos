cantidadInvertida = float (input("Ingrese su cantidad invertida: "))
porcentajeIntereses = float (input("Ingrese el porcentaje de intereses: "))
periodo = float (input ("Ingrese el periodo: "))

valorIntereses = (cantidadInvertida * (porcentajeIntereses * periodo))/360
descuento = valorIntereses * 0.007

netoPagar = cantidadInvertida + valorIntereses - descuento

print ("Sus ganancias fueron: ", netoPagar)
