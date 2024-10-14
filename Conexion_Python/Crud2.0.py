import os
import json

archivo_datos = 'datos_clientes.json'

def limpiar_pantalla():
    sistema = os.name
    if sistema == 'nt': 
        os.system('cls')

def cargar_datos():
    if os.path.exists(archivo_datos):
        with open(archivo_datos, 'r') as f:
            return json.load(f)
    return []

def guardar_datos(datos):
    with open(archivo_datos, 'w') as f:
        json.dump(datos, f, indent=4)

def opciones():
    while True:
        limpiar_pantalla()
        print("Menu de opciones")
        print("1) Crear un usuario")
        print("2) Leer un Usuario")
        print("3) Actualizar un Usuario")
        print("4) Borrar un Usuario")
        print("0) Salir")

        try:
            opcion = int(input("Digite un número para su opción: "))
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            input("Presione Enter para continuar...")
            continue

        if opcion == 1:
            crear()
        elif opcion == 2:
            leer()
        elif opcion == 3:
            actualizar()
        elif opcion == 4:
            borrar()
        elif opcion == 0:
            print("¡Chao con la de Dios!")
            break
        else:
            print("Opción no válida")
            input("Presione Enter para continuar...")

def crear():
    limpiar_pantalla()
    datos_clientes = cargar_datos()
    cliente = {
        "identificacion": input("Digite su identificación: "),
        "Nombre": input("Digite su nombre: "),
        "Apellido": input("Digite su apellido: "),
        "Edad": input("Digite su edad: "),
        "Correo": input("Digite su correo: ")
    }
    datos_clientes.append(cliente)
    guardar_datos(datos_clientes)
    print("Usuario creado con éxito")
    input("Presione Enter para continuar...")

def leer():
    limpiar_pantalla()
    datos_clientes = cargar_datos()
    if datos_clientes:
        identificacion = input("Digite la identificación del usuario que desea leer: ")
        encontrado = [c for c in datos_clientes if c["identificacion"] == identificacion]
        if encontrado:
            print("Datos del Usuario:")
            print(encontrado[0])
        else:
            print("Usuario no encontrado")
    else:
        print("No hay datos para mostrar")
    input("Presione Enter para continuar...")

def actualizar():
    limpiar_pantalla()
    datos_clientes = cargar_datos()
    if datos_clientes:
        identificacion = input("Digite la identificación del usuario que desea actualizar: ")
        for cliente in datos_clientes:
            if cliente["identificacion"] == identificacion:
                print("Datos actuales del Usuario:")
                print(cliente)
                cliente.update({
                    "Nombre": input("Digite su nuevo nombre: "),
                    "Apellido": input("Digite su nuevo apellido: "),
                    "Edad": input("Digite su nueva edad: "),
                    "Correo": input("Digite su nuevo correo: ")
                })
                guardar_datos(datos_clientes)
                print("Usuario actualizado con éxito")
                input("Presione Enter para continuar...")
                return
        print("Usuario no encontrado")
    else:
        print("No hay datos para actualizar")
    input("Presione Enter para continuar...")

def borrar():
    limpiar_pantalla()
    datos_clientes = cargar_datos()
    if datos_clientes:
        identificacion = input("Digite la identificación del usuario que desea borrar: ")
        datos_clientes = [c for c in datos_clientes if c["identificacion"] != identificacion]
        guardar_datos(datos_clientes)
        print("Usuario borrado")
    else:
        print("No hay datos para borrar")
    input("Presione Enter para continuar...")

if __name__ == "__main__":
    opciones()
