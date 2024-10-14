#leer un numero entero de dos digitos y determinar si sus digitos son primos 
import math
num=int(input('Ingrese un numero:'))
numero= math.trunc(num/10)
numero2= math.trunc(num%10)# se separan los numeros
cont=0
for i in range(2,numero):
    if ( numero%i==0):# primer numero priumo 
         cont=1
if (cont==0):#numeros primos 
    print("su numero es primo")
else:
     print("su numero no es primo")

cont=0
for i in range(2,numero2):
    if ( numero2%i==0):# segundo numero primo 
         cont=1
if (cont==0):#numeros primos 
    print("su numero es primo")
else:
     print("su numero no es primo")
