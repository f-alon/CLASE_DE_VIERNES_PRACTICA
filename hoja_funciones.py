# ESTE ARCHIVO CONTIENE FUNCIONES GENERICAS, USAR TENIENDO EN CUENTA ESO ---- SON GENERICAS ----

# en python elevar un número a 1/2 o 0.5 da como resultado su raíz cuadrada
#funcion para sacar raiz cuadrada de un numero recibe un numero n como parametro (invocar con raiz_cuadrada(n)):

def raiz_cuadrada(n):
    
    raiz = n**0.5
    return raiz

# OJO: funcion mas que generica que calcula el volumen de un cilindro: (recibe el radio y la altura como parametros)

def volumen_cilindro(radio,altura):

    pi =  3.141516
    volumen = (pi * radio**2) * altura
    return volumen

# funcion generica para calcular el perimetro de un rectangulo
def per_rectangulo(base,altura):
    perimetro = 2 * (base + altura)
    return perimetro

# Funcion generica que permite determinar el área y perímetro de un triángulo equilátero
def per_triangulo_equi(lado):
    perimetro = 3 * lado
    return 3 * lado


#funcion generica para calcular el Area de un triangulo escaleno(usar si se conoce un lado (b) y la altura (h) asociada a dicho lado)
# area = (b*h)/2

def area_triang_esc(base,altura):
    area = (base * altura) / 2
    return area


# Funcion generica para calcular radio inscrito (circulo interior) de un triangulo escaleno. Recibe dos parametros:
# a = el area del triangulo y s = el semiperimetro, que se calcula sumando los tres lados y dividiendo entre 2

def inscrito(a,s):
    radio_ins = a/s
    return radio_ins

# Funcion generica para calcular radio circunscrito (circulo exterior) de un triangulo escaleno. 
# (recibe como parametro las longitudes de los tres lados y el area total del triángulo)

def circunscrito(l1,l2,l3,area_total):
    radio_circ = (l1+l2+l3)/4*area_total
    return radio_circ