import datetime as d
import Usuarios 
import Pomodoro
import Cuestionarios
import Tareas
import Eventos

#MENUS FUNCIONES

def menuPomodoro():
    ciclos_pomodoro = int(input("\nIngrese la cantidad de ciclos Pomodoro (cada ciclo es 25 min de trabajo y 5 min de descanso): "))
    Pomodoro.pomodoro(ciclos_pomodoro)

def menuTareas():
    opcionTareas=0
    while opcionTareas != -1:
        opcionTareas = int(input("\n 1. Crear tarea\n 2. Completar tarea\n 3. Eliminar tarea\n 4. Buscar tarea\n 5. Ver todas las tareas\n-1. Salir\nSelecciona una opción: "))
        if opcionTareas == 1:
            descripcion = input("Descripción de la tarea: ")
            prioridad = int(input("Prioridad de la tarea (1-5): "))
            Tareas.crearTarea(tareas, descripcion, prioridad)
        elif opcionTareas == 2:
            descripcion = input("Descripción de la tarea a completar: ")
            Tareas.completarTarea(tareas, descripcion)
        elif opcionTareas == 3:
            descripcion = input("Descripción de la tarea a eliminar: ")
            Tareas.eliminarTarea(tareas, descripcion)
        elif opcionTareas == 4:
            patron = input("Ingrese un patrón para buscar: ")
            Tareas.buscarTarea(tareas, patron)
        elif opcionTareas == 5:
            print("\nLista de todas las tareas:")
            for tarea in tareas:
                estado = "Completa" if tarea["completa"] else "Incompleta"
                print(f"- {tarea['descripcion']} (Prioridad: {tarea['prioridad']}) - {estado}")

def menuAdministracionUsuarios():
    opcionUsuarios = 0
    while opcionUsuarios != -1 and usuarioActual != [0,0]:
        opcionUsuarios = int(input("\n1. Eliminar usuario\n2. Cambiar usuario\n-1. Volver\nSelecciona una opción: "))
        if opcionUsuarios == 1:
            nombre = input("\nIngrese nombre de usuario a eliminar: ")
            clave = int(input("Ingrese clave numérica del usuario a eliminar: "))
            Usuarios.eliminarUsuario(usuarios, nombre, clave, usuarioActual)
        elif opcionUsuarios == 2:
            Usuarios.cambiarUsuario(usuarios, usuarioActual)
        elif opcionUsuarios == -1:
            print("\nVolviendo al menú principal...")

def menuCalendario():
    opcionCalendario = 0
    while opcionCalendario != -1:
        opcionCalendario = int(input("\n1. Mostrar calendario\n2. Agregar evento\n3. Tiempo restante eventos\n4. Mostrar eventos\n-1. Volver\nSelecciona una opción: "))
        if opcionCalendario == 1:
            Eventos.mostrarCalendario(DIAACTUAL, MESACTUAL, AÑOACTUAL)
        elif opcionCalendario == 2:
            Eventos.agregarEvento(eventos)
        elif opcionCalendario == 3:
            Eventos.tiempoRestanteEventos(eventos)
        elif opcionCalendario == 4:
            Eventos.mostrarEventos(eventos)
        elif opcionCalendario == -1:
            print("\nVolviendo al menú principal...")

def menuCuestionario():
    opcionCuestionario = 0
    while opcionCuestionario != -1:
        opcionCuestionario=int(input("\nIngrese operacion: \n 1) Crear Cuestionario. \n 2) Ejecutar cuestionario.\n-1) Salir\nOpcion:  "))
        if opcionCuestionario==1:
            Cuestionarios.crearCuestionario(cuestionarios)
                        
        elif opcionCuestionario == 2:
            print("\nCuestionarios disponibles:")
            for cuest in cuestionarios.keys():
                print(cuest)
            nom = input("Ingrese nombre de cuestionario a ejecutar: ")
            
            cuestionario = cuestionarios.get(nom)
            if cuestionario != None:
                Cuestionarios.ejecutarCuestionario(cuestionario)
            elif cuestionario == None:
                print("Cuestionario inexistente.")

# DATOS
DIAACTUAL = d.date.today().day # Dia de hoy.
MESACTUAL = d.date.today().month # Mes actual.
AÑOACTUAL = d.date.today().year # Año actual.
eventos = [[9, 9, 2024, "Examen de Programación"],[10, 9, 2024, "Examen de Química"], [12, 9, 2024, "Examen de Física"],[28, 9, 2024, "Examen de matematica"]]
# Matriz de eventos(dia, mes, año, descripcion)
usuarios = [["usuario1", 1234], ["usuario2", 5678]]
# Matriz de usuarios(nombre, contraseña)
usuarioActual = [0, 0]
# Usuario actual
cuestionarios = {'Matematica': [{'pregunta': '1+1', 'opciones': ['2', '4', '1'], 'correcta': 1}, {'pregunta': '5*5', 'opciones': ['25', '30', '20'], 'correcta': 1}, {'pregunta': '2**2', 'opciones': ['4', '6', '12'], 'correcta': 1}]}
tareas = []


# MAIN
def main():
    opcionMenuPrincipal = 0
    while opcionMenuPrincipal != -1:
        if usuarioActual == [0, 0]:
            opcionUsuario = int(input("\n 1. Ingresar usuario\n 2. Crear usuario\n-1. Salir\nSelecciona una opción: "))
            if opcionUsuario == 1:
                Usuarios.cambiarUsuario(usuarios, usuarioActual)
            elif opcionUsuario == 2:
                Usuarios.cargarUsuario(usuarios,usuarioActual)
            elif opcionUsuario == -1:
                print("\nSaliendo del programa...")
                opcionMenuPrincipal = -1
        else:
            opcionMenuPrincipal = int(input("\n 1. Administrar usuarios\n 2. Calendario y eventos\n 3. Cuestionarios\n 4. Técnica Pomodoro\n 5. Administrar tareas\n-1. Salir\nSelecciona una opción: "))
            if opcionMenuPrincipal == 1:
                menuAdministracionUsuarios()            
            elif opcionMenuPrincipal == 2:
                menuCalendario()            
            elif opcionMenuPrincipal == 3:
                menuCuestionario()
            elif opcionMenuPrincipal == 4:
                menuPomodoro()
            elif opcionMenuPrincipal == 5:
                # Submenú de tareas
                menuTareas()             
            elif opcionMenuPrincipal == -1:
                print("\nSaliendo del programa...")


main()