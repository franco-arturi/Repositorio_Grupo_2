import datetime as d
import json
import Usuarios
import Pomodoro
import Cuestionarios
import Tareas
import Eventos

# Nombre del archivo JSON
ARCHIVO_JSON = 'datos.json'
ARCHIVO_LOG = 'actividad.log'

# Función para cargar datos desde el archivo JSON
def cargar_datos():
    try:
        with open(ARCHIVO_JSON, 'r') as archivo:
            datos = json.load(archivo)
            print("Datos cargados exitosamente.")
    except (FileNotFoundError, json.JSONDecodeError):
        # Crear estructura vacía si el archivo no existe o está vacío
        datos = {
            "admin": {"eventos": [],
                        "cuestionarios": {},
                        "tareas": [],
                        "contraseña":11111}
            
        }
        # Esto guarda la estructura inicial en el archivo
        guardar_datos(datos)
        print("Archivo de datos no encontrado. Se ha creado uno nuevo.")
    return datos

# Función para guardar datos en el archivo JSON
def guardar_datos(datos):
    with open(ARCHIVO_JSON, 'w') as archivo:
        json.dump(datos, archivo, indent=4)
    print("Datos guardados exitosamente.")

# Función para registrar actividad en el log
def registrar_actividad(mensaje):
    with open(ARCHIVO_LOG, 'a') as log_file:
        timestamp = d.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"{timestamp} - {mensaje}\n")

# Cargar datos iniciales
datos = cargar_datos()

# MENUS FUNCIONES

def menuPomodoro():
    ciclos_pomodoro = int(input("\nIngrese la cantidad de ciclos Pomodoro (cada ciclo es 25 min de trabajo y 5 min de descanso): "))
    Pomodoro.pomodoro(ciclos_pomodoro)
    registrar_actividad(f"Ejecutó {ciclos_pomodoro} ciclos Pomodoro.")

def menuTareas():
    opcionTareas = 0
    while opcionTareas != -1:
        opcionTareas = int(input("\n 1. Crear tarea\n 2. Completar tarea\n 3. Eliminar tarea\n 4. Buscar tarea\n 5. Ver todas las tareas\n-1. Volver al menú anterior\nSelecciona una opción: "))
        
        if opcionTareas == 1:
            descripcion = input("Descripción de la tarea: ").title()
            prioridad = 0
            while not (1 <= prioridad <= 5):
                prioridad = int(input("Prioridad de la tarea (1-5): "))
                if not (1 <= prioridad <= 5):
                    print("Error: La prioridad debe ser un número entre 1 y 5.")
            Tareas.crearTarea(datos, descripcion, prioridad,usuarioActual[0])
            guardar_datos(datos)  # Guardar después de crear una tarea
            registrar_actividad(f"Creó tarea: {descripcion} con prioridad {prioridad}.")
        
        elif opcionTareas == 2:
            descripcion = input("Descripción de la tarea a completar: ").title()
            Tareas.completarTarea(datos, descripcion,usuarioActual[0])
            guardar_datos(datos)  # Guardar después de completar una tarea
            registrar_actividad(f"Completó tarea: {descripcion}.")
        
        elif opcionTareas == 3:
            descripcion = input("Descripción de la tarea a eliminar: ").title()
            Tareas.eliminarTarea(datos, descripcion,usuarioActual[0])
            guardar_datos(datos)  # Guardar después de eliminar tarea
            registrar_actividad(f"Eliminó tarea: {descripcion}.")
        
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
        opcionUsuarios = int(input("\n1. Eliminar usuario\n2. Cambiar usuario\n-1. Volver al menú anterior\nSelecciona una opción: "))
        if opcionUsuarios == 1:
            nombre = input("\nIngrese nombre de usuario a eliminar: ")
            clave = int(input("Ingrese clave numérica del usuario a eliminar: "))
            Usuarios.eliminarUsuario(datos, nombre, clave, usuarioActual)
            guardar_datos(datos)  # Guardar después de eliminar usuario
            registrar_actividad(f"Eliminó usuario: {nombre}.")
        elif opcionUsuarios == 2:
            Usuarios.cambiarUsuario(datos, usuarioActual)
            guardar_datos(datos)  # Guardar después de cambiar usuario
            registrar_actividad(f"Cambió a usuario: {usuarioActual[0]}.")

def menuCalendario():
    opcionCalendario = 0
    while opcionCalendario != -1:
        opcionCalendario = int(input("\n1. Mostrar calendario\n2. Agregar evento\n3. Tiempo restante eventos\n4. Mostrar eventos\n-1. Volver al menú anterior\nSelecciona una opción: "))
        if opcionCalendario == 1:
            Eventos.mostrarCalendario(DIAACTUAL, MESACTUAL, AÑOACTUAL)
            registrar_actividad("Mostró el calendario.")
        elif opcionCalendario == 2:
            Eventos.agregarEvento(datos,usuarioActual[0])
            guardar_datos(datos)  # Guardar después de agregar evento
            registrar_actividad("Agregó un evento.")
        elif opcionCalendario == 3:
            Eventos.tiempoRestanteEventos(datos,usuarioActual[0])
            registrar_actividad("Consultó tiempo restante de eventos.")
        elif opcionCalendario == 4:
            Eventos.mostrarEventos(datos,usuarioActual[0])
            registrar_actividad("Mostró los eventos.")

def menuCuestionario():
    opcionCuestionario = 0  # Inicializa la variable para la opción del cuestionario
    while opcionCuestionario != -1:  # Continúa el bucle hasta que se elija volver al menú anterior
        opcionCuestionario = int(input("\nIngrese operación: \n 1) Crear Cuestionario. \n 2) Ejecutar cuestionario.\n-1) Volver al menú anterior\nOpción:  "))
        
        if opcionCuestionario == 1:
            # Si el usuario elige crear un cuestionario
            Cuestionarios.crearCuestionario(datos,usuarioActual[0])  # Llama a la función para crear un nuevo cuestionario
            guardar_datos(datos)  # Guarda los datos después de crear el cuestionario
            registrar_actividad("Creó un cuestionario.")  # Registra la actividad

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
                registrar_actividad(f"Ejecución del cuestionario: {nom}.")  # Registra la actividad
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
            opcionUsuario = int(input("\n 1. Ingresar usuario\n 2. Crear usuario\n-1. Salir\nSelecciona una opción: "))
            if opcionUsuario == 1:
                Usuarios.cambiarUsuario(datos, usuarioActual)
                guardar_datos(datos)
            elif opcionUsuario == 2:
                Usuarios.cargarUsuario(datos, usuarioActual)
                guardar_datos(datos)
        else:
            opcionMenuPrincipal = int(input("\n 1. Administrar usuarios\n 2. Calendario y eventos\n 3. Cuestionarios\n 4. Técnica Pomodoro\n 5. Administrar tareas\n-1. Volver al menú anterior\nSelecciona una opción: "))
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
