def crearCuestionario(diccionarioCUestionarios,usuario):
    """
    Objetivo: Solicitar informacion y crear un cuestionario nuevo.
    Parametros de Entrada: Ingresamos el diccionario usado para contener los diferentes cuestionarios.
    Parametros de Salida: No hay valor en el return, pero la funcion se encarga de agregar 
        el cuestionario creado al diccionario de cuestionarios.
    """

    
    # Ingresamo tematica del cuestionario, cantidad de preguntas y los detalles de cada una.
    nombreCuestionario=(input("Ingrese tematica del cuestionario.")).title()    
    cuestionario = []
    try:
        numPreguntas = int(input("\n¿Número de preguntas para el cuestionario? "))
    except ValueError:
        pregunta("Debe ingresar solo números.")
        return
    for i in range(numPreguntas):
        print(f"\nCreando pregunta {i + 1}:")
        pregunta = input("Escribe la pregunta: ")
        print("Nota: Solo se permiten 3 opciones de respuesta.")
        opciones = [input(f"Opción {j + 1}: ") for j in range(3)] 
        try:
            correcta = int(input("¿Cuál es la opción correcta (1, 2 o 3)? "))
        except ValueError:
            print("Debe ingresar solo números.")
            return
        cuestionario.append({"pregunta": pregunta, "opciones": opciones, "correcta": correcta})
    
    print("\nCuestionario creado exitosamente.")
    diccionarioCUestionarios[usuario]["cuestionarios"][nombreCuestionario]=cuestionario
    return 

def mostrarPregunta(pregunta, opciones):
    """
    Objetivo: Muestra una pregunta y sus opciones para luego ingresar la respuesta del usuario.
    Parametros de Entrada: Como entrada tomamos la pregunta y las opciones para imprimirlas.
    Parametros de Salida: Como parametro de salida devolvemos la respuesta a la pregunta.
    """
    
    print(f"\n{pregunta}")
    for i, opcion in enumerate(opciones, 1): #permite iterar sobre una secuencia l mismo tiempo y
        # obtener tanto el índice de cada elemento como el propio elemento
        print(f"{i}. {opcion}")
    try:
        eleccion = int(input("Selecciona la opción correcta (1, 2 o 3): "))
    except ValueError:
        print("Debe ingresar solo números.")
        return
    return eleccion

def ejecutarCuestionario(cuestionario):

    """
    Objetivo: Utiliza la funcion mostrarPregunta y corre el cuestionario con sus verificando las respuestas
        y dando puntos.
    Parametros de Entrada: Ingresamos el cuestionario a ejecutar.
    Parametros de Salida: No hay un return explicito, pero al finalizar se devuelve la puntuacion del cuestionario.
    """    
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