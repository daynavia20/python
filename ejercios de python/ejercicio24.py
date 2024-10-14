#leer un numero entero de cuatro digitos y determinar a cuanto es igual la suma de sus digitos 
n=int(input("Ingrese un numero de cuatro digitos:"))
n1_mil=n//1000# 
n2_cen=(n//100)%10#se dividen y se saca el mod de cada variable 
n3_dece=(n//10)%10
n4_uni=n%10
suma=(n1_mil+ n2_cen+ n3_dece+ n4_uni)# se calcula de una forma mas facil las suma
print(f"las suma de los digitos {n} es {suma}")