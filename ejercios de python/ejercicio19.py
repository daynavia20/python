 # leer tres numeros enteros de dos digitos cada unoy determninar en cual de ellos se encuentra el mayor digito
num1=int(input('Ingrese el primer numero de dos digitos :'))
num2=int(input(" ingrese el segundo numero de dos digitos:"))#se pide el numero
num3=int(input(" ingrese el tercer numero de dos digitos:"))
d1_n1=num1//10#extraer los digitos de caada numero 
d2_n1=num1%10

d1_n2=num2//10#extraer los digitos de caada numero 
d2_n2=num2%10

d1_n3=num3//10#extraer los digitos de caada numero 
d2_n3=num3%10
mayd=max (d1_n1,d2_n1,d1_n2,d2_n2,d1_n3,d2_n3)#sacar el digito mayor 
print(f"el mayor digito de los numeros {num1} , {num2} y {num3} es {mayd}")



