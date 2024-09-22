import datetime as d
import time

# FUNCIONES


#Tecnica Pomodoro

def pomodoro(ciclos):
    for i in range(ciclos):
        print(f"Pomodoro {i + 1} - Sesión de estudio (25 minutos)")
        timer(25)  # 25 minutos de estudio
        if i < ciclos - 1:  # No hacer descanso después del último ciclo y terminarlo.
            print("Descanso (5 minutos)")
            timer(5)  # 5 minutos de descanso
    print("Todas las sesiones de Pomodoro finalizadas!")

def timer(tiempo):
    for i in range(tiempo * 60, 0, -1):
        segundos = int(i % 60)
        minutos = int(i / 60) % 60
        horas = i // 3600
        print(f"{horas:02}:{minutos:02}:{segundos:02}", end='\r')  
        time.sleep(1)  # Pausa de 1 segundo para simular el tiempo real
        

# Manejo de Tareas
def crearTarea(tareas, descripcion, prioridad): 
    # Crea una nueva tarea con descripción y prioridad
    if isinstance(descripcion, str) and isinstance(prioridad, int):
        nuevaTarea = {"descripcion": descripcion, "prioridad": prioridad, "completa": False}
        tareas.append(nuevaTarea)
        print(f"\nTarea '{descripcion}' creada con prioridad {prioridad}.")
    else:
        print("\nError: Descripción debe ser una cadena de texto y la prioridad un entero.")

def eliminarTarea(tareas, descripcion):
    # Elimina una tarea buscandola por su descripción
    tareaFiltrada = list(filter(lambda t: t['descripcion'] == descripcion, tareas))
    if tareaFiltrada:
        tareas.remove(tareaFiltrada[0])
        print(f"\nTarea '{descripcion}' eliminada con éxito.")
    else:
        print(f"\nNo se encontró la tarea con descripción '{descripcion}'.")

def completarTarea(tareas, descripcion):
    # Marca una tarea como completa
    tarea = next(filter(lambda t: t['descripcion'] == descripcion, tareas), None)
    if tarea:
        tarea['completa'] = True
        print(f"\nTarea '{descripcion}' marcada como completa.")
    else:
        print(f"\nTarea '{descripcion}' no encontrada.")

def buscarTarea(tareas, patron):
    # Busca tareas que coincidan con un patrón específico
    patronCompilado = re.compile(patron, re.IGNORECASE)
    tareasEncontradas = list(filter(lambda t: patronCompilado.search(t['descripcion']), tareas))
    if tareasEncontradas:
        print("\nTareas encontradas:")
        for tarea in tareasEncontradas:
            print(f"- {tarea['descripcion']}, Prioridad: {tarea['prioridad']}")
    else:
        print(f"\nNo se encontraron tareas que coincidan con el patrón '{patron}'.")


# Usuarios
def cargarUsuario(listado):
    nombre = input("\nIngrese el nombre del nuevo usuario: ")
    if any(usuario[0] == nombre for usuario in listado):
        print("\nError: El nombre de usuario ya existe.")
        return
    
    clave = int(input("Ingrese clave numérica: "))
    usuario = [nombre, clave]
    listado.append(usuario)
    print("\nUsuario creado exitosamente.")
    usuarioActual[:] = usuario

def cambiarUsuario(listado, usuarioActual):
    # Cambia al usuario actual ingresando nombre y contraseña
    nuevoUsuario = input("\nIngrese nombre de usuario: ")
    for usuario in listado:
        if nuevoUsuario == usuario[0]:
            contraseña = int(input("Ingrese contraseña: "))
            if contraseña == usuario[1]:
                usuarioActual[:] = usuario
                print("\nUsuario cambiado exitosamente.")
            else:
                print("\nContraseña incorrecta.")
            return
    print("\nUsuario no encontrado.")

def eliminarUsuario(listado, nombre, contraseña):
    # Elimina un usuario si se proporciona el nombre y contraseña correctos
    for usuario in listado:
        if nombre == usuario[0] and contraseña == usuario[1]:
            listado.remove(usuario)
            if usuario == usuarioActual:
                usuarioActual[:] = [0, 0]
            print(f"\nUsuario {nombre} eliminado con éxito.")
            return
    print(f"\nUsuario {nombre} no encontrado o contraseña incorrecta.")

# Calendario
def mostrarCalendario(dia, mes, año):
    # Muestra el calendario del mes y año especificados
    meses = [["Enero", 31], ["Febrero", 28], ["Marzo", 31], ["Abril", 30], ["Mayo", 31],
             ['Junio', 30], ['Julio', 31], ['Agosto', 31], ["Septiembre", 30], ['Octubre', 31],
             ["Noviembre", 30], ['Diciembre', 31]]
    print(f"\n             {meses[mes - 1][0]} {año}")
    
    contador = 0
    for i in range(meses[mes - 1][1]):
        if contador < 6:
            if i + 1 < dia:
                print(f"{RED}{i + 1}{RESET}".center(15), end="")
            else:
                print(f"{GREEN}{i + 1}{RESET}".center(15), end="")
            contador += 1
        else:
            if i + 1 < dia:
                print(f"{RED}{i + 1}{RESET}".center(15))
            else:
                print(f"{GREEN}{i + 1}{RESET}".center(15))
            contador = 0

def ordenarEventos(eventos):
    # Ordena los eventos por fecha
    eventos.sort(key=lambda x: (x[2], x[1], x[0]))

