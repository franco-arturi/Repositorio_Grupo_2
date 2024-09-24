import datetime as d
import time
import re

# FUNCIONES


#Tecnica Pomodoro

def pomodoro(ciclos):
    #Input es la cantidad de ciclos a de 25 minutos de estudio y 5 de descanso.
    for i in range(ciclos):
        print(f"Pomodoro {i + 1} - Sesión de estudio (25 minutos)")
        timer(25)  # 25 minutos de estudio
        if i < ciclos - 1:  # No hacer descanso después del último ciclo y terminarlo.
            print("Descanso (5 minutos)")
            timer(5)  # 5 minutos de descanso
    print("Todas las sesiones de Pomodoro finalizadas!")

def timer(tiempo):
    #Se ingresa la cantidad de tiempo para el timer
    for i in range(tiempo * 60, 0, -1):
        segundos = int(i % 60)
        minutos = int(i / 60) % 60
        horas = i // 3600
        print(f"{horas:02}:{minutos:02}:{segundos:02}", end='\r')  
        time.sleep(1)  # Pausa de 1 segundo para simular el tiempo real
        

# Manejo de Tareas
def crearTarea(tareas, descripcion, prioridad): 
    # Crea una nueva tarea con descripción y prioridad.
    if isinstance(descripcion, str) and isinstance(prioridad, int):
        nuevaTarea = {"descripcion": descripcion, "prioridad": prioridad, "completa": False}
        tareas.append(nuevaTarea)
        print(f"\nTarea '{descripcion}' creada con prioridad {prioridad}.")
    else:
        print("\nError: Descripción debe ser una cadena de texto y la prioridad un entero.")

def eliminarTarea(tareas, descripcion):
    # Elimina una tarea buscandola por su descripción, en la lista de tareas.
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
    #Input, lista de usuarios. Se crea un nuevo usuario con su nombre y contraseña ingresadas por teclado.
    nombre = input("\nIngrese el nombre del nuevo usuario: ")
    if any(usuario[0] == nombre for usuario in listado):
        #Se chequea que el nombre de usuario no exista.
        print("\nError: El nombre de usuario ya existe.")
        return
    
    clave = int(input("Ingrese clave numérica: "))
    usuario = [nombre, clave]
    listado.append(usuario)
    print("\nUsuario creado exitosamente.")
    usuarioActual[:] = usuario

def cambiarUsuario(listado, usuarioActual):
    # Cambia al usuario actual ingresando nombre y contraseña.
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
    # Elimina un usuario si se proporciona el nombre y contraseña correctos.
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
    # Muestra el calendario del mes y año especificados, con el input de la fecha del dia.
    meses = [["Enero", 31], ["Febrero", 28], ["Marzo", 31], ["Abril", 30], ["Mayo", 31],
             ['Junio', 30], ['Julio', 31], ['Agosto', 31], ["Septiembre", 30], ['Octubre', 31],
             ["Noviembre", 30], ['Diciembre', 31]]
    print(f"\n             {meses[mes - 1][0]} {año}")
    
    contador = 0
    for i in range(meses[mes - 1][1]):
        if contador < 6:
            if i + 1 < dia:
                # El dia se imprime en rojo si ya paso. Reset deja el color original de la fuente.
                print(f"{RED}{i + 1}{RESET}".center(15), end="")
            else:
                # El dia se imprime en verde si no paso. Reset deja el color original de la fuente.
                print(f"{GREEN}{i + 1}{RESET}".center(15), end="")
            contador += 1
        else:
            if i + 1 < dia:
                print(f"{RED}{i + 1}{RESET}".center(15))
            else:
                print(f"{GREEN}{i + 1}{RESET}".center(15))
            contador = 0

def ordenarEventos(eventos):
    # Ordena los eventos por fecha, el input es la lista de eventos.
    eventos.sort(key=lambda x: (x[2], x[1], x[0]))

def agregarEvento(eventos):
    # Agrega un nuevo evento, asegurando que la fecha no sea del pasado.
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
    # Muestra el tiempo restante para los eventos programados.
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
    # Muestra todos los eventos programados, con colores según la fecha.
    fechaActual = d.datetime.now()
    if eventos:
        print("\nEventos programados:")
        for evento in eventos:
            fechaEvento = d.datetime(evento[2], evento[1], evento[0])
            fechaEventoStr = f"{evento[0]}/{evento[1]}/{evento[2]}"
            
            if fechaEvento < fechaActual:  # Evento pasado.
                print(f"{RED}- {fechaEventoStr}: {evento[3]} (Este evento ya paso){RESET}")
            else:  # Evento futuro.
                print(f"{GREEN}- {fechaEventoStr}: {evento[3]} (Este evento aun no paso){RESET}")
    else:
        print("\nNo hay eventos programados.")

# Cuestionarios
def crearCuestionario(diccionario):
    # Se ingresa un diccionario de los cuestionarios, donde vamos a guardar el cuestionario creado.
    # Ingresamo tematica del cuestionario, cantidad de preguntas y los detalles de cada una.
    nombreCuestionario=input("Ingrese tematica del cuestionario.")    
    cuestionario = []
    numPreguntas = int(input("\n¿Número de preguntas para el cuestionario? "))
    
    for i in range(numPreguntas):
        print(f"\nCreando pregunta {i + 1}:")
        pregunta = input("Escribe la pregunta: ")
        print("Nota: Solo se permiten 3 opciones de respuesta.")
        opciones = [input(f"Opción {j + 1}: ") for j in range(3)]
        correcta = int(input("¿Cuál es la opción correcta (1, 2 o 3)? "))
        cuestionario.append({"pregunta": pregunta, "opciones": opciones, "correcta": correcta})
    
    print("\nCuestionario creado exitosamente.")
    diccionario[nombreCuestionario]=cuestionario
    return 

