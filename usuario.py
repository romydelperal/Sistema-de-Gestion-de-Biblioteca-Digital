from persona import Persona
from cuenta import Cuenta
class Usuario(Persona): # Clase Usuario que hereda de Persona (Jerarquía de Herencia) [2]
    def __init__(self, nombre, apellido, dni, correo_electronico): # Constructor con datos completos
        super().__init__(nombre, apellido, dni) # Llama al constructor del padre (Persona) [2]
        # COMPOSICIÓN: Se crea una instancia de Cuenta que pertenece solo a este Usuario [2]
        self.cuenta = Cuenta(correo_electronico) 

    # 4. COMPORTAMIENTO POLIMÓRFICO: Redefinición del método del padre [2]
    def mostrar_perfil(self): # Implementación específica para la clase Usuario
        info_base = super().mostrar_perfil() # Obtiene la cadena de texto de la clase Persona
        # Retorna la información extendida incluyendo datos de la composición (cuenta)
        return f"[USUARIO] {info_base} | Email: {self.cuenta.email} | Estado: {self.cuenta.estado}"