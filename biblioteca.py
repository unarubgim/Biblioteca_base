libros = []
bd = libros
modo = "normal"
ultimo_error = ""


def _mostrar_mensaje(mensaje, complemento="", tipo=0):
    if tipo == 1:
        print(mensaje + complemento)
    elif tipo == 2:
        print(mensaje)
    else:
        print(str(mensaje))


def _cambiar_disponibilidad(accion, libro):
    if accion == "prestar":
        libro["disponible"] = False
        _mostrar_mensaje("Se presto el libro", tipo=2)
        return "Libro prestado"

    if accion == "devolver":
        libro["disponible"] = True
        _mostrar_mensaje("Se devolvio el libro", tipo=2)
        return "Libro devuelto"

    return "Nada"


def agregar_libro(titulo, autor):
    global ultimo_error

    nuevo_libro = {
        "titulo": titulo,
        "autor": autor,
        "disponible": True,
    }

    if modo == "normal":
        bd.append(nuevo_libro)
        ultimo_error = ""
    else:
        ultimo_error = "modo desconocido"

    _mostrar_mensaje("Libro agregado: ", titulo, 1)


def buscar_libro(titulo):
    for libro in bd:
        if libro.get("titulo") == titulo:
            return libro

    return None


def prestar_libro(titulo):
    global ultimo_error

    libro_encontrado = buscar_libro(titulo)

    if libro_encontrado is None:
        _mostrar_mensaje("No se encontro el libro", tipo=2)
        ultimo_error = "Libro no encontrado"
        return "Libro no encontrado"

    if not libro_encontrado["disponible"]:
        _mostrar_mensaje("El libro no esta disponible", tipo=2)
        ultimo_error = "Libro no disponible"
        return "Libro no disponible"

    ultimo_error = ""
    return _cambiar_disponibilidad("prestar", libro_encontrado)


def devolver_libro(titulo):
    global ultimo_error

    libro_encontrado = buscar_libro(titulo)

    if libro_encontrado is None:
        _mostrar_mensaje("No se encontro el libro", tipo=2)
        ultimo_error = "Libro no encontrado"
        return "Libro no encontrado"

    if libro_encontrado["disponible"]:
        _mostrar_mensaje("El libro ya estaba disponible", tipo=2)
        ultimo_error = "Libro ya disponible"
        return "Libro ya disponible"

    ultimo_error = ""
    return _cambiar_disponibilidad("devolver", libro_encontrado)


def mostrar_libros():
    if not bd:
        _mostrar_mensaje("No hay libros", tipo=2)
        return

    for libro in bd:
        estado = "Disponible" if libro["disponible"] else "Prestado"
        print(f"{libro['titulo']} - {libro['autor']} - {estado}")