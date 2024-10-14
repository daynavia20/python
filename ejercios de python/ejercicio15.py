#leer un numero entero de tres digitos y determinra en que posicion esta el mayor digito 
num=int(input('Ingrese un numero de tres digitos :'))
#extarer los digitos 
n1=num//100#se divide para que de le resultado
n2=(num//10)%10# dividimos el numero y le sacamos el mod 
n3=num%10#residuo del mod
nmay=max(n1,n2,n3)#econtrar digito mayor 
if nmay==n1:#encotrar la poscion de cada numero para asi mismo mostrar en pantalla 
    posicion=" pimer numero "
elif nmay==n2:   
    posicion=" segundo numero "
else:
    posicion=" tercer numero"    
print( f"el digito mayor es {nmay} y esta en la posicion:{posicion}") #se muestra en panatala la poscion 
#de cada numero y cual es el mayor de ellos   


