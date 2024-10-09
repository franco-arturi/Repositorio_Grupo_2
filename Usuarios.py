def cargarUsuario(listaUsuarios,usuActual):
    #Input, lista de usuarios. Se crea un nuevo usuario con su nombre y contraseña ingresadas por teclado.
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
    # Cambia al usuario actual ingresando nombre y contraseña.
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
    # Elimina un usuario si se proporciona el nombre y contraseña correctos.
    for usuario in listaUsuarios:
        if nombre == usuario[0] and contraseña == usuario[1]:
            listaUsuarios.remove(usuario)
            if usuario == usuActual:
                usuActual[:] = [0, 0]
            print(f"\nUsuario {nombre} eliminado con éxito.")
            return
    print(f"\nUsuario {nombre} no encontrado o contraseña incorrecta.")