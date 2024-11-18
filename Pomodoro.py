import time
def pomodoro(ciclos):
    """
    Objetivo: Planifica el tiempo de descanso y estudio de la sesion.
    Parametros de Entrada: Ingresa un entero que indica los ciclos pomodoro a realizar(25 
        minutos de estudio y 5 de descanso.)
    Parametros de Salida: No hay un valor de retorno, se muestra en la terminal el estado del ciclo 
        pomodoro.
    """
    
    for i in range(ciclos):
        print(f"Pomodoro {i + 1} - Sesión de estudio (25 minutos)")
        timer(25)  # 25 minutos de estudio
        if i < ciclos - 1:  # No hacer descanso después del último ciclo y terminarlo.
            print("Descanso (5 minutos)")
            timer(5)  # 5 minutos de descanso
    print("Todas las sesiones de Pomodoro finalizadas!")

def timer(minutosParametro):
    """
    Objetivo: Corre un cronometro en base al tiempo que se proporciono.
    Parametros de Entrada: Ingresan los minutos.
    Parametros de Salida: Se imprime el tiempo como string, no hay un return.
    """
    
    for i in range(minutosParametro * 60, 0, -1):
        segundos = int(i % 60)
        minutos = int(i / 60) % 60
        horas = i // 3600
        print(f"{horas:02}:{minutos:02}:{segundos:02}", end='\r')  
        time.sleep(1)  # Pausa de 1 segundo para simular el tiempo real
        