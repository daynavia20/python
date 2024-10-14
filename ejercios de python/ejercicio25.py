#leer un numero entero de cautro digitos y determinar cuantos digitos pares tiene .
num=int(input("Ingrese un numero de cuatro digitos:"))
n_mil=num//1000
n1_cent=(num//100)%10
n2_decen=(num//10)%10
n3_uni=num%10
print(n_mil,n1_cent,n2_decen,n3_uni)
contador=0
if(n_mil%2==0):#operacion a la variable 
    contador=contador+1
if(n1_cent%2==0):  
    contador=contador+1
if(n2_decen%2==0):  
    contador=contador+1   
if(n3_uni%2==0):  
    contador=contador+1 
if(contador>0):    
   print(f"el numero {num} tiene {contador} digitos pares.") 
else:
    print("el numero no tiene digitos pares.")  
if(n_mil%2==0 and n1_cent%2==0):
    print("dos numeros pares")# otra logica 