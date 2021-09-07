import sys

p1 = 0
p2 = 0

menu = """
1.- Sumar
2.- Restar
3.- Multiplicar
4.- Dividir
5.- Potencia
6.- Raiz
9.- Salir
"""

def Sumar():
    print("Ingresa el primer sumando: ")
    p1 = float(input())
    print("Ingrese el segundo sumando: ")
    p2 = float(input())
    print("El resultado es: ", p1 + p2)
    
def Restar():
    print("Ingresa el primer minuendo: ")
    p1 = float(input())
    print("Ingrese el segundo sustraendo: ")
    p2 = float(input())
    print("El resultado es: ", p1 - p2)
    
def Multiplicar():
    print("Ingresa el primer coefinciente: ")
    p1 = float(input())
    print("Ingrese el segundo coeficiente: ")
    p2 = float(input())
    print("El resultado es: ", p1 * p2)
    
def Dividir():
    print("Ingresa el primer Dividendo: ")
    p1 = float(input())
    print("Ingrese el segundo Divisor: ")
    p2 = float(input())
    print("El resultado es: ", p1 / p2)
    
def Potencia():
    print("Ingresa el primer base: ")
    p1 = float(input())
    print("Ingrese el segundo exponente: ")
    p2 = float(input())
    print("El resultado es: ", p1 ** p2)
    
def Raiz():
    print("Ingresa el primer radicando: ")
    p1 = float(input())
    print("Ingrese el segundo indice: ")
    p2 = float(input())
    print("El resultado es: ", p1 ** (1/p2))


while True:
    print(menu)
    opc = int(input())
    if opc == 1:
        Sumar()
    elif opc ==2:
        Restar()
    elif opc ==3:
        Multiplicar()
    elif opc ==4:
        Dividir()
    elif opc ==5:
        Potencia()
    elif opc ==6:
        Raiz()
    elif opc == 9:
        sys.exit()
