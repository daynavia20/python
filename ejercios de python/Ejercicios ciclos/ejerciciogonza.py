inventario = [] # variable para realizar el inventario
def agregar_producto():#definicion de la variable 
    nombre = input("ingrese el nombre del producto: ")#
    cantidad = input("ingrese la cantidad disponible: ")
    precio = input("ingrese el precio del producto: ")
    producto = {"nombre":nombre, "cantidad": cantidad, "precio": precio}
    inventario.append(producto)#se utiliza el append para agragra a la lista 
    print("producto agregado al inventario.")

def actualizar_cantidad():
    nombre = input("ingrese el nombre del producto que va a atualizar: ")
    for producto in inventario:
        if producto["nombre"] == nombre:
            nuevaCantidad = input("ingrese la nueva cantidad disponible: ")
            producto["cantidad"] = nuevaCantidad
            print("cantidad actualizada.")
            return
    print("El producto no esta encontrado en inventario")


def eliminar_producto():
    nombre = input("Ingrese el nombre del producto que va a eliminar: ")
    for producto in inventario:
        if producto["nombre"] == nombre:
            inventario.remove(producto)
            print("Producto ha sido elimminado del inventario.")
            return
    print("Producto no encontrado en el inventario.")

def mostrar_inventario():
    print("Inventario")
    for producto in inventario:
        print( producto)

def buscar_producto():
    nombre = input("Ingrese el nombre del producto a buscar: ")
    for producto in inventario:
        if producto["nombre"] == nombre:
            print(producto)
            return
    print("Producto no encontrado en el inventario")

while True:
    
    opcion = int(input("selccione una opción:\n1. agregar poducto\n2. actualizar cantidad\n3. eliminar producto\n4. mostrar inventario\n5. buscar producto\n6. salir\n"))

    if opcion == 1:
        agregar_producto()
    elif opcion == 2:

        actualizar_cantidad()
    elif opcion == 3:
        eliminar_producto()
    elif opcion == 4:
        mostrar_inventario()
    elif opcion == 5:
        buscar_producto()
    elif opcion == 6:
        break
    else:
        print("opción no valida. Por favor, seleccione una opción valida")