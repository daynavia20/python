#leer tres numeros enteros y determinar cual es el mayor, usando dos variables 
num1=int(input('Ingrese el primer numero:'))
num2=int(input(" ingrese el segundo numero"))#se pide el numero
num3=int(input(" ingrese el tercer numero"))
may=num1#primer numero mayor
if num2>may:# se compara el segundo numero 
    may=num2
if num3>may:#se compara el tercer numero
    may=num3    
print(f"el numero mayor de los tres es: {may}")    