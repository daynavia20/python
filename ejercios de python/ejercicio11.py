#ler dos números enteros de dos digitos y determinar si tienen digitos comunes. 

n1 = int (input('Digite un número de dos digitos:'))
n2 = int (input('Digite otro número de dos digitos:'))
a = int(n1 / 10)
b = n1 % 10 
c = int(n2 / 10)
d = n2 % 10 
e = 0
print(a , "-" , b, "-", c, "-", d)#se imprimen los numeros

if( a == c ): print("los digitos tienen en comun el número: ", a)
else: e = e + 1

if( a == d): print("los digitos tienen en comun el número: ", a) 
else: e = e + 1

if( b == c): print("los digitos tienen en comun el número: ", b)
else: e = e + 1

if( b == d): print("los digitos tienen en comun el número: ", b)
else:  e = e + 1

if(e == 4): print("No hay números comunes")# en caso de que no tenga digitos comunes se hace negacion 

