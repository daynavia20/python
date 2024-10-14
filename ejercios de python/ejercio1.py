#leer un numero entero y determinar si es un numero terminado en 4 
num=int(input('digite un numero: '))
a=num%10#en este paso todo numero dividido mod 10 da el ultimo digito  
if (a==4):# es una comparacion para ver si el numero si da 4 
    print('el numero termina en 4')# si es correcto muestra este contendio 
else:
    print('el numero no termina en 4')#si no es correcto
    