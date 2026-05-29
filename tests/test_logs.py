import unittest

import biblioteca


class TestLogs(unittest.TestCase):

    def setUp(self):
        biblioteca.libros.clear()
        biblioteca.usuarios.clear()
        biblioteca.prestamos.clear()

        if hasattr(biblioteca, "logs"):
            biblioteca.logs.clear()

    def test_registrar_log_anade_mensaje_a_la_lista(self):
        biblioteca.registrar_log("Prueba de log")

        self.assertEqual(len(biblioteca.logs), 1)

    def test_registrar_log_guarda_el_mensaje_correcto(self):
        biblioteca.registrar_log("Usuario 1 ha prestado Libro 1")

        self.assertEqual(biblioteca.logs[0], "Usuario 1 ha prestado Libro 1")

    def test_prestar_libro_registra_log(self):
        biblioteca.crear_libro(1, "Nada", "Carmen Laforet", "ISBN001")
        biblioteca.crear_usuario(1, "Unai", "Rubio", "unai@email.com")

        biblioteca.prestar_libro(1, 1)

        self.assertIn("Usuario 1 ha prestado Libro 1", biblioteca.logs)

    def test_devolver_libro_registra_log(self):
        biblioteca.crear_libro(1, "Nada", "Carmen Laforet", "ISBN001", disponible=False)
        biblioteca.crear_usuario(1, "Unai", "Rubio", "unai@email.com")
        biblioteca.prestamos.append({"libro_id": 1, "usuario_id": 1})

        biblioteca.devolver_libro(1, 1)

        self.assertIn("Usuario 1 ha devuelto Libro 1", biblioteca.logs)

    def test_obtener_logs_devuelve_lista_de_logs(self):
        biblioteca.registrar_log("Log 1")
        biblioteca.registrar_log("Log 2")

        resultado = biblioteca.obtener_logs()

        self.assertEqual(len(resultado), 2)


if __name__ == "__main__":
    unittest.main()