RED = "\033[31m"  # Rojo
GREEN = "\033[32m"  # Verde
RESET = "\033[0m"  # Reset del color

import datetime as d

def mostrarCalendario(dia, mes, año):
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

def ordenarEventos(listaEventos,usuario):
    """
    Ordena los eventos en la lista en base a la fecha más próxima.
    """
    listaEventos.sort(key=lambda evento: (evento["año"], evento["mes"], evento["dia"]))

def agregarEvento(listaEventos,usuario):
    """
    Agrega un nuevo evento a la lista de eventos, asegurando que la fecha no sea en el pasado.
    """
    try:
        diaEvento = int(input("\nIngrese día del evento: "))
        mesEvento = int(input("Ingrese mes del evento: "))
        añoEvento = int(input("Ingrese año del evento: "))
    except ValueError:
        print("La fecha debe ser números enteros.")
        return

    try:
        fechaEvento = d.datetime(añoEvento, mesEvento, diaEvento)
    except ValueError as e:
        print(f"\nError: {e}")
        return
    
    fechaActual = d.datetime.now()
    
    if fechaEvento < fechaActual:
        print("\nError: No se puede agregar un evento en el pasado.")
        return
    
    descripcion = input("Ingrese descripción del evento: ")
    
    # Crear diccionario del nuevo evento
    nuevo_evento = {
        "descripcion": descripcion,
        "dia": diaEvento,
        "mes": mesEvento,
        "año": añoEvento
    }
    
    listaEventos[usuario]["eventos"].append(nuevo_evento)
    ordenarEventos(listaEventos[usuario]["eventos"],usuario)  # Ordenar eventos al agregar uno nuevo
    print("\nEvento agregado exitosamente.")

def tiempoRestanteEventos(listaEventos,usuario):
    """
    Muestra cuánto tiempo queda para cada evento programado en la lista de eventos.
    """
    fechaActual = d.datetime.now()
    print("\nTiempo restante para los eventos:")
    for evento in listaEventos[usuario]["eventos"]:
        fechaEvento = d.datetime(evento["año"], evento["mes"], evento["dia"])
        diferencia = fechaEvento - fechaActual
        
        if diferencia.days == 1:
            print(f"- El día siguiente es el evento '{evento['descripcion']}'.")
        elif diferencia.days > 1:
            print(f"- Faltan {diferencia.days} días para el evento '{evento['descripcion']}'.")
        elif diferencia.days == 0:
            print(f"- Hoy es el evento '{evento['descripcion']}'.")
        else:
            print(f"- El evento '{evento['descripcion']}' ya ha pasado.")

def mostrarEventos(listaEventos,usuario):
    """
    Muestra todos los eventos, en rojo si ya pasaron o en verde si están por ocurrir.
    """
    fechaActual = d.datetime.now()
    if listaEventos[usuario]["eventos"]:
        print("\nEventos programados:")
        for evento in listaEventos[usuario]["eventos"]:
            fechaEvento = d.datetime(evento["año"], evento["mes"], evento["dia"])
            fechaEventoStr = f"{evento['dia']}/{evento['mes']}/{evento['año']}"
            
            if fechaEvento < fechaActual:  # Evento pasado.
                print(f"{RED}- {fechaEventoStr}: {evento['descripcion']} (Este evento ya pasó){RESET}")
            else:  # Evento futuro.
                print(f"{GREEN}- {fechaEventoStr}: {evento['descripcion']} (Este evento aún no ha pasado){RESET}")
    else:
        print("\nNo hay eventos programados.")

