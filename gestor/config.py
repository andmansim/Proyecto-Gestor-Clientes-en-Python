import sys
DATABASE_PATH = 'clientes.csv'
#lo ponemos aquí pq antes nos daba problemas
#pq antes las pruebaS nos modificaban el fichero csv, por eso lo hacemos constante
if 'pytest' in sys.argv[0]:
    DATABASE_PATH = 'tests/clientes_test.csv' #con esto las pruebas irán a bucar el nuevo fichero