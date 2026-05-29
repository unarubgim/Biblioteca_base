libros = []
prestamos = []


class Libro:

    def __init__(self, id, titulo, autor, isbn="", disponible=True):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    def __getitem__(self, clave):
        if clave == "id":
            return self.id

        if clave == "titulo":
            return self.titulo

        if clave == "autor":
            return self.autor

        if clave == "isbn":
            return self.isbn

        if clave == "disponible":
            return self.disponible

        raise KeyError(clave)

    def __setitem__(self, clave, valor):
        if clave == "id":
            self.id = valor
        elif clave == "titulo":
            self.titulo = valor
        elif clave == "autor":
            self.autor = valor
        elif clave == "isbn":
            self.isbn = valor
        elif clave == "disponible":
            self.disponible = valor
        else:
            raise KeyError(clave)


def agregar_libro(titulo, autor):
    nuevo_id = len(libros) + 1
    libro = Libro(nuevo_id, titulo, autor)
    libros.append(libro)


def prestar_libro(titulo):
    for libro in libros:
        if libro.titulo == titulo:
            if libro.disponible:
                libro.disponible = False
                return "Libro prestado"

            return "Libro no disponible"

    return "Libro no encontrado"


def devolver_libro(libro_id, usuario_id=None):
    if usuario_id is None:
        titulo = libro_id

        for libro in libros:
            if libro.titulo == titulo:
                if not libro.disponible:
                    libro.disponible = True
                    return "Libro devuelto"

                return "El libro no estaba prestado"

        return "Libro no encontrado"

    libro = obtener_libro_por_id(libro_id)
    usuario = obtener_usuario_por_id(usuario_id)

    if libro is None:
        return "Libro no encontrado"

    if usuario is None:
        return "Usuario no encontrado"

    for prestamo in prestamos:
        if prestamo["libro_id"] == libro_id and prestamo["usuario_id"] == usuario_id:
            prestamos.remove(prestamo)
            libro.disponible = True
            return "Libro devuelto"

    return "Prestamo no encontrado"


def crear_libro(id, titulo, autor, isbn, disponible=True):
    libro = Libro(id, titulo, autor, isbn, disponible)
    libros.append(libro)
    return libro


def obtener_libro_por_id(id):
    for libro in libros:
        if libro.id == id:
            return libro

    return None


def buscar_libro_por_id(id):
    return obtener_libro_por_id(id)


def actualizar_libro(id, titulo=None, autor=None, isbn=None, disponible=None):
    libro = obtener_libro_por_id(id)

    if libro is None:
        return False

    if titulo is not None:
        libro.titulo = titulo

    if autor is not None:
        libro.autor = autor

    if isbn is not None:
        libro.isbn = isbn

    if disponible is not None:
        libro.disponible = disponible

    return True


def eliminar_libro(id):
    libro = obtener_libro_por_id(id)

    if libro is None:
        return False

    libros.remove(libro)
    return True


def buscar_libros_por_titulo(titulo):
    resultado = []

    for libro in libros:
        if libro.titulo == titulo:
            resultado.append(libro)

    return resultado


def buscar_libros_por_autor(autor):
    resultado = []

    for libro in libros:
        if libro.autor == autor:
            resultado.append(libro)

    return resultado


def buscar_libros_por_disponibilidad(disponible):
    resultado = []

    for libro in libros:
        if libro.disponible == disponible:
            resultado.append(libro)

    return resultado


def buscar_libros_por_coincidencia(texto):
    resultado = []
    texto = texto.lower()

    for libro in libros:
        titulo = libro.titulo.lower()
        autor = libro.autor.lower()

        if texto in titulo or texto in autor:
            resultado.append(libro)

    return resultado


usuarios = []


class Usuario:

    def __init__(self, id, nombre, apellidos, email, habilitado=True):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.habilitado = habilitado


def crear_usuario(id, nombre, apellidos, email, habilitado=True):
    usuario = Usuario(id, nombre, apellidos, email, habilitado)
    usuarios.append(usuario)
    return usuario


def obtener_usuario_por_id(id):
    for usuario in usuarios:
        if usuario.id == id:
            return usuario

    return None


def actualizar_usuario(id, nombre=None, apellidos=None, email=None, habilitado=None):
    usuario = obtener_usuario_por_id(id)

    if usuario is None:
        return False

    if nombre is not None:
        usuario.nombre = nombre

    if apellidos is not None:
        usuario.apellidos = apellidos

    if email is not None:
        usuario.email = email

    if habilitado is not None:
        usuario.habilitado = habilitado

    return True


def eliminar_usuario(id):
    usuario = obtener_usuario_por_id(id)

    if usuario is None:
        return False

    usuarios.remove(usuario)
    return True


def habilita_usuario(id):
    usuario = obtener_usuario_por_id(id)

    if usuario is None:
        return False

    usuario.habilitado = True
    return True


def deshabilita_usuario(id):
    usuario = obtener_usuario_por_id(id)

    if usuario is None:
        return False

    usuario.habilitado = False
    return True


def buscar_usuarios_por_nombre(nombre):
    resultado = []

    for usuario in usuarios:
        if usuario.nombre == nombre:
            resultado.append(usuario)

    return resultado


def buscar_usuarios_por_apellidos(apellidos):
    resultado = []

    for usuario in usuarios:
        if usuario.apellidos == apellidos:
            resultado.append(usuario)

    return resultado


def buscar_usuario_por_email(email):
    for usuario in usuarios:
        if usuario.email == email:
            return usuario

    return None