import unittest

import biblioteca


class TestIntegracion(unittest.TestCase):

    def setUp(self):
        biblioteca.libros.clear()
        biblioteca.usuarios.clear()
        biblioteca.prestamos.clear()
        biblioteca.logs.clear()

    def test_operar_crear_libro(self):
        datos = {
            "id": 1,
            "titulo": "Nada",
            "autor": "Carmen Laforet",
            "isbn": "ISBN001"
        }

        libro = biblioteca.operar("crear_libro", datos)

        self.assertEqual(libro.titulo, "Nada")

    def test_operar_crear_usuario(self):
        datos = {
            "id": 1,
            "nombre": "Unai",
            "apellidos": "Rubio",
            "email": "unai@email.com"
        }

        usuario = biblioteca.operar("crear_usuario", datos)

        self.assertEqual(usuario.nombre, "Unai")

    def test_operar_prestar_libro(self):
        biblioteca.crear_libro(1, "Nada", "Carmen Laforet", "ISBN001")
        biblioteca.crear_usuario(1, "Unai", "Rubio", "unai@email.com")

        datos = {
            "libro_id": 1,
            "usuario_id": 1
        }

        resultado = biblioteca.operar("prestar_libro", datos)

        self.assertEqual(resultado, "Libro prestado")

    def test_operar_devolver_libro(self):
        biblioteca.crear_libro(1, "Nada", "Carmen Laforet", "ISBN001")
        biblioteca.crear_usuario(1, "Unai", "Rubio", "unai@email.com")
        biblioteca.prestar_libro(1, 1)

        datos = {
            "libro_id": 1,
            "usuario_id": 1
        }

        resultado = biblioteca.operar("devolver_libro", datos)

        self.assertEqual(resultado, "Libro devuelto")

    def test_operar_accion_inexistente_devuelve_false(self):
        resultado = biblioteca.operar("accion_inventada", {})

        self.assertFalse(resultado)


if __name__ == "__main__":
    unittest.main()