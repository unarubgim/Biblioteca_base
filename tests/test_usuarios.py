import unittest

import biblioteca


class TestUsuarios(unittest.TestCase):

    def setUp(self):
        biblioteca.usuarios.clear()

    def test_crear_usuario_anade_usuario_a_la_lista(self):
        biblioteca.crear_usuario(1, "Unai", "Rubio", "Unai@email.com")

        self.assertEqual(len(biblioteca.usuarios), 1)

    def test_crear_usuario_guarda_id(self):
        usuario = biblioteca.crear_usuario(1, "Unai", "Rubio", "Unai@email.com")

        self.assertEqual(usuario.id, 1)

    def test_crear_usuario_guarda_nombre(self):
        usuario = biblioteca.crear_usuario(1, "Unai", "Rubio", "Unai@email.com")

        self.assertEqual(usuario.nombre, "Unai")

    def test_crear_usuario_guarda_apellidos(self):
        usuario = biblioteca.crear_usuario(1, "Unai", "Rubio", "Unai@email.com")

        self.assertEqual(usuario.apellidos, "Rubio")

    def test_crear_usuario_guarda_email(self):
        usuario = biblioteca.crear_usuario(1, "Unai", "Rubio", "Unai@email.com")

        self.assertEqual(usuario.email, "Unai@email.com")


if __name__ == "__main__":
    unittest.main()