import csv 
import config
class Cliente: #coge los datos y los devuelve
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apllido = apellido
    
    def __str__(self): #Nos devuelve una cadena de caracteres, como si fuese el getter
        return f"({self.dni}) {self.nombre} {self.apellido}"
    
    
class Clientes: #Se encargará de uscar, crear, actualizar y borrar clientes
    #lista de clientes
    #Recogerá todos los datos dni, nombre y apellidos
    lista = []
    # Creamos la lista y cargamos los clientes en memoria
    with open(config.DATABASE_PATH, newline="\n") as fichero:
        reader = csv.reader(fichero, delimiter=";")
        for dni, nombre, apellido in reader:
            cliente = Cliente(dni, nombre, apellido)
            lista.append(cliente)
            
    @staticmethod #Se le pone a los métodos q llamamos mucho, donde solo nos guarda lo último
    def buscar(dni):
        for cliente in Clientes.lista: #busca en la lista que hemos creado antes
            if cliente.dni == dni:
                return cliente
            
    @staticmethod
    def crear(dni, nombre, apellido):
        cliente = Cliente(dni, nombre, apellido) #llamamos a la clase Cliente
        Clientes.lista.append(cliente)
        Clientes.guardar()
        return cliente
    
    @staticmethod
    def modificar(dni, nombre, apellido):
        for indice, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni: #cliente nos recorre la lita, pero esta se compone de objetos de las clases, por eso podemos poner el .dni. Pq va asociado a la clase Clientes
                Clientes.lista[indice].nombre = nombre
                Clientes.lista[indice].apellido =apellido
                Clientes.guardar()
                return Clientes.lista[indice]
    
    @staticmethod
    def borrar(dni):
        for indice, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                cliente = Clientes.lista.pop(indice)
                Clientes.guardar()
                return cliente
            
    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, "w", newline="\n") as fichero:
            writer = csv.writer(fichero, delimiter=";")
            for c in Clientes.lista:
                writer.writerow((c.dni, c.nombre, c.apellido))