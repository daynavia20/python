
menu="""
1). calcular area y perimetro del cuadrado.
2). calcular el area y perimetro del triangulo.
3). calcular el area y perimetro del rectangulo.
4). calculara el area y perimetro del circulo.
0). fin programa
"""
print(menu)
while True:
    option=int(input("Digite la opcion que desea: "))

    if option ==1:
        lados=int(input("Digite el tamaño del lado del cuadrado: "))
        area = lados*lados
        perimetro = lados*4
        print(f"el area del cuadrado {area}, perimetro del cuadrado {perimetro}")
    elif option == 2:
        base=int(input("Digite la base del triangulo: "))
        altura=int(input("Digite la altura del triangulo: "))
        altura2=int(input("Digite la segunda altura del triangulo: "))
        area=altura*base
        perimetro= base+altura+altura2
        print(f"el area del triangulo {area}, perimetro del triangulo {perimetro}")
    elif option ==3:
        base=int(input("Digite la base del rectangulo: "))
        altura=int(input("Digite la altura del rectangulo: "))
        area=base*altura
        perimetro=2*(base+altura)
        print(f"el area del rectangulo {area}, perimetro del rectangulo {perimetro}")
    elif option== 4:
        circuferencia=int(input("Digite el radio del circulo: "))
        area = 3.14 * circuferencia**2.
        perimetro= 2*3.14* circuferencia
        print(f"el area del circulo {area}, el perimetro del circulo {perimetro}")
    elif option == 0:
        print("programa finalizado ")
        break
    else:
        print("opciones invalidas")
        
        



    



    

        

