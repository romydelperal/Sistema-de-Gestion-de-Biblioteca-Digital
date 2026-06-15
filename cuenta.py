# 2. RELACIÓN DE COMPOSICIÓN: La existencia de Cuenta depende de Usuario [2]
class Cuenta: # Clase que representa la cuenta de acceso del usuario
    def __init__(self, email): # Constructor que recibe el correo electrónico [1]
        self.email = email # Asignación del correo electrónico (dato mínimo) [1]
        self.estado = "Activo" # Estado inicial de la cuenta dentro del sistema