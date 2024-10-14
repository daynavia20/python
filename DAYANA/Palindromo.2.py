#pal=input("Ingrese un cadena de caracteres: ")

# contador=0
# while True:
#     if pal[0]== pal[-1]:
#         contador+=1
#         break 
#     else:
#         print("Carateres no palindromos")  
#         break 
# if contador==1:
#     print("Carater palindromo ")

pal=input("Ingrese un cadena de caracteres: ")

if pal == pal[::-1]:
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")








