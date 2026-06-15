from persona import Persona
from cuenta import Cuenta
class Usuario(Persona):  # Clase Usuario que hereda de Persona (Jerarquía de Herencia) 
    def __init__(self, nombre, apellido, dni, correo_electronico):  # Constructor con datos completos
        super().__init__(nombre, apellido, dni)  # Llama al constructor del padre (Persona) 
        # COMPOSICIÓN: Se crea una instancia de Cuenta que pertenece solo a este Usuario 
        self.cuenta = Cuenta(correo_electronico) 

    # COMPORTAMIENTO POLIMÓRFICO: Redefinición del método del padre 
    def mostrar_perfil(self):  # Implementación específica para la clase Usuario
        info_base = super().mostrar_perfil()  # Obtiene la cadena de texto de la clase Persona
        # Retorna la información extendida incluyendo datos de la composición (cuenta)
        return f"[USUARIO] {info_base} | Email: {self.cuenta.email} | Estado: {self.cuenta.estado}"
