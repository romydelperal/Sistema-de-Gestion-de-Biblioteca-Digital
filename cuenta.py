#RELACIÓN DE COMPOSICIÓN: La existencia de Cuenta depende de Usuario 
class Cuenta:  # Clase que representa la cuenta de acceso del usuario
    def __init__(self, email):  # Constructor que recibe el correo electrónico 
        self.email = email  # Asignación del correo electrónico (dato mínimo) 
        self.estado = "Activo"  # Estado inicial de la cuenta dentro del sistema
