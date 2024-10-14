#leer un numero entero menor que 50 y positivo y determinar si es un numero primo 
num=int(input("Ingrese un numero:"))
if(num<50 and num>0):
    contador=0
    for i in range (2,num):
        if (num%i==0):
            contador=1
    if (contador==0 ) :
        print("el numero es primo")  
    else:
        print("el numero no es primo.") 
else:
    print("el numero es negativo o mayor a 50")                
        

