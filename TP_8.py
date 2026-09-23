        #          Trabajo Práctico VIII
        # Estructuras repetitivas condicionales

# Ejercicio 5 del tp 7 modificado para usar un while
# 5 Cree un script que le solicite al usuario ingresar 10 números enteros, y por cada uno, informarle si el mismo es positivo, negativo, o cero.


# cantidad = 0

# while cantidad != 10:

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

# terminar = "parar"

# while (terminar):

#     palabra = input("Ingresar una palabra (usar 'parar' para salir): ")
#     print("la palabra ingresada es: ", palabra)
#     if palabra == terminar:
#         terminar = False
#         print("--- TERMINADO ---")


#otra forma de hacer el 1 --- usar el not para ingresar al while sirve para validaciones ---

# fin = False
# while not(fin):
#     palabra = input("Ingresar una palabra: ") 
#     fin = (palabra == "parar")
#     if fin:
#         print("TERMINADO")
#     else:
#         print(palabra)    


# 2. Cree un script que le solicite al usuario ingresar notas de parciales por teclado, hasta que el usuario ingrese el valor -1, indicando que ya no hay más notas para cargar. Una vez ingresadas las notas, 
# el programa debe informar la nota promedio (tenga cuidado de no incluir al -1 dentro del promedio).

#nota = int(input("Ingresar la nota del primer parcial (usar '-1' para salir): "))

# #Esta variable va a iniciar el bucle
# iniciar = True

# #este acumulador va a ir guardando las notas
# acumulador = 0

# # este contador va a ir contando la cantidad de notas ingresadas
# contador = 0

# while (iniciar):
    
#     nota = int(input("Ingresar la nota del primer parcial (usar '-1' para salir): "))
#     if nota != -1: #Si la nota ingresada no es -1
#         acumulador = acumulador + nota # la variable acumulador guarda el valor ingresado de nota y la va sumando por cada iteracion
#         contador = contador + 1 #contador va incrementando su valor en 1 por cada nota ingresada
        
#     else: #bloque de condicion para que corte el bucle solamente cuando el -1 es ingresado y no se incluya en el promedio final
#         if nota == -1:
#             iniciar = False 

#         promedio = (acumulador / contador)  #al final el promedio se calcula dividiendo el valor de acumulador por contador
#         print("Promedio de las notas ingresadas --->", promedio)
#         print("--- TERMINADO ---")

        
# 3. Cree un script que le solicite al usuario leer un número entero entre 1 y 100. El programa debe ser capaz de solicitarle al usuario que reingrese el número cuantas veces sea necesario, 
# hasta que el usuario provea un dato válido. Cada vez que detecte un error de validación, informele al usuario cuál fue el error, con los mensajes “El dato ingresado no es numérico.”, o 
# “El número ingresado está fuera del rango permitido.”. Finalmente, cuando el usuario ingrese un dato válido, muestre el mensaje “[NÚMERO] es válido. Gracias!”.


rango_valido = False
dato_numerico = False
rango_no_valido = False

while not(rango_valido) and not(dato_numerico):
    numero = input("Ingresar un numero entre 1 y 100: ")

    dato_numerico = numero.isdigit()
    dato_no_numerico = numero.isalpha()
    fuera_rango = rango_valido == False

    if dato_numerico:
        rango_valido = (int(numero) >= 1 and int(numero) <= 100)
        if rango_valido:
            mensaje = f" {numero} es válido. Gracias!"
            print(mensaje)
        elif fuera_rango:
            print("Dato fuera de rango")    

    if dato_no_numerico: 
        print("Dato no valido")            