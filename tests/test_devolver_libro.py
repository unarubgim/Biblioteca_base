import unittest

import biblioteca


class TestDevolverLibro(unittest.TestCase):

    def setUp(self):
        biblioteca.libros.clear()
        biblioteca.usuarios.clear()

        if hasattr(biblioteca, "prestamos"):
            biblioteca.prestamos.clear()

    def test_devolver_libro_devuelve_mensaje_correcto(self):
        biblioteca.crear_libro(1, "Nada", "Carmen Laforet", "ISBN001", disponible=False)
        biblioteca.crear_usuario(1, "Unai", "Rubio", "unai@email.com")
        biblioteca.prestamos.append({"libro_id": 1, "usuario_id": 1})

        resultado = biblioteca.devolver_libro(1, 1)

        self.assertEqual(resultado, "Libro devuelto")

    def test_devolver_libro_cambia_disponible_a_true(self):
        biblioteca.crear_libro(1, "Nada", "Carmen Laforet", "ISBN001", disponible=False)
        biblioteca.crear_usuario(1, "Unai", "Rubio", "unai@email.com")
        biblioteca.prestamos.append({"libro_id": 1, "usuario_id": 1})

        biblioteca.devolver_libro(1, 1)

        libro = biblioteca.obtener_libro_por_id(1)
        self.assertTrue(libro.disponible)

    def test_devolver_libro_elimina_el_prestamo(self):
        biblioteca.crear_libro(1, "Nada", "Carmen Laforet", "ISBN001", disponible=False)
        biblioteca.crear_usuario(1, "Unai", "Rubio", "unai@email.com")
        biblioteca.prestamos.append({"libro_id": 1, "usuario_id": 1})

        biblioteca.devolver_libro(1, 1)

        self.assertEqual(len(biblioteca.prestamos), 0)

    def test_no_devolver_libro_inexistente(self):
        biblioteca.crear_usuario(1, "Unai", "Rubio", "unai@email.com")

        resultado = biblioteca.devolver_libro(99, 1)

        self.assertEqual(resultado, "Libro no encontrado")

    def test_no_devolver_usuario_inexistente(self):
        biblioteca.crear_libro(1, "Nada", "Carmen Laforet", "ISBN001", disponible=False)

        resultado = biblioteca.devolver_libro(1, 99)

        self.assertEqual(resultado, "Usuario no encontrado")

    def test_no_devolver_prestamo_inexistente(self):
        biblioteca.crear_libro(1, "Nada", "Carmen Laforet", "ISBN001", disponible=False)
        biblioteca.crear_usuario(1, "Unai", "Rubio", "unai@email.com")

        resultado = biblioteca.devolver_libro(1, 1)

        self.assertEqual(resultado, "Prestamo no encontrado")


if __name__ == "__main__":
    unittest.main()