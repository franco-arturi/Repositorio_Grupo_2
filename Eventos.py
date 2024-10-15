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

def ordenarEventos(listaEventos):
    """
    Objetivo: Se ordena la lista de eventos en base a la fecha mas proxima.
    Parametros de Entrada: Se ingresa la lista de eventos.
    Parametros de Salida: No hay return, solo se actualiza la lista de eventos.
    """
    listaEventos.sort(key=lambda x: (x[2], x[1], x[0]))

def agregarEvento(listaEventos):
    """
    Objetivos: Se agrega un nuevo evento a la lista de eventos.
    Parametros de Entrada: Se ingresa la lista de eventos.
    Parametros de Salida: No hay un return, solo se actualiza la lista de eventos.
    """
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
    listaEventos.append(evento)
    ordenarEventos(listaEventos)
    print("\nEvento agregado exitosamente.")

def tiempoRestanteEventos(listaEventos):
    """
    Objetivos: Se muestra por pantalla cuanto tiempo restante hay hasta que suceda el evento.
    Parametros de Entrada: Ingresamos la lista de eventos.
    Parametros de Salida: Nos hay return, se imprime por la terminal informacion.
    """
    # Muestra el tiempo restante para los eventos programados. Parametro es la lista de eventos.
    fechaActual = d.datetime.now()
    print("\nTiempo restante para los eventos:")
    for evento in listaEventos:
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

def mostrarEventos(listaEventos):
    """
    Objetivo: Se muestran los eventos guardados, en rojo si ya pasaron o en verde si estan por suceder.
    Parametros de Entrada: Ingresa la lista de eventos.
    Parametros de Salida: No hay un return, se imprime informacion por la terminal.
    """
    # Muestra todos los eventos programados, con colores según la fecha.
    fechaActual = d.datetime.now()
    if listaEventos:
        print("\nEventos programados:")
        for evento in listaEventos:
            fechaEvento = d.datetime(evento[2], evento[1], evento[0])
            fechaEventoStr = f"{evento[0]}/{evento[1]}/{evento[2]}"
            
            if fechaEvento < fechaActual:  # Evento pasado.
                print(f"{RED}- {fechaEventoStr}: {evento[3]} (Este evento ya paso){RESET}")
            else:  # Evento futuro.
                print(f"{GREEN}- {fechaEventoStr}: {evento[3]} (Este evento aun no paso){RESET}")
    else:
        print("\nNo hay eventos programados.")