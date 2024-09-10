import datetime as d


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
def mostrarCalendario(dia,mes,año,):
    meses=[["Enero",31],["Febrero",28],["Marzo",31],["Abril",30],["Mayo",31],
           ['Junio',30],['Julio',31],['Agosto',31],["Septiembre",30],['Octubre',31],["Noviembre",30],
           ['Diciembre',31]]
    print(f"             {meses[mes-1][0]} {año}")

    contador=0
    for i in range(meses[mes-1][1]):
        if contador<6:
            if i<dia:
                print(f"{RED}{i+1}{RESET}".center(15),end="")
                contador+=1
            else:
                print(f"{GREEN}{i+1}{RESET}".center(15),end="")
                contador+=1
        else:
            if i<dia:
                print(f"{RED}{i+1}{RESET}".center(15))
                contador=0
            else:
                print(f"{GREEN}{i+1}{RESET}".center(15))
                contador=0

def ordenar_matriz(matriz):
    for i in range(len(matriz)-1):
        for j in range(i,len(matriz)):
            if matriz[i][0]>matriz[j][0]:
                aux=matriz[j]
                matriz[j]=matriz[i]
                matriz[i]=aux

def agregar_evento(matriz):
    evento=[]
    evento.append(int(input("Ingrese dia del evento: ")))
    evento.append(int(input("Ingrese mes del evento: ")))
    evento.append(int(input("Ingrese año del evento: ")))
    evento.append((input("Ingrese evento: ")))
    matriz.append(evento)

def tiempo_restante(matriz):
    fecha=(d.datetime.now())
    for i in range(len(matriz)):
        fecha_aux = d.datetime(matriz[i][2],matriz[i][1],matriz[i][0],12,0,0)
        diferencia = fecha_aux - fecha
        print(f"{matriz[i][3]} faltan {diferencia}")
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


RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"
dia=d.date.today().day
mes=d.date.today().month
año=d.date.today().year
eventos=[[10,9,2024,"Examen Quimica."],[12,9,2024,"Examen Fisica"],[9,9,2024,"Examen Progra"],[9,9,2025,"Examen Matematica"]]
eventos_mes=[]

estado=True
usuarios=[["a",12],["b",2],["c",3]]
usuario=[0,0]



#MAIN
while estado==True:
    if usuario==[0,0]:
        opcion=int(input("Ingrese usuario(1) o cree uno(2): "))
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
    elif operacion == 2:
        oper_calendario = int(input("Ingrese operacion:\n1. Mostrar Calendario\n2. Agregar evento\n -"))
        ordenar_matriz(eventos_mes)
        for i in range(len(eventos)):
            if eventos[i][2] == año and eventos[i][1] == mes and eventos[i][0] >= dia:
                eventos_mes.append(eventos[i])
        ordenar_matriz(eventos_mes)
        if oper_calendario == 1:
            mostrarCalendario(dia,mes,año)
            print("\nEventos del mes: ")
            for i in range(len(eventos_mes)):
                print(f"{eventos_mes[i][0]}/{eventos_mes[i][1]}/{eventos_mes[i][2]} ---  {eventos_mes[i][3]}")
        elif oper_calendario == 2:
            agregar_evento(eventos)
        elif oper_calendario == 3:
            tiempo_restante(eventos_mes)


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