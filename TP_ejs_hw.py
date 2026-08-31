# Cree una función que recibe un número entero, entre 1 y 12, correspondiente a un mes y retorna un string, con el nombre de la estación. Considera la 
# relación entre números y estaciones de la siguiente forma: 

# 1, 2, 3: "Verano",
# 4, 5, 6: "Otoño", 
# 7, 8, 9: "Invierno", 
# 10, 11, 12: "Primavera"

def season(numero):
    if numero == 0 or numero > 12: 
        season_name = "no valido"
        print(season_name)
    else:
        if numero >= 1 and numero <= 3:
            season_name = "Verano"
        elif numero >= 4 and numero <= 6:
            season_name = "Otoño"
        elif numero >= 7 and numero <= 9:
            season_name = "Invierno"
        else:
            numero >= 10 and numero <= 12
            season_name = "Primavera"
    return season_name


# Cree una función que recibe dos string como parámetro(a,b), y retorna un string con 
# la leyenda "Gana a", si el string a tiene mayor cantidad de caracteres que el string b.
# Si el string b tiene mayor cantidad de caracteres que el string a, debe retornar "Gana b".
# Si ambos strings tienen la misma cantidad de caracteres, debe retornar "Empate".

def quien_gana(a,b):
    if len(a) == len(b):
        ganador = "Empate"
    else:
        if len(a) >= len(b):
            ganador = "Gana Player 1"
        else:
            len(a) <= len(b)
            ganador = "Gana Player 2"
    return ganador

# Crear una función que recibe dos números de parámetro, y realiza la resta de ambos. 
# ( a - b)
# Si el resultado de la resta es mayor a 0, debe retornar true, caso contrario, debe
# retornar false.

def dos_numero(a,b):
    resta = (a-b)
    if resta > 0:
        resultado = True
    else:
        resultado = False
    return resultado

def main():
    print("¿Estación del año?")
    numero = int(input("Ingresar un numero: "))
    estacion = season(numero)
    print(estacion)

    print("¿Quien gana?")
    palabra1 = input("Player 1: Ingresar una palabra: ")
    palabra2 = input("Player2: Ingresar una palabra: ")
    ganador = quien_gana(palabra1,palabra2)
    print(ganador)

    print("Dos números")
    numero1 = int(input("Ingresar el primero número: "))
    numero2 = int(input("Ingresar el segundo número: "))
    resultado = dos_numero(numero1,numero2)
    print(resultado)



main()

