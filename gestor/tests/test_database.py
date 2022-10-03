import copy
import unittest
import helpers
import config
import csv
import database as db

# el unittest.TestCase es para que pase todos los datos de los test a esta clase
class TestDatabase(unittest.TestCase):
    
    def setUp(self): #Es un método de Python
        #se ejecuta antes de cada prueba
        db.Clientes.lista = [
            db.Cliente('15J', 'Marta', 'Pérez'), 
            db.Cliente('48H', 'Manolo', 'López'),
            db.Cliente('28Z', 'Ana', 'Garcia') ]
        
    #miramos cada método de la clase Clientes, siempre con la palabra test delante
    def test_buscar_cliente(self):
        cliente_existente = db.Clientes.buscar('15J')
        cliente_no_existente = db.Clientes.buscar('99X')
        self.assertIsNotNone(cliente_existente) #assert es como el print de los tests
        self.assertIsNone(cliente_no_existente)

    def test_crear_cliente(self):
        nuevo_cliente = db.Clientes.crear('39X', 'Héctor', 'Costa')
        self.assertEqual(len(db.Clientes.lista), 4)
        self.assertEqual(nuevo_cliente.dni, '39X')
        self.assertEqual(nuevo_cliente.nombre, 'Héctor')
        self.assertEqual(nuevo_cliente.apellido, 'Costa')
        
    
    def test_modificar_cliente(self):
        cliente_a_modificar = copy.copy(db.Clientes.buscar('28Z'))
        cliente_modificado = db.Clientes.modificar('28Z', 'Mariana', 'Pérez')
        self.assertEqual(cliente_a_modificar.nombre, 'Ana')
        self.assertEqual(cliente_modificado.nombre, 'Mariana')
 
    def test_borrar_cliente(self):
        cliente_borrado = db.Clientes.borrar('48H')
        cliente_rebuscado = db.Clientes.buscar('48H')
        self.assertEqual(cliente_borrado.dni, '48H')
        self.assertNotEqual(cliente_rebuscado)

    def test_dni_valido(self):
        self.assertTrue(helpers.dni_valido('00A', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('23223S', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('F35', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('48H', db.Clientes.lista))
    
    
    def test_escritura_csv(self):
        db.Clientes.borrar('48H')
        db.Clientes.borrar('15J')
        db.Clientes.modificar('28Z', 'Mariana', 'García')
        
        dni, nombre, apellido = None, None, None
        with open(config.DATABASE_PATH, newline="\n") as fichero:
            reader = csv.reader(fichero, delimiter=";")
            dni, nombre, apellido = next(reader) # Primera línea del iterador
        self.assertEqual(dni, '28Z')
        self.assertEqual(nombre, 'Mariana')
        self.assertEqual(apellido, 'García')

if __name__== '__main__':
    unittest.main()