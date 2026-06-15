# METACLASE: Implementa el patrón Singleton para asegurar una única instancia de la Biblioteca
class SingletonMeta(type):  # Metaclase que hereda de 'type' 
    _instances = {}  # Diccionario para almacenar la instancia única
    def __call__(cls, *args, **kwargs):  # Controla la creación de la clase
        if cls not in cls._instances:  # Si no existe la instancia, la crea
            cls._instances[cls] = super().__call__(*args, **kwargs)  # Almacena la instancia
        return cls._instances[cls]  # Retorna siempre la misma instancia
    
