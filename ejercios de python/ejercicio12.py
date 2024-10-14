#leer dos numero enteros de dos digitos y determinar si la suma de los dos numeros origina un par.
n1 = int (input('Digite un número de dos digitos:'))
n2 = int (input('Digite un número de dos digitos:'))
a=n1+n2 #un numero par es cuando se divide entre 2 y el residuo es 0
if (a%2==0):
    print("el numero es par")
else:
    print("el numero no es par")


