#leer un numero de dos digitos y deteminar si es primo y ademas si es negativo
#  los numero negativos son menores que 0 y los positivos son mayores que 0 
num=int(input('Ingrese un numero:'))
if (num<0):# es la condicion para saber si un numero es negativo o positivo 
    print("es un numero negativo")
else:
    cont=0
    print(" es un numero positivo")
    for i in range(2,num):
      if ( num%i==0):
         cont=1
    if (cont==0):#numeros primos 
        print("su numero es primo")
    else:
        print("su numero no es primo")







