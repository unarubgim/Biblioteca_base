import unittest

import biblioteca


class TestPrestarLibro(unittest.TestCase):

    def setUp(self):
        biblioteca.libros.clear()
        biblioteca.usuarios.clear()

        if hasattr(biblioteca, "prestamos"):
            biblioteca.prestamos.clear()

    def test_prestar_libro_devuelve_mensaje_correcto(self):
        biblioteca.crear_libro(1, "Nada", "Carmen Laforet", "ISBN001")
        biblioteca.crear_usuario(1, "Unai", "Rubio", "unai@email.com")

        resultado = biblioteca.prestar_libro(1, 1)

        self.assertEqual(resultado, "Libro prestado")

    def test_prestar_libro_cambia_disponible_a_false(self):
        biblioteca.crear_libro(1, "Nada", "Carmen Laforet", "ISBN001")
        biblioteca.crear_usuario(1, "Unai", "Rubio", "unai@email.com")

        biblioteca.prestar_libro(1, 1)

        libro = biblioteca.obtener_libro_por_id(1)
        self.assertFalse(libro.disponible)


    def test_prestar_libro_guarda_el_prestamo(self):
        biblioteca.crear_libro(1, "Nada", "Carmen Laforet", "ISBN001")
        biblioteca.crear_usuario(1, "Unai", "Rubio", "unai@email.com")

        biblioteca.prestar_libro(1, 1)

        self.assertEqual(len(biblioteca.prestamos), 1)

    def test_no_prestar_libro_inexistente(self):
        biblioteca.crear_usuario(1, "Unai", "Rubio", "unai@email.com")

        resultado = biblioteca.prestar_libro(99, 1)

        self.assertEqual(resultado, "Libro no encontrado")

    def test_no_prestar_usuario_inexistente(self):
        biblioteca.crear_libro(1, "Nada", "Carmen Laforet", "ISBN001")

        resultado = biblioteca.prestar_libro(1, 99)

        self.assertEqual(resultado, "Usuario no encontrado")

    def test_no_prestar_usuario_deshabilitado(self):
        biblioteca.crear_libro(1, "Nada", "Carmen Laforet", "ISBN001")
        biblioteca.crear_usuario(1, "Unai", "Rubio", "unai@email.com", habilitado=False)

        resultado = biblioteca.prestar_libro(1, 1)

        self.assertEqual(resultado, "Usuario no habilitado")

    def test_no_prestar_libro_no_disponible(self):
        biblioteca.crear_libro(1, "Nada", "Carmen Laforet", "ISBN001", disponible=False)
        biblioteca.crear_usuario(1, "Unai", "Rubio", "unai@email.com")

        resultado = biblioteca.prestar_libro(1, 1)

        self.assertEqual(resultado, "Libro no disponible")


if __name__ == "main":
    unittest.main()
