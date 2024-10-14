# leer un numero entero de tres digitos y detemninar si alguno de sus digitos es igual a la suma de los otros dos
num=int(input('ingrese un numero de tres  digitos:'))
n1=num//100
n2=num%100//10
n3=num%10
print(n1,n2,n3)# imprimen los numeros y se separan
if(n1== (n2 + n3)):# se empiezana sumar las variables 
    print("La suma de los dos ultimos numeros es igual al primer número")
if(n2==(n1+n3)):
    print("la suma de los digitos es igual a ultimo numero.")    
if(n3==(n1+n2)):
    print(" la suma de los numeros es igual al segundo numero")  
else:
    print("no se suman")
