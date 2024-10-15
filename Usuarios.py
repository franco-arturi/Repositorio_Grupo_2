

def cargarUsuario(listaUsuarios,usuActual):
    """
    Objetivo: Se crea un usuario nuevo verificando los datos ingresados.
    Parametros de Entrada: Ingresamos la lista de usuarios existente y el usuario actual.
    Parametros de Salida: Si bien no hay un return, se actualizan los datos del usuario actual.
    """
   
    nombre = input("\nIngrese el nombre del nuevo usuario: ")
    if any(usuario[0] == nombre for usuario in listaUsuarios):
        #Se chequea que el nombre de usuario no exista.
        print("\nError: El nombre de usuario ya existe.")
        return
    
    clave = int(input("Ingrese clave numérica: "))
    usuario = [nombre, clave]
    listaUsuarios.append(usuario)
    print("\nUsuario creado exitosamente.")
    usuActual[:] = usuario

def cambiarUsuario(listaUsuarios, usuActual):
    """
    Objetivo: La usamos para cambiar el usuario que estamos usando actualmente, sin crear otro. 
    Parametros de Entrada: Ingresamos la lista de usuarios y el usuario actual.
    Parametros de Salida: No hay return, se alctualizan los datos del usuario.
    """
    nuevoUsuario = input("\nIngrese nombre de usuario: ")
    for usuario in listaUsuarios:
        if nuevoUsuario == usuario[0]:
            contraseña = int(input("Ingrese contraseña: "))
            if contraseña == usuario[1]:
                usuActual[:] = usuario
                print("\nUsuario cambiado exitosamente.")
            else:
                print("\nContraseña incorrecta.")
            return
    print("\nUsuario no encontrado.")

def eliminarUsuario(listaUsuarios, nombre, contraseña, usuActual):
    """
    Objetivo: Borramos el usuario indicado y comprobando los datos.
    Parametros de Entrada: Ingresamos la lista de usuarios, el nombre y contraseña del usuario a eliminar y 
        el usuario actual.  
    Parametros de Salida: No hay un return solo se borra de la lista de usuarios el indicado.
    """
    for usuario in listaUsuarios:
        if nombre == usuario[0] and contraseña == usuario[1]:
            listaUsuarios.remove(usuario)
            if usuario == usuActual:
                usuActual[:] = [0, 0]
            print(f"\nUsuario {nombre} eliminado con éxito.")
            return
    print(f"\nUsuario {nombre} no encontrado o contraseña incorrecta.")