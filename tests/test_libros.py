import unittest

import biblioteca


class TestLibrosFase4(unittest.TestCase):

    def setUp(self):
        biblioteca.libros.clear()

    def test_crear_libro_anade_un_libro_a_la_lista(self):
        biblioteca.crear_libro(1, "El Quijote", "Miguel de Cervantes", "ISBN001")

        self.assertEqual(len(biblioteca.libros), 1)

    def test_crear_libro_guarda_id(self):
        libro = biblioteca.crear_libro(1, "El Quijote", "Miguel de Cervantes", "ISBN001")

        self.assertEqual(libro.id, 1)

    def test_crear_libro_guarda_titulo(self):
        libro = biblioteca.crear_libro(1, "El Quijote", "Miguel de Cervantes", "ISBN001")

        self.assertEqual(libro.titulo, "El Quijote")

    def test_crear_libro_guarda_autor(self):
        libro = biblioteca.crear_libro(1, "El Quijote", "Miguel de Cervantes", "ISBN001")

        self.assertEqual(libro.autor, "Miguel de Cervantes")

    def test_crear_libro_guarda_isbn(self):
        libro = biblioteca.crear_libro(1, "El Quijote", "Miguel de Cervantes", "ISBN001")

        self.assertEqual(libro.isbn, "ISBN001")

    def test_crear_libro_esta_disponible_por_defecto(self):
        libro = biblioteca.crear_libro(1, "El Quijote", "Miguel de Cervantes", "ISBN001")

        self.assertTrue(libro.disponible)

    def test_crear_libro_permite_crearlo_no_disponible(self):
        libro = biblioteca.crear_libro(
            1,
            "El Quijote",
            "Miguel de Cervantes",
            "ISBN001",
            disponible=False
        )

        self.assertFalse(libro.disponible)

    def test_obtener_libro_por_id_existente(self):
        biblioteca.crear_libro(1, "Nada", "Carmen Laforet", "ISBN002")

        libro = biblioteca.obtener_libro_por_id(1)

        self.assertEqual(libro.titulo, "Nada")

    def test_obtener_libro_por_id_inexistente_devuelve_none(self):
        libro = biblioteca.obtener_libro_por_id(99)

        self.assertIsNone(libro)

    def test_actualizar_libro_cambia_titulo(self):
        biblioteca.crear_libro(1, "Titulo antiguo", "Autor", "ISBN003")

        biblioteca.actualizar_libro(1, titulo="Titulo nuevo")

        libro = biblioteca.obtener_libro_por_id(1)
        self.assertEqual(libro.titulo, "Titulo nuevo")

    def test_actualizar_libro_cambia_autor(self):
        biblioteca.crear_libro(1, "Libro", "Autor antiguo", "ISBN003")

        biblioteca.actualizar_libro(1, autor="Autor nuevo")

        libro = biblioteca.obtener_libro_por_id(1)
        self.assertEqual(libro.autor, "Autor nuevo")

    def test_actualizar_libro_cambia_isbn(self):
        biblioteca.crear_libro(1, "Libro", "Autor", "ISBN003")

        biblioteca.actualizar_libro(1, isbn="ISBN999")

        libro = biblioteca.obtener_libro_por_id(1)
        self.assertEqual(libro.isbn, "ISBN999")

    def test_actualizar_libro_cambia_disponibilidad(self):
        biblioteca.crear_libro(1, "Libro", "Autor", "ISBN003")

        biblioteca.actualizar_libro(1, disponible=False)

        libro = biblioteca.obtener_libro_por_id(1)
        self.assertFalse(libro.disponible)

    def test_actualizar_libro_existente_devuelve_true(self):
        biblioteca.crear_libro(1, "Libro", "Autor", "ISBN003")

        resultado = biblioteca.actualizar_libro(1, titulo="Nuevo titulo")

        self.assertTrue(resultado)

    def test_actualizar_libro_inexistente_devuelve_false(self):
        resultado = biblioteca.actualizar_libro(99, titulo="Nuevo titulo")

        self.assertFalse(resultado)

    def test_eliminar_libro_existente_devuelve_true(self):
        biblioteca.crear_libro(1, "Nada", "Carmen Laforet", "ISBN002")

        resultado = biblioteca.eliminar_libro(1)

        self.assertTrue(resultado)

    def test_eliminar_libro_borra_libro_de_la_lista(self):
        biblioteca.crear_libro(1, "Nada", "Carmen Laforet", "ISBN002")

        biblioteca.eliminar_libro(1)

        self.assertEqual(len(biblioteca.libros), 0)

    def test_eliminar_libro_inexistente_devuelve_false(self):
        resultado = biblioteca.eliminar_libro(99)

        self.assertFalse(resultado)

    def test_buscar_libros_por_titulo(self):
        biblioteca.crear_libro(1, "Nada", "Carmen Laforet", "ISBN002")

        resultado = biblioteca.buscar_libros_por_titulo("Nada")

        self.assertEqual(len(resultado), 1)

    def test_buscar_libros_por_titulo_inexistente_devuelve_lista_vacia(self):
        biblioteca.crear_libro(1, "Nada", "Carmen Laforet", "ISBN002")

        resultado = biblioteca.buscar_libros_por_titulo("El Quijote")

        self.assertEqual(resultado, [])

    def test_buscar_libros_por_autor(self):
        biblioteca.crear_libro(1, "Nada", "Carmen Laforet", "ISBN002")

        resultado = biblioteca.buscar_libros_por_autor("Carmen Laforet")

        self.assertEqual(len(resultado), 1)

    def test_buscar_libros_disponibles(self):
        biblioteca.crear_libro(1, "Nada", "Carmen Laforet", "ISBN002", disponible=True)

        resultado = biblioteca.buscar_libros_por_disponibilidad(True)

        self.assertEqual(len(resultado), 1)

    def test_buscar_libros_no_disponibles(self):
        biblioteca.crear_libro(1, "Nada", "Carmen Laforet", "ISBN002", disponible=False)

        resultado = biblioteca.buscar_libros_por_disponibilidad(False)

        self.assertEqual(len(resultado), 1)

    def test_buscar_libros_por_coincidencia_parcial_en_titulo(self):
        biblioteca.crear_libro(1, "El Quijote", "Miguel de Cervantes", "ISBN001")

        resultado = biblioteca.buscar_libros_por_coincidencia("Quij")

        self.assertEqual(len(resultado), 1)

    def test_buscar_libros_por_coincidencia_parcial_en_autor(self):
        biblioteca.crear_libro(1, "El Quijote", "Miguel de Cervantes", "ISBN001")

        resultado = biblioteca.buscar_libros_por_coincidencia("Cervantes")

        self.assertEqual(len(resultado), 1)

    def test_buscar_libros_por_coincidencia_inexistente_devuelve_lista_vacia(self):
        biblioteca.crear_libro(1, "El Quijote", "Miguel de Cervantes", "ISBN001")

        resultado = biblioteca.buscar_libros_por_coincidencia("Harry Potter")

        self.assertEqual(resultado, [])

    def test_buscar_libro_por_id_existente(self):
        biblioteca.crear_libro(1, "Nada", "Carmen Laforet", "ISBN002")

        libro = biblioteca.buscar_libro_por_id(1)

        self.assertEqual(libro.titulo, "Nada")

    def test_buscar_libro_por_id_inexistente_devuelve_none(self):
        libro = biblioteca.buscar_libro_por_id(99)

        self.assertIsNone(libro)


if __name__ == "__main__":
    unittest.main()