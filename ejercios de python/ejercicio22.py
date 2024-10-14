#leer un numero entero de tres digitos y determinar cuantos digitos  pares tiene
import math
num=int(input('ingrese un numero de tres  digitos:'))
n1=math.trunc(num/100 )# se vivide por el total de numeros
a=math.trunc(num%100)#se coloca otra variable 
n2=math.trunc(a/10)#va a ser igual a la  variable a dividivo 10 
n3=math.trunc(a%10)# se saca el resultado 
if(n1%2==0 or n2%2==0 or n3%2==0):#se hace la comparacion 
    print('tiene digitos pares')
else:
    print('no tiene digitos pares')