def agregarEvento(eventos):
    # Agrega un nuevo evento, asegurando que la fecha no sea del pasado
    evento = []
    diaEvento = int(input("\nIngrese día del evento: "))
    mesEvento = int(input("Ingrese mes del evento: "))
    añoEvento = int(input("Ingrese año del evento: "))
    
    try:
        fechaEvento = d.datetime(añoEvento, mesEvento, diaEvento)
    except ValueError as e:
        print(f"\nError: {e}")
        return
    
    fechaActual = d.datetime.now()
    
    if fechaEvento < fechaActual:
        print("\nError: No se puede agregar un evento en el pasado.")
        return
    
    evento.append(diaEvento)
    evento.append(mesEvento)
    evento.append(añoEvento)
    evento.append(input("Ingrese descripción del evento: "))
    eventos.append(evento)
    ordenarEventos(eventos)
    print("\nEvento agregado exitosamente.")

def tiempoRestanteEventos(eventos):
    # Muestra el tiempo restante para los eventos programados
    fechaActual = d.datetime.now()
    print("\nTiempo restante para los eventos:")
    for evento in eventos:
        fechaEvento = d.datetime(evento[2], evento[1], evento[0])
        diferencia = fechaEvento - fechaActual
        
        if diferencia.days == 1:
            print(f"- El día siguiente es el evento '{evento[3]}'.")
        elif diferencia.days > 1:
            print(f"- Faltan {diferencia.days} días para el evento '{evento[3]}'.")
        elif diferencia.days == 0:
            print(f"- Hoy es el evento '{evento[3]}'.")
        else:
            print(f"- El evento '{evento[3]}' ya ha pasado.")

def mostrarEventos(eventos):
    # Muestra todos los eventos programados, con colores según la fecha
    fechaActual = d.datetime.now()
    if eventos:
        print("\nEventos programados:")
        for evento in eventos:
            fechaEvento = d.datetime(evento[2], evento[1], evento[0])
            fechaEventoStr = f"{evento[0]}/{evento[1]}/{evento[2]}"
            
            if fechaEvento < fechaActual:  # Evento pasado
                print(f"{RED}- {fechaEventoStr}: {evento[3]} (Este evento ya paso){RESET}")
            else:  # Evento futuro
                print(f"{GREEN}- {fechaEventoStr}: {evento[3]} (Este evento aun no paso){RESET}")
    else:
        print("\nNo hay eventos programados.")

# Cuestionarios




# DATOS
RED = "\033[31m"  # Rojo
GREEN = "\033[32m"  # Verde
RESET = "\033[0m"  # Este reset reestablece el color. No se si funciona o si es al pedo. Chequealo y si no te parece ok sacalo nomas.
diaActual = d.date.today().day
mesActual = d.date.today().month
añoActual = d.date.today().year
eventos = [[9, 9, 2024, "Examen de Programación"],[10, 9, 2024, "Examen de Química"], [12, 9, 2024, "Examen de Física"],[28, 9, 2024, "Examen de matematica"]]
usuarios = [["usuario1", 1234], ["usuario2", 5678]]
usuarioActual = [0, 0]



# MAIN
opcionMenuPrincipal = 0

while opcionMenuPrincipal != -1:
    if usuarioActual == [0, 0]:
        opcionUsuario = int(input("\n1. Ingresar usuario\n2. Crear usuario\n-1. Salir\nSelecciona una opción: "))
        if opcionUsuario == 1:
            cambiarUsuario(usuarios, usuarioActual)
        elif opcionUsuario == 2:
            cargarUsuario(usuarios)
        elif opcionUsuario == -1:
            print("\nSaliendo del programa...")
            opcionMenuPrincipal = -1
    else:
        print(usuarioActual)
        opcionMenuPrincipal = int(input("\n1. Administrar usuarios\n2. Calendario y eventos\n3. Cuestionarios\n4. Técnica Pomodoro\n-1. Salir\nSelecciona una opción: "))
        
        if opcionMenuPrincipal == 1:
            opcionUsuarios = 0
            while opcionUsuarios != -1 and usuarioActual != [0,0]:
                opcionUsuarios = int(input("\n1. Eliminar usuario\n2. Cambiar usuario\n-1. Volver\nSelecciona una opción: "))
                if opcionUsuarios == 1:
                    nombre = input("\nIngrese nombre de usuario a eliminar: ")
                    clave = int(input("Ingrese clave numérica del usuario a eliminar: "))
                    eliminarUsuario(usuarios, nombre, clave)
                elif opcionUsuarios == 2:
                    cambiarUsuario(usuarios, usuarioActual)
                elif opcionUsuarios == -1:
                    print("\nVolviendo al menú principal...")
        
        elif opcionMenuPrincipal == 2:
            opcionCalendario = 0
            while opcionCalendario != -1:
                opcionCalendario = int(input("\n1. Mostrar calendario\n2. Agregar evento\n3. Tiempo restante eventos\n4. Mostrar eventos\n-1. Volver\nSelecciona una opción: "))
                if opcionCalendario == 1:
                    mostrarCalendario(diaActual, mesActual, añoActual)
                elif opcionCalendario == 2:
                    agregarEvento(eventos)
                elif opcionCalendario == 3:
                    tiempoRestanteEventos(eventos)
                elif opcionCalendario == 4:
                    mostrarEventos(eventos)
                elif opcionCalendario == -1:
                    print("\nVolviendo al menú principal...")
        


        elif opcionMenuPrincipal == 4:
            ciclos_pomodoro = int(input("Ingrese la cantidad de ciclos Pomodoro (cada ciclo es 25 min de trabajo y 5 min de descanso): "))
            pomodoro(ciclos_pomodoro)

        elif opcionMenuPrincipal == -1:
            print("\nSaliendo del programa...")