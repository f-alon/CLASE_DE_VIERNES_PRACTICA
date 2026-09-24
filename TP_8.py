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


# rango_valido = False
# dato_numerico = False
# rango_no_valido = False

# while not(rango_valido) and not(dato_numerico):
#     numero = input("Ingresar un numero entre 1 y 100: ")

#     dato_numerico = numero.isdigit()
#     dato_no_numerico = numero.isalpha()
#     fuera_rango = rango_valido == False

#     if dato_numerico:
#         rango_valido = (int(numero) >= 1 and int(numero) <= 100)
#         if rango_valido:
#             mensaje = f" {numero} es válido. Gracias!"
#             print(mensaje)
#         elif fuera_rango:
#             print("Dato fuera de rango")    

#     if dato_no_numerico: 
#         print("Dato no valido")        


#5. Si bien el While es útil cuando desconocemos la cantidad de veces que repetiremos un bloque de instrucciones, también puede ser utilizado en los mismos casos que es utilizado el For 
# (aunque la inversa no es verdadera). Rehaga todos los ejercicios del Trabajo Práctico VII utilizando un While en lugar de un For.
# 
# 1. Cree un script para mostrar los primeros 100 números enteros positivos, comenzando desde el 1
# 

# numero = 0
# contar = 0  
# while numero != 100:
#        numero = numero + 1
#        contar = contar + 1 
#        print(contar,"- Numero",numero)


# 2 Modifique el script del ejercicio anterior para que se muestren sólo los números pares. Para saber si un número es par, utilice el operador de módulo (%).

# numero = 0
# contar = 0
# while numero != 100:        
#     numero = numero + 1
#     numero_par = numero % 2

#     if numero_par == 0:
#         print("Numero par --->",numero)
#     else:
#         print("Numero impar",numero)

# 3 Cree un script para calcular el resultado de sumar los números desde el 75 al 150 = 8550

# sumatoria = 0
# inicio = False
# fin = False

# while not(inicio) and not(fin):
#     inicio = 75
#     fin = 150
#     cantidad = 76
#     sumatoria = (cantidad * (inicio + fin)) // 2
#     print( "La sumatoria desde el 75 al 150 es:",sumatoria)

# 4 Cree un script que le solicite al usuario ingresar un número entero, y muestre en pantalla el factorial de dicho número. NOTA: puede obviar la validación en este ejercicio, 
# pero recuerde que la función range no incluye al valor máximo enviado como parámetro. factorial de n = n! = 1 * 2 * 3 * … * (n - 1) * n
#tengo que simular la estructura de repeticion for, para lograr multiplicar 1*2*3*4*5*6*...(n-1)*n
print("die Anwendung muß sterben")

print("Fakultät einer Zahl")

inicio = 1 
factorial = False
while not(factorial): 
    numero = int(input("Ingresar un numero entero: "))

#Estructura de desición que calcula la distancia entre el número ingresado y cero

    if numero < 0: 
        valor_absoluto = -numero 
        print(valor_absoluto) 
    else:
        valor_absoluto = numero
        print(valor_absoluto)

# Gegenlogik:
#este contador -(GENERA LA TABLA DE MULTIPLICAR DEL NUMERO QUE SE INGRESE)-

    contador = 0
    start = True
    while start:
        contador = contador + 1
        if contador == 100:
            start = False
        
        factorial = numero * contador
        print("esto es contador --->",contador, "esto es Factorial --->", factorial)




#cantidad_numeros = cantidad_numeros + 1

# for j in range(1,factorial):

#     factorial = numero * j

# print( "factorial--->:",factorial)




# x = int(input("ingresar un numero: "))


#die Kreatur muß sterben

# 4 Cree un script que le solicite al usuario ingresar un número entero, y muestre en pantalla el factorial de dicho número. NOTA: puede obviar la validación en este ejercicio, 
# pero recuerde que la función range no incluye al valor máximo enviado como parámetro. factorial de n = n! = 1 * 2 * 3 * … * (n - 1) * n


# numero = int(input("Ingresar un numero entero: "))




