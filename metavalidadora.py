# 1. METACLASE utilizando 'type' para validar la estructura de las clases [2]
class MetaValidadora(type): # Definición de la metaclase heredando de 'type'
    def __new__(cls, name, bases, dct): # Método que se ejecuta al crear una nueva clase
        # Verifica si la clase no es la base y si le falta el método polimórfico [2]
        if name != "Persona" and "mostrar_perfil" not in dct: 
            print(f"Aviso: La clase '{name}' debe implementar 'mostrar_perfil'.") # Notificación de validación
        return super().__new__(cls, name, bases, dct) # Crea y retorna la clase validada
    
# 2. DECORADOR PROPIO: Valida la disponibilidad del libro antes de prestarlo
def validar_disponibilidad(func): # Definición del decorador 
    def wrapper(self, dni, isbn, fecha): # Envoltorio que recibe los datos del préstamo
        if any(p.libro.isbn == isbn and p.activo for p in self.prestamos):  # Verifica si el libro ya tiene un préstamo activo en el sistema
            print(f"Error: El libro con ISBN {isbn} ya está prestado.") # Bloquea la operación
            return None # Termina la ejecución si no está disponible
        return func(self, dni, isbn, fecha) # Si está libre, procede con el préstamo
    return wrapper # Retorna la función decorada