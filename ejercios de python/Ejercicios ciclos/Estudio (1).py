
# Programa
# Crea un programa que administre una lista de tareas pendientes. El programa debe permitir al
# usuario agregar nuevas tareas, marcar tareas como completadas y eliminar tareas de la lista.
# Además, el programa debe mostrar la lista de tareas pendientes en cualquier momento y
# proporcionar opciones para que el usuario interactúe con ella.
# Por ejemplo, el usuario podría ingresar "Agregar" para agregar una nueva tarea, "Completar" para
# marcar una tarea como completada, "Eliminar" para eliminar una tarea de la lista, y "Mostrar" para
# mostrar todas las tareas pendientes.
# Este ejercicio implica el uso de una lista para almacenar las tareas pendientes y decisiones para
# determinar qué acción realizar en función de la entrada del usuario.

def agregarProducto():
    print("")
    nuevaTarea=input("vamos a agregar una tarea: ")
    tareas.append(nuevaTarea)
    print("Tarea agregada")
    completado.append("Incompleta")

def tareaCompleta():
    print("")
    tareaRealizada=input("Escribe que tarea realizaste: ")
    for i in range(len(tareas)):
        if (tareas[i]==tareaRealizada):
            completado[i]="Completo"
            print("Tarea completada")
            return
    print("No se hayó la tarea")

def eliminarTarea():
    print("")
    tareaEliminar=input("Escribe la tarea que quieres eliminar: ")
    for i in range(len(tareas)):
        if (tareas[i]==tareaEliminar):
            if (completado=="Incompleta"):
                print("La tarea no esta completa")
                
                return
            else:
                tareas.pop(i)
                completado.pop(i)
                print("Tarea borrada")
                return
    print("No se hayó la tarea")


def mostrarPendientes():
    print("")
    for i in range(len(completado)):
        if (completado[i]=="Incompleta"):
            print(tareas[i])




tareas=["barrer","trapear","lavar"]
completado=["Incompleta","Incompleta","Incompleta"]
while True:
    print("")
    print("-----Menú-----")
    print("1) Agregar elemento a la lista")
    print("2) Marcar tarea como completa")
    print("3) Elimninar tareas")
    print("4) Mostrar tareas pendientes")
    print("5) Mostrar todas las tareas")
    print("6) Salir")
    respuesta=int(input("Elije la acción: "))
    
    if (respuesta==1):
        agregarProducto()

    elif (respuesta==2):
        tareaCompleta()

    elif (respuesta==3):
        eliminarTarea()

    elif (respuesta==4):
        mostrarPendientes()

    elif (respuesta==5):
        print("")
        print(tareas)

    elif (respuesta==6):
        print("Gracias by: Kevinsito")
        break
    else:
        print("Opción no valida")

