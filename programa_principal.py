'''8. Cree un archivo llamado modulo_cadena.py; dentro de él, cree una función
llamada leer_cadena que, sin recibir ningún parámetro, le solicite al usuario leer
un string cualquiera, y luego lo retorne. Luego cree otro archivo llamado
programa_principal.py, que ejecute el programa haciendo uso de la función
creada en el otro archivo.'''

from modulo_cadena import leer_cadena as lc

def main():

    lc()

if __name__ == '__main__':

    main()