RED = "\033[31m"  # Rojo
GREEN = "\033[32m"  # Verde
RESET = "\033[0m"  # Este reset reestablece el color.

import datetime as d



def mostrarCalendario(dia, mes, año):
    """
    Objetivo: Se imprime un calendario en la terminal del mes actual y marcando en rojo los dias pasados y en verde los dias por ocurrir.
    Parametros de Entrada: Ingresa el dia, mes y año actual.
    Parametros de Salida: No hay un return, solo se imprime el calendario.
    """
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

def ordenarEventos(diccionarioEventos):
    """
    Objetivo: Se ordena un diccionario de eventos en base a la fecha más proxima.
    Parametros de Entrada: Se ingresa el diccionario de eventos.
    Parametros de Salida: Se devuelve una copia del diccionario pero ordenado.
    """
    eventos_ordenados = dict(sorted(diccionarioEventos.items(), key=lambda item: (item[1][2], item[1][1], item[1][0])))
    return eventos_ordenados

def agregarEvento(diccionarioEventos):
    """
    Objetivos: Se agrega un nuevo evento al diccionario de eventos.
    Parametros de Entrada: Se ingresa el diccionario de eventos.
    Parametros de Salida: No hay un return, solo se actualiza el diccionario de eventos.
    """
    # Agrega un nuevo evento, asegurando que la fecha no sea del pasado.
    fecha = []
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
    
    fecha.append(diaEvento)
    fecha.append(mesEvento)
    fecha.append(añoEvento)
    desc=(input("Ingrese descripción del evento: "))
    diccionarioEventos[desc]=fecha
    diccionarioEventos=ordenarEventos(diccionarioEventos)
    print("\nEvento agregado exitosamente.")

def tiempoRestanteEventos(diccionarioEventos):
    """
    Objetivos: Se muestra por pantalla cuanto tiempo restante hay hasta que suceda el evento.
    Parametros de Entrada: Ingresamos el diccionario de eventos.
    Parametros de Salida: Nos hay return, se imprime por la terminal informacion.
    """
    # Muestra el tiempo restante para los eventos programados. Parametro es el diccionario de eventos.
    fechaActual = d.datetime.now()
    print("\nTiempo restante para los eventos:")
    for desc, evento in diccionarioEventos.items():
        fechaEvento = d.datetime(evento[2], evento[1], evento[0])
        diferencia = fechaEvento - fechaActual
        
        if diferencia.days == 1:
            print(f"- El día siguiente es el evento '{desc}'.")
        elif diferencia.days > 1:
            print(f"- Faltan {diferencia.days} días para el evento '{desc}'.")
        elif diferencia.days == 0:
            print(f"- Hoy es el evento '{desc}'.")
        else:
            print(f"- El evento '{desc}' ya ha pasado.")

def mostrarEventos(diccionarioEventos):
    """
    Objetivo: Se muestran los eventos guardados, en rojo si ya pasaron o en verde si estan por suceder.
    Parametros de Entrada: Ingresa el diccionario de eventos.
    Parametros de Salida: No hay un return, se imprime informacion por la terminal.
    """
    # Muestra todos los eventos programados, con colores según la fecha.
    fechaActual = d.datetime.now()
    if diccionarioEventos:
        print("\nEventos programados:")
        for desc,evento in diccionarioEventos.items():
            fechaEvento = d.datetime(evento[2], evento[1], evento[0])
            fechaEventoStr = f"{evento[0]}/{evento[1]}/{evento[2]}"
            
            if fechaEvento < fechaActual:  # Evento pasado.
                print(f"{RED}- {fechaEventoStr}: {desc} (Este evento ya paso){RESET}")
            else:  # Evento futuro.
                print(f"{GREEN}- {fechaEventoStr}: {desc} (Este evento aun no paso){RESET}")
    else:
        print("\nNo hay eventos programados.")