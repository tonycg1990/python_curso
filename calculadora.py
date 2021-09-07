def ingreso():
    global a,b
    a=int(input("Ingrese primer numero: "))
    b=int(input("Ingrese segundo numero: "))
def suma():
    print ("El resultado es; ", a+b)
    input()
def resta():
    print ("El resultado es; ", a-b)
    input()
def multiplicacion():
    print ("El resultado es; ", a*b)
    input()
def division():
    if (b==0):
        print ("No se puede dividir en 0")
        input()
    else:
        print ("El resultado es; ", a/b)
        input()
    
while(True):
    print ("1 Suma")
    print ("2 Resta")
    print ("3 Multiplicación")
    print ("4 División")
    opcion=int(input("Ingrese opcion: "))
    if(opcion==1):
        ingreso()
        suma()
    
    elif(opcion==2):
        ingreso()
        resta()
        
    elif(opcion==3):
        ingreso()
        multiplicacion()
        
    elif(opcion==4):
        ingreso()
        division()