#leer un numero entero de dos digitos y determinar si ambos digitos son pares
import math# se llama la carpeta de suma
num=int(input('ingrese un numero de dos digitos:'))# se pide el total de numeros
num1=math.trunc(num/10)# se hace la division para que de el resultado 
num2=math.trunc(num%10)# se saca el residuo con el mod 
if (num1%2==0 and num2%2==0):# se dividen los numeros entre 2 para saber si el residuo es 0, con una decicion en Y para que den si o si numero pares
    print('los digitos son pares')
else:
    print('los digitos no son pares')    