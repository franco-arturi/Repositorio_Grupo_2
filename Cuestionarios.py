def crearCuestionario(diccionarioCUestionarios):
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
    diccionarioCUestionarios[nombreCuestionario]=cuestionario
    return 

def mostrarPregunta(pregunta, opciones):
    # Muestra una pregunta del cuestionario con sus opciones
    print(f"\n{pregunta}")
    for i, opcion in enumerate(opciones, 1): #permite iterar sobre una secuencia l mismo tiempo y
        # obtener tanto el índice de cada elemento como el propio elemento
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