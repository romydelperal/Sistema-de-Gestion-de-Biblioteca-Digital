from metavalidadora import MetaValidadora
# JERARQUÍA DE HERENCIA: Persona como clase base 
class Persona(metaclass=MetaValidadora): # Clase base que utiliza la metaclase definida
    def __init__(self, nombre, apellido, dni): # Constructor con los datos personales básicos [1]
        self.nombre = nombre # Almacena el nombre del usuario [1]
        self.apellido = apellido # Almacena el apellido del usuario [1]
        self.dni = dni # Almacena el DNI, identificador clave para el CRUD [1]

    def mostrar_perfil(self): # Método base para ser sobreescrito (Polimorfismo) [2]
        return f"{self.apellido}, {self.nombre} (DNI: {self.dni})" # Retorna formato estándar de nombre