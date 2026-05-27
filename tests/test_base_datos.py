import sqlite3
import unittest
from pathlib import Path


RUTA_BD = Path(__file__).resolve().parent.parent / "bd" / "biblioteca.db"


class TestBaseDatosInicial(unittest.TestCase):

    def test_biblioteca_db_existe(self):
        self.assertTrue(RUTA_BD.exists())

    def test_biblioteca_db_es_un_archivo(self):
        self.assertTrue(RUTA_BD.is_file())

    def test_biblioteca_db_tiene_extension_db(self):
        self.assertEqual(RUTA_BD.suffix, ".db")

    def test_existe_tabla_libros(self):
        conexion = sqlite3.connect(RUTA_BD)

        tablas = conexion.execute(
            "SELECT name FROM sqlite_master WHERE type = 'table'"
        ).fetchall()

        conexion.close()

        self.assertIn(("libros",), tablas)

    def test_tabla_libros_tiene_cuatro_columnas(self):
        conexion = sqlite3.connect(RUTA_BD)

        columnas = conexion.execute("PRAGMA table_info(libros)").fetchall()

        conexion.close()

        self.assertEqual(len(columnas), 4)

if __name__ == "__main__":
    unittest.main()