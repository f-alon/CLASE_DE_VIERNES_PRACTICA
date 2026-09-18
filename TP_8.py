"""             Trabajo Práctico VIII
        Estructuras repetitivas condicionales"""

# Ejercicio 5 del tp 7 modificado para usar un while
# 5 Cree un script que le solicite al usuario ingresar 10 números enteros, y por cada uno, informarle si el mismo es positivo, negativo, o cero.


cantidad = 1

while cantidad != 11:

    numero = int(input("Ingresar un numero entero: "))
    cantidad = cantidad + 1

    positivo = numero > 0
    negativo = numero < 0

    if positivo:
        mensaje = "el numero es positivo"
        print(mensaje) 
    elif negativo:
        mensaje = "el numero es negativo"
        print(mensaje) 
    else:
        mensaje = "el numero es cero"
        print(mensaje) 
    