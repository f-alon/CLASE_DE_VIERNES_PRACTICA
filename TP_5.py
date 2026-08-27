'''1. Cree una función que reciba dos números como parámetro, y muestre en
pantalla la suma aritmética de ambos. Invoque a la función con dos números
leídos desde teclado
2. Modifique el script del ejercicio anterior para que la función retorne el resultado
en vez de mostrarlo. El programa debe seguir mostrando el resultado en
pantalla
3. Cree una función que reciba un string como parámetro, y retorne la cantidad de
letras que posee. Luego, utilice la función para escribir un programa que solicite
ingresar el nombre del usuario, y luego muestre en pantalla cuántas letras tiene
ese nombre.

4. Cree una función que reciba dos números como parámetro (base y exponente),
y retorne el resultado de elevar base a la potencia exponente

5. Cree una función que reciba un string como parámetro, y retorne el mismo
string, pero con todas las letras convertidas a mayúsculas.

6. Modifique la función del ejercicio anterior para que retorne dos versiones del
string recibido como parámetro: primero la versión en minúsculas, y luego la
versión en mayúsculas

7. Cree una función que reciba dos string como parámetro (nombre1 y nombre2),
y retorne True si nombre1 tiene más letras que nombre2, o False en caso
contrario

8. Cree un archivo llamado modulo_cadena.py; dentro de él, cree una función
llamada leer_cadena que, sin recibir ningún parámetro, le solicite al usuario leer
un string cualquiera, y luego lo retorne. Luego cree otro archivo llamado
programa_principal.py, que ejecute el programa haciendo uso de la función
creada en el otro archivo.
'''
#funcion que retorna la suma entre a y b
def dos_numeros(a,b):
    resultado = a+b 
    return resultado

#funcion que cuenta la cantidad de letras del nombre que ingresa el usuario
def cantidad_letras(letras):
    return len(letras)

# (EJE 4) funcion que retorna el resultado de la potenciacion 
def potencia(base,exponente):
    pote = base ** exponente
    return pote

#9. Cree un test unitario para el ejercicio 4. Utilice al menos 3 casos con distintos
    #parámetros.
    
def test_potencia():
    assert potencia(2,3) == 8
    assert potencia(3,3) == 27
    assert potencia(4,2) == 16

    print("PASO!!")
    print("PASO!!")
    print("PASO!!")


def mayusculas(cadena):
    conv_min = cadena.lower()
    conv_may = cadena.upper()
    return conv_min,conv_may

def compara_long(nombre1,nombre2):
    mayor_letras = False
    if len(nombre1) > len(nombre2):
        mayor_letras = True
    return mayor_letras


def main():
    numero1 = int(input("Ingresar un numero: "))
    numero2 =  int(input("Ingresar otro numero: "))
    resultado1 = dos_numeros(numero1,numero2)
    print("El resultado es: ", resultado1)

    resultado2 = potencia(numero1,numero2)
    print("El resultado de la potenciacion es: ", resultado2)

    nombre = input("Ingresar un nombre para contar cuantas letras posee: ")
    letras_nombre = cantidad_letras(nombre)
    print("El nombre posee: ",letras_nombre,"letras")
    nombre_mayus = mayusculas(nombre)
    print("Su nombre todo en minusculas y mayusculas:",nombre_mayus)

    nombre1 = input("Ingresar un nombre: ")
    nombre2 = input("Ingresar un nombre: ")
    mas_largo = compara_long(nombre1,nombre2)
    print("Es mas largo: ",mas_largo)

    test_potencia()

main()






