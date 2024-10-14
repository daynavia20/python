#leer un numero entero y mostrar todos los enteros comprendidos entre 1 y numero leido.
num= int(input("Ingrese un numero: "))
if num<=0:
    print("el numero debe ser positivo.")
else:
    print("los numeros comprendidos entre 1 y ",num, "son:")
    for i in range(1,num+1):
        print(i)
