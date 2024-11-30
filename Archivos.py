import json
import datetime as d

def cargar_datos(ARCHIVO_JSON):
    """
    Objetivo: Se cargan o crean datos del archivo JSON.
    Parametros de Entrada: La variable global con el nombre del archivo JSON.
    Parametros de Salida: Se devuelven los datos del archivo JSON.
    """
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
                        "contraseña":"A11111111"}
        }
        
        # Esto guarda la estructura inicial en el archivo
        guardar_datos(datos,ARCHIVO_JSON)
        print("Archivo de datos no encontrado. Se ha creado uno nuevo.")
    return datos

# Función para guardar datos en el archivo JSON
def guardar_datos(datos,ARCHIVO_JSON):
    """
    Objetivo: Se llama cuando se quiere guardar los datos en el archivo JSON.
    Parametros de Entrada: Ingresamos los datos del archivo.
    Parametros de Salida: Si bien no hay ninguno return, se actualiza el JSON.
    """
    with open(ARCHIVO_JSON, 'w') as archivo:
        json.dump(datos, archivo, indent=4)
    print("Datos guardados exitosamente.")

# Función para registrar actividad en el log
def registrar_actividad(mensaje,ARCHIVO_LOG):
    """
    Objetivo: Se registra la actividad en un archivo.
    Parametros de Entrada: Entra el mensaje de actividad como parametro.
    Parametros de Salida: Si bien no hay un return, se ingresan los datos al archivo.
    """
    with open(ARCHIVO_LOG, 'a') as log_file:
        timestamp = d.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"{timestamp} - {mensaje}\n")
