import unittest

import biblioteca


class TestBiblioteca(unittest.TestCase):

    def setUp(self):
        biblioteca.libros.clear()

    def test_lista_libros_empieza_vacia(self):
        self.assertEqual(len(biblioteca.libros), 0)

    def test_agregar_libro_guarda_titulo_autor_y_estado_disponible(self):
        biblioteca.agregar_libro("El Quijote", "Miguel de Cervantes")

        self.assertEqual(len(biblioteca.libros), 1)
        self.assertEqual(biblioteca.libros[0]["titulo"], "El Quijote")
        self.assertEqual(biblioteca.libros[0]["autor"], "Miguel de Cervantes")
        self.assertTrue(biblioteca.libros[0]["disponible"])

    def test_agregar_un_libro_aumenta_la_lista(self):
        biblioteca.agregar_libro("Nada", "Carmen Laforet")

        self.assertEqual(len(biblioteca.libros), 1)

    def test_agregar_dos_libros_aumenta_la_lista(self):
        biblioteca.agregar_libro("Nada", "Carmen Laforet")
        biblioteca.agregar_libro("La colmena", "Camilo Jose Cela")

        self.assertEqual(len(biblioteca.libros), 2)

    def test_agregar_dos_libros_guarda_el_orden(self):
        biblioteca.agregar_libro("Nada", "Carmen Laforet")
        biblioteca.agregar_libro("La colmena", "Camilo Jose Cela")

        self.assertEqual(biblioteca.libros[0]["titulo"], "Nada")
        self.assertEqual(biblioteca.libros[1]["titulo"], "La colmena")

    def test_libro_nuevo_esta_disponible(self):
        biblioteca.agregar_libro("El camino", "Miguel Delibes")

        self.assertTrue(biblioteca.libros[0]["disponible"])

    def test_prestar_libro_cambia_estado_si_existe_y_esta_disponible(self):
        biblioteca.agregar_libro("Nada", "Carmen Laforet")

        resultado = biblioteca.prestar_libro("Nada")

        self.assertEqual(resultado, "Libro prestado")
        self.assertFalse(biblioteca.libros[0]["disponible"])

    def test_prestar_libro_no_elimina_el_libro(self):
        biblioteca.agregar_libro("Nada", "Carmen Laforet")

        biblioteca.prestar_libro("Nada")

        self.assertEqual(len(biblioteca.libros), 1)

    def test_prestar_libro_no_cambia_el_titulo(self):
        biblioteca.agregar_libro("Nada", "Carmen Laforet")

        biblioteca.prestar_libro("Nada")

        self.assertEqual(biblioteca.libros[0]["titulo"], "Nada")

    def test_prestar_libro_no_cambia_el_autor(self):
        biblioteca.agregar_libro("Nada", "Carmen Laforet")

        biblioteca.prestar_libro("Nada")

        self.assertEqual(biblioteca.libros[0]["autor"], "Carmen Laforet")

    def test_prestar_libro_inexistente_devuelve_mensaje_error(self):
        resultado = biblioteca.prestar_libro("Libro inventado")

        self.assertEqual(resultado, "Libro no encontrado")

    def test_prestar_libro_ya_prestado_devuelve_mensaje_error(self):
        biblioteca.agregar_libro("Nada", "Carmen Laforet")
        biblioteca.prestar_libro("Nada")

        resultado = biblioteca.prestar_libro("Nada")

        self.assertEqual(resultado, "Libro no disponible")

    def test_devolver_libro_cambia_estado_si_estaba_prestado(self):
        biblioteca.agregar_libro("La colmena", "Camilo Jose Cela")
        biblioteca.prestar_libro("La colmena")

        resultado = biblioteca.devolver_libro("La colmena")

        self.assertEqual(resultado, "Libro devuelto")
        self.assertTrue(biblioteca.libros[0]["disponible"])

    def test_devolver_libro_no_elimina_el_libro(self):
        biblioteca.agregar_libro("La colmena", "Camilo Jose Cela")
        biblioteca.prestar_libro("La colmena")

        biblioteca.devolver_libro("La colmena")

        self.assertEqual(len(biblioteca.libros), 1)

    def test_devolver_libro_inexistente_devuelve_mensaje_error(self):
        resultado = biblioteca.devolver_libro("Libro inventado")

        self.assertEqual(resultado, "Libro no encontrado")

    def test_setUp_limpia_la_lista_antes_de_cada_test(self):
        self.assertEqual(len(biblioteca.libros), 0)


if __name__ == "__main__":
    unittest.main()