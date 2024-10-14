#leer un numero entero de 3 digitos y determinar si almenos 2  de sus digitos son iguales 
num=int(input('Ingrese un numero de tres digitos:'))

n1= int(num/100)#se divide para que de le resultado
n2=int((num/10)%10)# dividimos el numero y le sacamos el mod 
n3=num%10#residuo
if(n1==n2 or n1==n3 or n2==n3): #se hace la condicion O
    print(" dos de sus digitos son iguales")
else:
    print("no hay digitos iguales")