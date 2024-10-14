# leer un numero entero de dos digitos y determinar si los digitos son iguales 
import math
num=int(input('Ingrese un numero:'))
num1=math.trunc(num/10)# se hace la division para que de el resultado 
num2=math.trunc(num%10)# se saca el mod 
if (num1==num2):
    print("sus digitos son iguales")
else:
    print("sus digitos no son iguales")
