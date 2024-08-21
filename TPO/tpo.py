from datetime import date

def crearTarea(idUsuario):
    tarea=[]
    tarea.append(idUsuario)
    tarea.append(input("Ingrese tarea: "))
    tarea.append("□")
    tarea.append(date.today().strftime("%d/%m/%Y")  )
    return tarea

#MENU
#tarea_realizada = "■"
#tarea_no_realizada = "□"
#print(crearTarea(1))
# (1)  Crear tarea.
# (-1) Salir.

estado=0
idUsuario=int(input("Ingrese id del usuario: "))
tareas=[]
while estado!=-1:
    estado=int(input("Opciones: \n (1)  Crear tarea.\n (2)  Mostrar tareas.\n (3)  Completar tarea.\n (4)  Eliminar tarea. \n (-1) Salir.\nEntrada: "))
    if estado == 1:
        tareas.append(crearTarea(idUsuario))
    elif estado == 2:
        for i in range(len(tareas)):
            print(f"{tareas[i][2]}  {tareas[i][1]} {tareas[i][3]} (Usuario: {tareas[i][0]})")
    elif estado == 3:
        completada=int(input("Ingrese numero de tarea completada: "))
        tareas[completada-1][2]="■"
    elif estado == 4:
        eliminar=int(input("Elija la tarea a elminar."))
        del tareas[eliminar]