# leer un numero entero de tres digitos y determinar cuantos digitos primos tiene.
num=int(input('Ingrese un numero de tres digitos:'))
digito_centenas = num // 100 #se sacan las dentenas 
digito_decenas = (num // 10) % 10#se sacan las decenas 
digito_unidades = num % 10#se sacan las unidades 
cont_pri= 0# se hace un contador 
if (digito_centenas):
    print("es primo")
    cont_pri += 1
if (digito_decenas):
    print("es primo")# Contar los dígitos primos
    cont_pri += 1
if (digito_unidades):
    print("es primo")
    cont_pri += 1
print(f"El número {num} tiene {cont_pri} dígito(s) primo(s).")# Mostrar el resultado
