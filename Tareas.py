import re

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
    tareaFiltrada = list(filter(lambda t: t['descripcion'] == descripcion, tareas)) #Filtra las tareas para eliminarla.
    if tareaFiltrada:
        tareas.remove(tareaFiltrada[0])
        print(f"\nTarea '{descripcion}' eliminada con éxito.")
    else:
        print(f"\nNo se encontró la tarea con descripción '{descripcion}'.")

def completarTarea(tareas, descripcion):
    # Marca una tarea como completa
    # Agarra la variable t y la compara con descripcion 
    tarea = next(filter(lambda t: t['descripcion'] == descripcion, tareas), None) #El next devuelve el primer elemento que encuentre
    if tarea:
        tarea['completa'] = True
        print(f"\nTarea '{descripcion}' marcada como completa.")
    else:
        print(f"\nTarea '{descripcion}' no encontrada.")

def buscarTarea(tareas, patron):
    # Busca tareas que coincidan con un patrón específico
    patronCompilado = re.compile(patron, re.IGNORECASE) #Evita el key sensitive 
    #Esto es una lista por comprension. Va a iterar cada elemento de la lista y el elemtno se asigna a la 
    #variable tarea. Usa el search en patron para encontrar una coincidencia en la descripcion.
    tareasEncontradas = [tarea for tarea in tareas if patronCompilado.search(tarea['descripcion'])] #Si el patron coincide la tarea se agrega a tareasEncontradas.
    if tareasEncontradas:
        print("\nTareas encontradas:")
        for tarea in tareasEncontradas:
            print(f"- {tarea['descripcion']}, Prioridad: {tarea['prioridad']}")
    else:
        print(f"\nNo se encontraron tareas que coincidan con el patrón '{patron}'.")