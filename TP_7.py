#Estructuras repetitivas incondicionales:
#ciclo definido
# sintaxis
#   for <variable> in <(iterable)>:
# for i in ("hola"):
#     print(i)


#otra forma

# palabra = "hsdsafosalaasfsahjaklalag"
# contador = 0 
# for i in palabra:
#     if i == "a":
#         contador = contador + 1
#     #print("a")

# print(contador)

# range es un instruccion que se le da a python y este genera una lista de elementos
# 



# b = 1
# a = 3 > 1
# while a:
#     b = b + 1
#     print("hola!")
#     a = 3 > b # el bucle se repite dos veces




# 1 Cree un script para mostrar los primeros 100 números enteros positivos, comenzando desde el 1

# print(f"Estos son los primeros 100 numeros enteros positivos:")
# for i in range(1,101):
    
#     print(i)


# 2 Modifique el script del ejercicio anterior para que se muestren sólo los números pares. Para saber si un número es par, utilice el operador de módulo (%).



# for i in range(1,101):

#     numero_par = i % 2
#     if numero_par == 0:
#         print("Numero par --->",i)

# print("######################################################################################################################################################")
# for i in range(1,101):

#     numero_par = i % 2
#     if numero_par != 0:
#         print("Numero impar ---->",i)

# 3 Cree un script para calcular el resultado de sumar los números desde el 75 al 150

sumatoria = 0
for j in range(75,151):
    sumatoria = sumatoria + j

print( "La sumatoria desde el 75 al 150 es:",sumatoria)

    
# 4 Cree un script que le solicite al usuario ingresar un número entero, y muestre en pantalla el factorial de dicho número. NOTA: puede obviar la validación en este ejercicio, pero recuerde que la función range 
# no incluye al valor máximo enviado como parámetro. factorial de n = n! = 1 * 2 * 3 * … * (n - 1) * n
