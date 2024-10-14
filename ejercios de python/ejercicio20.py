#leer un numero entero de tres digitos y determinar si el primer digito es igual al ultimo.
num=int(input('Ingrese un numero de tres digitos:'))
dig_cent=num//100# se extraen los digitos 
dig_uni=num%10
if (dig_cent==dig_uni):#se comparan los digitos 
    print(f"el primer digito {dig_cent} es igual al ultimo digito {dig_uni}.")
else:
    print(f"el primer digito {dig_cent} no es igual al ultimo digito {dig_uni}")    
