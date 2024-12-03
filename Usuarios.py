import re

import re  # Asegúrate de importar re para las validaciones de clave

def cargarUsuario(diccionarioUsuarios, usuActual):
    """
    Objetivo: Se crea un usuario nuevo verificando los datos ingresados.
    Parametros de Entrada: Ingresamos el diccionario de usuarios existente y el usuario actual.
    Parametros de Salida: Si bien no hay un return, se actualizan los datos del usuario actual.
    """
    nombre = ""  # Inicializamos el nombre como vacío
    while not nombre.strip():
        nombre = input("\nIngrese el nombre del nuevo usuario: ").strip()
        if not nombre:
            print("Error: El nombre de usuario no puede estar vacío.")
        elif nombre in diccionarioUsuarios:
            # Verifica que el nombre de usuario no exista
            print("Error: El nombre de usuario ya existe.")
            return
    
    clave = input("Ingrese clave numérica (Debe contener al menos una mayúscula, al menos un número y mínimo 8 caracteres): ")
    patronMayuscula = "[A-Z]"
    patronNumero = "[0-9]"
    if re.search(patronMayuscula, clave) and re.search(patronNumero, clave) and len(clave) >= 8:
        diccionarioUsuarios[nombre] = {
            "eventos": [],
            "cuestionarios": {},
            "tareas": [],
            "contraseña": clave
        }
        print("\nUsuario creado exitosamente.")
        usuActual[:] = [nombre, clave]
    else:
        print("\nError: Formato de la clave erróneo.")
        return
       

def cambiarUsuario(diccionarioUsuarios, usuActual):
    """
    Objetivo: La usamos para cambiar el usuario que estamos usando actualmente, sin crear otro. 
    Parametros de Entrada: Ingresamos el diccionario de usuarios y el usuario actual.
    Parametros de Salida: No hay return, se alctualizan los datos del usuario.
    """
    nuevoUsuario = input("\nIngrese nombre de usuario: ")
    
    if nuevoUsuario in diccionarioUsuarios:
        contraseña = (input("Ingrese contraseña: "))
        if diccionarioUsuarios[nuevoUsuario]["contraseña"] == contraseña:
            usuActual[:] = [nuevoUsuario,contraseña]
            print("\nUsuario cambiado exitosamente.")
        else:
            print("\nContraseña incorrecta .")
        return
    print("\nUsuario no encontrado.")

def eliminarUsuario(diccionarioUsuarios, nombre, contraseña, usuActual):
    """
    Objetivo: Borramos el usuario indicado y comprobando los datos.
    Parametros de Entrada: Ingresamos el diccionario de usuarios, el nombre y contraseña del usuario a eliminar y el
    usuario actual.  
    Parametros de Salida: No hay un return solo se borra del diccionario de usuarios el indicado.
    """
    if nombre in diccionarioUsuarios  and diccionarioUsuarios[nombre]["contraseña"] == contraseña :
            del diccionarioUsuarios[nombre]
            if nombre == usuActual[0]:
                usuActual[:] = [0, 0]
            print(f"\nUsuario {nombre} eliminado con éxito.")
            return
    print(f"\nUsuario {nombre} no encontrado o contraseña incorrecta.")