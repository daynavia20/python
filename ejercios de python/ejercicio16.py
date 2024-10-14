#leer un numero de tres digitos y determnira si algun digito es multiplo de los otros 
num=int(input('Ingrese un numero de tres digitos :'))
n1=num//100#se divide para que de le resultado
n2=(num//10)%10# dividimos el numero y le sacamos el mod 
n3=num%10#residuo del mod
#se verifica si los digitos son mulyiplos de los otros 
if(n1%n2==0 or n1%n3==0):
    print(f"el digito {n1} es multiplo de los otros digitos" )
elif( n2%n1 ==0 or n2%n3==0): #proceso para saber si los njmeros son multiplos 
   print(f"el digito {n2} es multiplo de los otros digitos.")# todo  numero es multiplo de si mismo 
elif(n3%n1==0 or n3%n2==0):
    print(f"el digito {n3} es multiplo de los otros numeros") # los multiplos son numero que se obtiene al multiplicar 2 numeros enteros   
else:
    print("ninguno es multiplo de el otro")    


    