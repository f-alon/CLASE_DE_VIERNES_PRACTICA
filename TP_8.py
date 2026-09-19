"""             Trabajo Práctico VIII
        Estructuras repetitivas condicionales"""

# Ejercicio 5 del tp 7 modificado para usar un while
# 5 Cree un script que le solicite al usuario ingresar 10 números enteros, y por cada uno, informarle si el mismo es positivo, negativo, o cero.


# cantidad = 1

# while cantidad != 11:

#     numero = int(input("Ingresar un numero entero: "))
#     cantidad = cantidad + 1

#     positivo = numero > 0
#     negativo = numero < 0

#     if positivo:
#         mensaje = "el numero es positivo"
#         print(mensaje) 
#     elif negativo:
#         mensaje = "el numero es negativo"
#         print(mensaje) 
#     else:
#         mensaje = "el numero es cero"
#         print(mensaje) 


# 1. Cree un script que le pida al usuario ingresar palabras, una a una, hasta que el usuario ingrese la palabra “parar”. A medida que se van ingresando las palabras, el programa simplemente debe mostrarlas en 
# pantalla. Al detectar la palabra para detenerse, debe mostrar el mensaje “--- TERMINADO ---”

#palabra = input("Ingresar una palabra (usar 'parar' para salir): ")

# terminar = "parar"

# while (terminar):

#     palabra = input("Ingresar una palabra (usar 'parar' para salir): ")
#     print("la palabra ingresada es: ", palabra)
#     if palabra == terminar:
#         terminar = False
#         print("--- TERMINADO ---")



# 2. Cree un script que le solicite al usuario ingresar notas de parciales por teclado, hasta que el usuario ingrese el valor -1, indicando que ya no hay más notas para cargar. Una vez ingresadas las notas, 
# el programa debe informar la nota promedio (tenga cuidado de no incluir al -1 dentro del promedio).

#nota = int(input("Ingresar la nota del primer parcial (usar '-1' para salir): "))

terminar = "-1"

#hacer variable que acumule las notas sumandolas para despues poder sacar el promedio
acumulador = 0
print("Acumulador --->",acumulador)

contador = 0
print("Contador --->",contador)

while (terminar):

    nota = int(input("Ingresar la nota del primer parcial (usar '-1' para salir): "))

    acumulador = acumulador + nota
    print("Acumulador + nota --->",acumulador)

    contador = contador + 1
    print("Contador + 1 --->",contador)

    promedio = acumulador / contador

    if nota == terminar:
        terminar = False

        print("promedio de las notas ingresadas --->", promedio)
        print("--- TERMINADO ---")

        







































