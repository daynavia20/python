#ejercicio del profesor
def agregarProducto():
    print("")   
    nuevaTarea=input("vamos a agregar una tarea:")
    tareas.append(nuevaTarea)
    print("")
    print("tarea agregada")
    completado.append("Incompleta")

def tareaCompleta():
    tareaRealizada=input("Escribe que tarea realizaste:")
    for i in range(len(tareas)):
        if (tareas[i]==tareaRealizada):
            completado[i]="completo"
            print("")
            print(" tarea completada ")
            return
    print("no se hallo la tarea ")   

def eliminarTarea():
    print("")
    tareaEliminar=input("escribe la tarea que deseas eliminar: ")
    for i in range (len(tareas)):
        if (tareas[i] == tareaEliminar):
            if (completado=="completo"):
                print("la tarea no esta completa")  
                tareas.pop
                return
            
            else:
                tareas.pop(i)
                completado.pop(i)
                print("")
                print("tarea borrada")
                return
    print("no se hallo la tarea ")
# pop sire para eliminar teniedno en cuenta el indice 
# remove para eliminar la palabra te        
def mostrarPendientes():
    print("")
    for i in range(len(completado)):
        if (completado[i]=="Incompleta"):
            print(tareas[i])

tareas=["barrer","trapear","lavar",] #podemos colocar numero letras y veradero falso
completado=["Incompleta", "Incompleta","Incompleta"]
while True:
    print("----menu----")
    print(" 1 - agregar elemento a la lista ")
    print(" 2 - marcar tareas ")
    print(" 3 - eliminar tareas ")
    print(" 4 - mostrar tareas pendientes  ") 
    print(" 5 - mostrar todas la tareas ")
    print(" 6 - salir ")
    respuesta =int(input("Elija una opcion: ")) #pedir una opcion al ususrio
    
    if (respuesta==1):
        agregarProducto()

    elif (respuesta ==2):
        tareaCompleta()

    elif respuesta==3:
       eliminarTarea()

    elif respuesta==4:
        mostrarPendientes()

    elif respuesta==5:
        print("")
        print(tareas)    
        
    elif respuesta ==6 :
        print("salir")    
        break
    else:
        print("opcion no valida")
      



#i=0
    #while True:
        #if (tareas[i==""]):
            #tareas[i]==nuevaTarea
            #break#

