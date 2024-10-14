#leer un numero de dos digitos menor que 20 y deteminar si es primo
# un numero primo se diferencia de si mismo si de divide entre 1 y el mismo
num=int(input('Ingrese un numero:'))
if (num<20):#numero menor que 20
    cont=0
    for i in range(2,num):# empieza en 2 porque todos los numero se dividen por 1 y el -1 para que sea divisible entre el mismo
        if ( num%i==0):# i se divide con el numero 
            cont=1#se coloca el valor de contador 
    if (cont==0):#contador va ser verdadero 
        print("su numero es primo")
    else:
        print("su numero no es primo")


   
