'''
1. Cree un script que, al ejecutarlo, le solicite al usuario ingresar su nombre de
pila, luego lo salude y calcule la cantidad de letras del nombre, mostrando
el mensaje “Hola, [NOMBRE], tu nombre tiene [N] letras.”.

'''

nombre_pila = input("Cual es tu nombre? ")
contador_letras = len(nombre_pila)

print(f"HOLA!! {nombre_pila}, tu nombre tiene {contador_letras} letras")

'''
2. Cree un script que lea dos números enteros por teclado, y luego muestre en pantalla el resultado de la suma entre ellos.
'''

n1 = int(input("Ingresar un numero: "))
n2 = int(input("Ingresar otro numero: "))

resultado = n1 + n2

print("Este es el resultado ---> ", resultado)


'''3. Cree un script que muestre en pantalla el perímetro de un rectángulo, leyendo su base y altura desde teclado. perímetro = 2 * (base + altura)'''

base = float(input("Ingresar el valor de la base: "))
altura = float(input("Ingresar el valor de la altura: "))

perimetro = 2 * (base + altura)

print(perimetro)

'''4. Cree un script que le solicite a un alumno ingresar su apellido, la nota del primer parcial, y la nota del segundo parcial. Finalmente, se debe mostrar
un reporte con la siguiente información

Alumno [APELLIDO]
- Primer parcial: [NOTA1]
- Segundo parcial: [NOTA2]
- Promedio: [PROMEDIO]
''' 
apellido = input("Ingresa tu apellido: ")
nota1 = int(input("Ingresa la nota del primer parcial: "))
nota2 = int(input("Ingresa la nota del segundo parcial: "))
promedio = (nota1 + nota2) / 2
print(f"Alumno: -{apellido}- \n Primer parcial: {nota1} \n Segundo parcial: {nota2} \n Promedio {promedio}")



'''5. Cree un script que lea dos números de teclado (una base y un exponente) y
luego muestre en pantalla el resultado de elevar el número base a la
potencia exponente.'''

base = int(input("Ingresar la base: "))
exponente = int(input("Ingresar el exponente: "))
resultado = base**exponente
print(resultado)