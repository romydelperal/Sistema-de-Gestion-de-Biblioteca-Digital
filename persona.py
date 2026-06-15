from metavalidadora import MetaValidadora
# JERARQUÍA DE HERENCIA: Persona como clase base 
class Persona(metaclass=MetaValidadora):  # Clase base que utiliza la metaclase definida
    def __init__(self, nombre, apellido, dni):  # Constructor con los datos personales básicos 
        self.nombre = nombre  
        self.apellido = apellido  
        self.dni = dni 

    def mostrar_perfil(self):  # Método base para ser sobreescrito (Polimorfismo) 
        return f"{self.apellido}, {self.nombre} (DNI: {self.dni})"  # Retorna formato estándar de nombre
