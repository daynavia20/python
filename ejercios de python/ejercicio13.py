#leer un numero entero de 3 digitos y determinar a cuanto es igual la suma de sus digitos.
num=int(input('Digite un número de tres digitos:'))
n1=num//100#se divide para que de le resultado
n2=(num//10)%10# dividimos el numero y le sacamos el mod 
n3=num%10#residuo del mod
suma=n1+n2+n3#se da la orden para hacer la suma 
print(suma)#imprime resultado 




