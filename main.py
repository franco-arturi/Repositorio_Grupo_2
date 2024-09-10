#FUNCIONES
#Primera Parte TP
#Manejo de Tareas
def crearTarea():
    pass
def eliminarTarea():
    pass
def completarTarea():
    pass
def buscarTarea():
    pass
#   Seleccion de usuarios
def cargarUsuario(listado):
    usuario=[]
    usuario.append(input("Ingrese el nombre del nuevo usuario: "))
    usuario.append(int(input("Ingrese clave numerica: ")))
    listado.append(usuario)

def cambiarUsuario(listado,viejo):
    nuevo=str(input("Ingrese  nombre de usuario: "))
    for i in listado:
        if nuevo in i:
            nuevo=i
            contraseña=int(input("Ingrese contraseña: "))
            if contraseña == nuevo[1]:
                viejo[0]=nuevo[0]
                viejo[1]=nuevo[1]
            else:
                print("Contraseña incorrecta.")
            
    
def eliminarUsuario(listado,nombre,cont):
    for i in listado:
        if nombre in i and cont ==i[1]:
            print(i[1])
            del listado[listado.index(i)]
            print(f"Usuario {nombre} eliminado.")
            return
    print(f"Usuario {nombre} no encontrado o contraseña incorrecta.")

usuarios=[["a",12],["b",23],["c",34]]
usuario=[0,0]

    
#Calendario
#   Recordatorios de eventos

#Estudio
#   Cronometro Pomodoro


#   Sistema de Flashcards

#   Generación de Cuestionarios
 

#Segunda Parte TP
def cargarTarea():
    pass
def guardarProgresoTareas():
    pass
def generarReporte():
    pass


#DATOS
estado=True
usuarios=[["a",12],["b",2],["c",3]]
usuario=[0,0]



#MAIN
while estado==True:
    if usuario==[0,0]:
        opcion=int(input("Ingrese usuario o cree uno: "))
        if opcion==1:
            cambiarUsuario(usuarios,usuario)
        if opcion==2:
            cargarUsuario(usuarios)
            usuario[0]=usuarios[-1][0]
            usuario[1]=usuarios[-1][1]
    operacion=int(input("Ingrese operacion a realizar:\n1. Administrar usuarios."))
    if operacion == 1:
        oper_usuarios=int(input("Ingrese operacion:\n1. Eliminar usuario.\n2. Cambiar/Crear usuario."))
        if oper_usuarios == 1:
            nombre=input("Ingrese nombre de usuario a eliminar.")
            contraseña_elim=int(input("Ingrese contraseña del usuario: "))
            eliminarUsuario(usuarios,nombre,contraseña_elim)
            print(usuarios)
        elif oper_usuarios == 2:
            usuario[0]=0
            usuario[1]=0

    
#LOGIN
#MENU
#1.Tareas
#2.Herramientas Estudio
#3.Calendario

#   Tareas
#   1.Crear Tarea
#   2.Mostrar Tareas
#   3.Completar Tareas
#   4.Buscar Tarea
#   5.Eliminar Tarea
#
#   Herramientas Estudio
#   1.Pomodoro
#   2.Flashcards
#   3.Cuestionarios
#
#   Calendario
#   1.Mostrar Calendario
#   2.Agregar evento
#   3.Tiempo hasta proximo examen