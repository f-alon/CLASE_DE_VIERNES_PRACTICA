#1. Cree un script que almacene un número entero en una variable, y luego muestre en pantalla su valor absoluto, con el mensaje 
# “El valor absoluto de N es |N|”. Finalmente, verifique que su programa funciona correctamente, ejecutándolo con el valor 10 en 
# la variable (la salida debería ser 10), y luego con el valor -10 (la salida debería ser 10 nuevamente).

numero = int(-10)
print("El valor absoluto de ",numero, "es", abs(numero))
print(f"El valor absoluto de |{numero}| es {abs(numero)}")

# Cree un script que almacene su nombre de pila en una variable, y luego muestre en pantalla la cantidad de letras de ese nombre,
#  con el mensaje “El nombre [NOMBRE] tiene [N] letras.”

nombre = "Felipe"

print(f"El nombre {nombre} tiene {len(nombre)} letras")


# Cree un script que almacene, en dos variables, una base y un exponente, y
# luego muestre en pantalla el resultado de elevar el número base a la potencia exponente.

base = 3
exponente = 2
resultado = base ** exponente
print("resultado de la potencia --->",resultado)

# Implemente un algoritmo en Python para calcular el perímetro de un rectángulo, conociendo su base y altura. 
# Los datos se deben almacenar en variables, y el resultado se debe mostrar en pantalla.
# perímetro = 2 * (base + altura)

base = 3
altura = 2
perimetro = 2 * (base + altura)
print("perimetro del rectangulo--->",perimetro)

# Implemente un algoritmo en Python para calcular el área de un rectángulo, conociendo su base y altura. Los datos se deben almacenar
# en variables, y el resultado se debe mostrar en pantalla.
# área = base * altura

base = 3
altura = 2
area = base * altura
print("area del rectangulo -->",area)

# Implemente un algoritmo que intercambie los valores entre dos variables a y b cualesquiera. 
# Por ejemplo, si a = 10 y b = 5, luego de ejecutar el algoritmo, la variable "a" debería ser igual 5, y la variable "b" debería 
# ser igual a 10.

a = 5
b = 10
numero_b = a #numero_b es una variable que almacena de forma temporal el valor de a
a = b # ahora a puede tomar el valor de b
b = numero_b # y b puede tomar el valor que se almaceno de forma temporal en numero_b
print(a,b) # se muestra en pantalla los valores intercambiados

'''
Si no quisiera utilizar una variable temporal simplemente se escribe-:
    a,b = b,a
    print(a)
    print(b)

En Python, la asignación múltiple permite crear y dar valores a varias variables en una sola línea de código, 
separando los nombres y los valores con comas Por ejemplo: a, b, c = 1, 2, 3
Formas de uso: 
    
    Distintos valores: x, y, z = "Hola", 5, True
    
    Mismo valor: a = b = c = 10
    
    Intercambiar valores: a, b = b, a (sirve para rotar variables sin usar una auxiliar)
    

'''
'''Escriba un algoritmo que, conociendo las notas de los dos parciales de un alumno de la asignatura Introducción a la Programación, muestre en pantalla su promedio.'''

nota1 = 10
nota2 = 9
promedio = (nota1 + nota2) / 2
print("Promedio--->", promedio)


'''
Cree un script que, sabiendo cuántos pesos argentinos tiene una persona ahorrada en su cuenta (almacenando ese monto en una variable), muestre
en pantalla los montos convertidos en dólares (U$1 = $80.5), reales ($R1 =$14.1), y euros (€1 = $69.5). La salida del programa debe tener el siguiente
formato:
Usted tiene $XXX pesos argentinos, los cuales se convierten en:
- U$XXX dólares.
- R$XXX reales.
- €XXX euros.

'''
ahorros = 1500000
precio_dolar = 1475
precio_real = 14
precio_euro = 69

print(f"Usted tiene {ahorros} pesos argentinos, los cuales se convierten en: ")
print(f"U${ahorros / precio_dolar} dolares")
print(f"R${round(ahorros / precio_real)} reales")
print(f"€${round(ahorros / precio_euro)} euros")