import datetime as d
import json
import Usuarios
import Pomodoro
import Cuestionarios
import Tareas
import Eventos
import Archivos

# Nombre del archivo JSON
ARCHIVO_JSON = 'datos.json'
ARCHIVO_LOG = 'actividad.log'

# Función para cargar datos desde el archivo JSON

# Cargar datos iniciales
datos = Archivos.cargar_datos(ARCHIVO_JSON)


# MENUS FUNCIONES

def menuPomodoro():
    try:
        ciclos_pomodoro = int(input("""========================================
       CONFIGURACIÓN POMODORO          
========================================
Por favor, ingrese la cantidad de ciclos Pomodoro.  
Nota: Cada ciclo incluye 25 minutos de trabajo y 5 minutos de descanso.
========================================
Cantidad de ciclos: """))
        Pomodoro.pomodoro(ciclos_pomodoro)
        Archivos.registrar_actividad(f"Ejecutó {ciclos_pomodoro} ciclos Pomodoro.",ARCHIVO_LOG)
    except ValueError:
        print("Ingrese un numero entero para la cantidad de ciclos.")
def menuTareas():
    opcionTareas = 0
    while opcionTareas != -1:
        try:
            opcionTareas = int(input("""========================================
           GESTIÓN DE TAREAS           
========================================
[1] Crear tarea
[2] Completar tarea
[3] Eliminar tarea
[4] Buscar tarea
[5] Ver todas las tareas
[-1] Volver al menú anterior
========================================
Selecciona una opción: """))
        except ValueError:
            print("Por favor, ingrese únicamente valores numéricos.")
            opcionTareas=0

        if opcionTareas == 1:
            descripcion = input("Descripción de la tarea: ").title()
            prioridad = 0
            while not (1 <= prioridad <= 5):
                try:
                    prioridad = int(input("Prioridad de la tarea (1-5): "))
                except ValueError:
                    prioridad=0
                if not (1 <= prioridad <= 5):
                    print("Error: La prioridad debe ser un número entre 1 y 5.")
            Tareas.crearTarea(datos, descripcion, prioridad,usuarioActual[0])
            Archivos.guardar_datos(datos,ARCHIVO_JSON)  # Guardar después de crear una tarea
            Archivos.registrar_actividad(f"Creó tarea: {descripcion} con prioridad {prioridad}.",ARCHIVO_LOG)
        
        elif opcionTareas == 2:
            descripcion = input("Descripción de la tarea a completar: ").title()
            Tareas.completarTarea(datos, descripcion,usuarioActual[0])
            Archivos.guardar_datos(datos,ARCHIVO_JSON)  # Guardar después de completar una tarea
            Archivos.registrar_actividad(f"Completó tarea: {descripcion}.",ARCHIVO_LOG)
        
        elif opcionTareas == 3:
            descripcion = input("Descripción de la tarea a eliminar: ").title()
            Tareas.eliminarTarea(datos, descripcion,usuarioActual[0])
            Archivos.guardar_datos(datos,ARCHIVO_JSON)  # Guardar después de eliminar tarea
            Archivos.registrar_actividad(f"Eliminó tarea: {descripcion}.",ARCHIVO_LOG)
        
        elif opcionTareas == 4:
            patron = input("Ingrese un patrón para buscar: ")
            Tareas.buscarTarea(datos, patron,usuarioActual[0])
        
        elif opcionTareas == 5:
            print("\nLista de todas las tareas:")
            for tarea in datos[usuarioActual[0]]["tareas"]:
                estado = "Completa" if tarea["completa"] else "Incompleta"
                print(f"- {tarea['descripcion']} (Prioridad: {tarea['prioridad']}) - {estado}")



def menuAdministracionUsuarios():
    opcionUsuarios = 0
    while opcionUsuarios != -1 and usuarioActual != [0,0]:
        try:
            opcionUsuarios = int(input("""========================================
          GESTIÓN DE USUARIOS          
========================================
[1] Eliminar usuario
[2] Cambiar de usuario
[-1] Volver al menú anterior
========================================
Selecciona una opción: """))
        except ValueError:
            print("Por favor, ingrese únicamente valores numéricos.")
            opcionUsuarios=0
        if opcionUsuarios == 1:
            nombre = input("\nIngrese nombre de usuario a eliminar: ")
            clave = (input("Ingrese clave  del usuario a eliminar: "))
            Usuarios.eliminarUsuario(datos, nombre, clave, usuarioActual)
            Archivos.guardar_datos(datos,ARCHIVO_JSON)  # Guardar después de eliminar usuario
            Archivos.registrar_actividad(f"Eliminó usuario: {nombre}.",ARCHIVO_LOG)
        elif opcionUsuarios == 2:
            Usuarios.cambiarUsuario(datos, usuarioActual)
            Archivos.guardar_datos(datos,ARCHIVO_JSON)  # Guardar después de cambiar usuario
            Archivos.registrar_actividad(f"Cambió a usuario: {usuarioActual[0]}.",ARCHIVO_LOG)

