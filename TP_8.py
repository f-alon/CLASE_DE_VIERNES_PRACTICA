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

#Esta variable va a iniciar el bucle
iniciar = True

#este acumulador va a ir guardando las notas
acumulador = 0

# este contador va a ir contando la cantidad de notas ingresadas
contador = 0

while (iniciar):
    
    nota = int(input("Ingresar la nota del primer parcial (usar '-1' para salir): "))
    if nota != -1: #Si la nota ingresada no es -1
        acumulador = acumulador + nota # la variable acumulador guarda el valor ingresado de nota y la va sumando por cada iteracion
        contador = contador + 1 #contador va incrementando su valor en 1 por cada nota ingresada
        
    else: #bloque de condicion para que corte el bucle solamente cuando el -1 es ingresado y no se incluya en el promedio final
        if nota == -1:
            iniciar = False 

        promedio = (acumulador / contador)  #al final el promedio se calcula dividiendo el valor de acumulador por contador
        print("Promedio de las notas ingresadas --->", promedio)
        print("--- TERMINADO ---")

        







































