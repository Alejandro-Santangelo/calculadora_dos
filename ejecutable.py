
import resta
import division
import multiplicacion
import suma

calculo = input("Escriba una operación de entre estas (suma, resta, multiplicacion, division): ")

a = float(input("Ingrese el primer valor: "))
b = float(input("Ingrese el segundo valor: "))

if calculo == "resta":
    resultado = resta.resta(a, b)
    print("El resultado de la resta es:", resultado)

elif calculo == "division":
    resultado = division.division(a, b)
    print("El resultado de la división es:", resultado)

elif calculo == "multiplicacion":
    resultado = multiplicacion.multiplicacion(a, b)
    print("El resultado de la multiplicación es:", resultado)

elif calculo == "suma":
    resultado = suma.suma(a, b)
    print("El resultado de la suma es:", resultado)

else:
    print("Operación no válida")
