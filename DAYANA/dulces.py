productos = {
    "ponque" : 3000,
    "papas" : 4000,
    "chocolate" : 1000,
    "arequipe" : 2500
}
with open("productos.txt", 'a') as archivo2: 
    for producto in productos:
        mensaje = "El producto disponible es: " + producto + "\n"
        archivo2.write(mensaje)

with open("productos.txt", 'r') as archivo3:
    datos = archivo3.read()
    print(datos)
menu = """
1) Mostrar productos
2) Comprar producto
3) Insertar dinero
0) Salir del programa
"""
print(menu)
saldo = 0
while True:
    opcion = int(input("Ingrese una opcion a realizar:  "))
    if opcion == 1:
        print("Los productos de la maquina son:  ")
        for producto, precio in productos.items():
            print(f"{producto}: ${precio}")
    elif opcion == 2:
        producto = input("¿Qué artículo desea comprar? ").strip().lower()
        if producto in productos:
            precio_producto = productos[producto]
            if saldo < precio_producto:
                print("No hay saldo suficiente, recargue saldo.")
            else:
                saldo -= precio_producto
                print(f"saldo : {saldo}")
                print(f"Gracias por confiar en nosotros")
        else:
            print("Producto no disponible.")
    elif opcion == 3:
        recarga = int(input("¿Desea recargar? "))
        if recarga < 0:
            print("Ingrese un valor para la recarga.")
        else:
            saldo += recarga
            print(f"Saldo recargado. Saldo : ${saldo}")
    elif opcion == 0:
        print("Gracias por usar la máquina.")
        break
    else:
        print("Opción invalida, seleccione una opción válida del menú.")




