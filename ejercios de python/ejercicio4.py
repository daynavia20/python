#leer un numero entero de dos digitos y determinar a cuanto es igual la suma de sus digitos
import math 
num=int(input('digite un numero de dos digitos: '))#se pide sl total de numeros que se van a necesitar
num1=math.trunc(num/10)# se hace la division para que de el resultado 
num2=math.trunc(num%10)# se saca el residuo con el mod 
suma=num1+num2# se da la orden para la suma de los numeros 
print(suma)# proceso para irmprimir el resultado 