def mostrarPregunta(pregunta, opciones):
    # Muestra una pregunta del cuestionario con sus opciones
    print(f"\n{pregunta}")
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")
    eleccion = int(input("Selecciona la opción correcta (1, 2 o 3): "))
    return eleccion

def ejecutarCuestionario(cuestionario):
    # Inicia el cuestionario y evalúa las respuestas
    
    puntuacion = 0
    print("\nIniciando cuestionario...")
    for pregunta in cuestionario:
        eleccion = mostrarPregunta(pregunta["pregunta"], pregunta["opciones"])
        if eleccion == pregunta["correcta"]:
            print("Correcto!")
            puntuacion += 1
        else:
            print("Incorrecto")
    print(f"\nTu puntuación final es: {puntuacion}/{len(cuestionario)}")



# DATOS
RED = "\033[31m"  # Rojo
GREEN = "\033[32m"  # Verde
RESET = "\033[0m"  # Este reset reestablece el color.
diaActual = d.date.today().day # Dia de hoy.
mesActual = d.date.today().month # Mes actual.
añoActual = d.date.today().year # Año actual.
eventos = [[9, 9, 2024, "Examen de Programación"],[10, 9, 2024, "Examen de Química"], [12, 9, 2024, "Examen de Física"],[28, 9, 2024, "Examen de matematica"]]
# Matriz de eventos(dia, mes, año, descripcion)
usuarios = [["usuario1", 1234], ["usuario2", 5678]]
# Matriz de usuarios(nombre, contraseña)
usuarioActual = [0, 0]
# Usuario actual
cuestionarios = {'Matematica': [{'pregunta': '1+1', 'opciones': ['2', '4', '1'], 'correcta': 1}, {'pregunta': '5*5', 'opciones': ['25', '30', '20'], 'correcta': 1}, {'pregunta': '2**2', 'opciones': ['4', '6', '12'], 'correcta': 1}]}
tareas = []


# MAIN
opcionMenuPrincipal = 0

while opcionMenuPrincipal != -1:
    if usuarioActual == [0, 0]:
        opcionUsuario = int(input("\n 1. Ingresar usuario\n 2. Crear usuario\n-1. Salir\nSelecciona una opción: "))
        if opcionUsuario == 1:
            cambiarUsuario(usuarios, usuarioActual)
        elif opcionUsuario == 2:
            cargarUsuario(usuarios)
        elif opcionUsuario == -1:
            print("\nSaliendo del programa...")
            opcionMenuPrincipal = -1
    else:
        opcionMenuPrincipal = int(input("\n 1. Administrar usuarios\n 2. Calendario y eventos\n 3. Cuestionarios\n 4. Técnica Pomodoro\n 5. Administrar tareas\n-1. Salir\nSelecciona una opción: "))
        
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
        
        elif opcionMenuPrincipal == 3:
            opcionCuestionario = 0
            while opcionCuestionario != -1:
                opcionCuestionario=int(input("\nIngrese operacion: \n 1) Crear Cuestionario. \n 2) Ejecutar cuestionario.\n-1) Salir\nOpcion:  "))
                if opcionCuestionario==1:
                    crearCuestionario(cuestionarios)
                    
                elif opcionCuestionario == 2:
                    print("\nCuestionarios disponibles:")
                    for cuest in cuestionarios.keys():
                        print(cuest)
                    nom = input("Ingrese nombre de cuestionario a ejecutar: ")
        
                    cuestionario = cuestionarios.get(nom)
                    if cuestionario != None:
                        ejecutarCuestionario(cuestionario)
                    elif cuestionario == None:
                        print("Cuestionario inexistente.")

        elif opcionMenuPrincipal == 4:
            ciclos_pomodoro = int(input("\nIngrese la cantidad de ciclos Pomodoro (cada ciclo es 25 min de trabajo y 5 min de descanso): "))
            pomodoro(ciclos_pomodoro)

        elif opcionMenuPrincipal == 5:
            # Submenú de tareas
            opcionTareas = int(input("\n1. Crear tarea\n2. Completar tarea\n3. Eliminar tarea\n4. Buscar tarea\n5. Ver todas las tareas\nSelecciona una opción: "))
            if opcionTareas == 1:
                descripcion = input("Descripción de la tarea: ")
                prioridad = int(input("Prioridad de la tarea (1-5): "))
                crearTarea(tareas, descripcion, prioridad)
            elif opcionTareas == 2:
                descripcion = input("Descripción de la tarea a completar: ")
                completarTarea(tareas, descripcion)
            elif opcionTareas == 3:
                descripcion = input("Descripción de la tarea a eliminar: ")
                eliminarTarea(tareas, descripcion)
            elif opcionTareas == 4:
                patron = input("Ingrese un patrón para buscar: ")
                buscarTarea(tareas, patron)
            elif opcionTareas == 5:
                print("\nLista de todas las tareas:")
                for tarea in tareas:
                    estado = "Completa" if tarea["completa"] else "Incompleta"
                    print(f"- {tarea['descripcion']} (Prioridad: {tarea['prioridad']}) - {estado}")


        elif opcionMenuPrincipal == -1:
            print("\nSaliendo del programa...")