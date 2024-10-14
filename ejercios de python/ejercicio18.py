#leer tres numero enteros y mostrarlos en forma ascendente 
num1=int(input('Ingrese el primer numero:'))
num2=int(input(" ingrese el segundo numero:"))#se pide el numero
num3=int(input(" ingrese el tercer numero:"))
#secunecia de menor a mayor 
if (num1<=num2<=num3):
    print(f"los numeros ordenados ascendentemente son:{num1},{num2},{num3}")
elif num1 <= num3 <= num2:
    print(f"Los números ordenados ascendentemente son: {num1}, {num3}, {num2}")
elif num2 <= num1 <= num3:
    print(f"Los números ordenados ascendentemente son: {num2}, {num1}, {num3}")
elif num2 <= num3 <= num1:
    print(f"Los números ordenados ascendentemente son: {num2}, {num3}, {num1}")
elif num3 <= num1 <= num2:
    print(f"Los números ordenados ascendentemente son: {num3}, {num1}, {num2}")
else:
    print(f"Los números ordenados ascendentemente son: {num3}, {num2}, {num1}")    