def menuCalendario():
    opcionCalendario = 0
    while opcionCalendario != -1:
        try:
            opcionCalendario = int(input("""========================================
           CALENDARIO Y EVENTOS         
========================================
[1] Mostrar calendario
[2] Agregar evento
[3] Tiempo restante para eventos
[4] Mostrar eventos
[-1] Volver al menú anterior
========================================
Selecciona una opción: """))
        except ValueError:
            print("Por favor, ingrese únicamente valores numéricos.")
            opcionCalendario=0
        if opcionCalendario == 1:
            Eventos.mostrarCalendario(DIAACTUAL, MESACTUAL, AÑOACTUAL)
            Archivos.registrar_actividad("Mostró el calendario.",ARCHIVO_LOG)
        elif opcionCalendario == 2:
            Eventos.agregarEvento(datos,usuarioActual[0])
            Archivos.guardar_datos(datos,ARCHIVO_JSON)  # Guardar después de agregar evento
            Archivos.registrar_actividad("Agregó un evento.",ARCHIVO_LOG)
        elif opcionCalendario == 3:
            Eventos.tiempoRestanteEventos(datos,usuarioActual[0])
            Archivos.registrar_actividad("Consultó tiempo restante de eventos.",ARCHIVO_LOG)
        elif opcionCalendario == 4:
            Eventos.mostrarEventos(datos,usuarioActual[0])
            Archivos.registrar_actividad("Mostró los eventos.",ARCHIVO_LOG)

def menuCuestionario():
    opcionCuestionario = 0  # Inicializa la variable para la opción del cuestionario
    while opcionCuestionario != -1:  # Continúa el bucle hasta que se elija volver al menú anterior
        try:
            opcionCuestionario = int(input("""========================================
         GESTIÓN DE CUESTIONARIOS      
========================================
[1] Crear cuestionario
[2] Ejecutar cuestionario
[-1] Volver al menú anterior
========================================
Ingrese su opción: """))
        except ValueError:
            print("Por favor, ingrese únicamente valores numéricos.")
            opcionCuestionario=0
        if opcionCuestionario == 1:
            # Si el usuario elige crear un cuestionario
            Cuestionarios.crearCuestionario(datos,usuarioActual[0])  # Llama a la función para crear un nuevo cuestionario
            Archivos.guardar_datos(datos,ARCHIVO_JSON)  # Guarda los datos después de crear el cuestionario
            Archivos.registrar_actividad("Creó un cuestionario.",ARCHIVO_LOG)  # Registra la actividad

        elif opcionCuestionario == 2:
            # Si el usuario elige ejecutar un cuestionario
            print("\nCuestionarios disponibles:")  # Muestra los cuestionarios disponibles
            for cuest in datos[usuarioActual[0]]["cuestionarios"].keys():
                print(cuest)  # Imprime el nombre de cada cuestionario
            
            # Solicita al usuario el nombre del cuestionario a ejecutar
            nom = input("Ingrese nombre de cuestionario a ejecutar: ").title()  # Normaliza el nombre a formato título
            
            cuestionario = datos[usuarioActual[0]]["cuestionarios"].get(nom)  # Busca el cuestionario por su nombre
            
            if cuestionario is not None:  # Verifica si el cuestionario existe
                Cuestionarios.ejecutarCuestionario(cuestionario)  # Ejecuta el cuestionario
                Archivos.registrar_actividad(f"Ejecución del cuestionario: {nom}.",ARCHIVO_LOG)  # Registra la actividad
            else:
                print("Cuestionario inexistente.")  # Notifica si el cuestionario no existe


# DATOS
DIAACTUAL = d.date.today().day
MESACTUAL = d.date.today().month
AÑOACTUAL = d.date.today().year
usuarioActual = [0, 0]  # Usuario actual, va a cambiar al ingresar un usuario.

# MAIN
def main():
    opcionMenuPrincipal = 0
    while opcionMenuPrincipal != -1:
        if usuarioActual == [0, 0]:
            try: 
                opcionUsuario = int(input("""\n ========================================
          MENÚ DE USUARIO              
========================================
[1] Ingresar usuario
[2] Crear usuario
[-1] Salir
========================================
Selecciona una opción: """))
            except ValueError:
                print("Por favor, ingrese únicamente valores numéricos.")
                opcionUsuario=0
            if opcionUsuario == 1:
                Usuarios.cambiarUsuario(datos, usuarioActual)
                Archivos.guardar_datos(datos,ARCHIVO_JSON)
            elif opcionUsuario == 2:
                Usuarios.cargarUsuario(datos, usuarioActual)
                Archivos.guardar_datos(datos,ARCHIVO_JSON)
        else:
            try:
                opcionMenuPrincipal = int(input("""========================================
           MENÚ PRINCIPAL              
========================================
[1] Administrar usuarios
[2] Calendario y eventos
[3] Cuestionarios
[4] Técnica Pomodoro
[5] Administrar tareas
[-1] Volver al menú anterior
========================================
Selecciona una opción: """))
            except ValueError:
                print("Por favor, ingrese únicamente valores numéricos.")
                opcionMenuPrincipal=0
            if opcionMenuPrincipal == 1:
                menuAdministracionUsuarios()            
            elif opcionMenuPrincipal == 2:
                menuCalendario()            
            elif opcionMenuPrincipal == 3:
                menuCuestionario()
            elif opcionMenuPrincipal == 4:
                menuPomodoro()
            elif opcionMenuPrincipal == 5:
                menuTareas()

main()

