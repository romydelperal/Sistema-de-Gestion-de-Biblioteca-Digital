from usuario import Usuario
# RELACIÓN DE AGREGACIÓN Y OPERACIONES CRUD 
class GestorUsuarios: # Clase encargada de administrar la colección de usuarios
    def __init__(self): # Constructor del gestor
        # AGREGACIÓN: Lista de usuarios que existen independientemente del gestor 
        self.usuarios = [] 

    # OPERACIÓN: ALTA 
    def alta_usuario(self, nombre, apellido, dni, email):  # Método para registrar nuevos usuarios
        nuevo_usuario = Usuario(nombre, apellido, dni, email)  # Crea instancia de la clase Usuario
        self.usuarios.append(nuevo_usuario)  # Agrega el nuevo objeto a la lista de agregación
        print(f"Usuario {nombre} registrado con éxito.")  # Confirmación de la operación

    # OPERACIÓN: LISTADO 
    def listar_usuarios(self):  # Método para mostrar todos los registros
        print("\n--- LISTADO DE USUARIOS ---")  # Encabezado visual para la consola
        for u in self.usuarios:  # Itera sobre cada objeto en la lista de agregación
            print(u.mostrar_perfil())  # Llama al método polimórfico de cada usuario 

    # OPERACIÓN: MODIFICACIÓN 
    def modificar_usuario(self, dni, nuevo_email): # Método para actualizar datos por DNI
        for u in self.usuarios:  # Busca al usuario en la colección
            if u.dni == dni:  # Si encuentra el DNI ingresado
                u.cuenta.email = nuevo_email  # actualiza el email en el objeto Cuenta (Composición)
                print(f"Email del usuario con DNI {dni} actualizado.")  # Confirmación de éxito
                return  # Finaliza el método tras la modificación
        print("Usuario no encontrado.")  # Mensaje si no hubo coincidencias de DNI

    # OPERACIÓN: BAJA 
    def baja_usuario(self, dni):  # Método para eliminar un registro del sistema
        for u in self.usuarios:  # Recorre la lista de usuarios agregados
            if u.dni == dni: # Si el DNI coincide con el registro
                self.usuarios.remove(u)  # Elimina el objeto de la lista del gestor
                print(f"Usuario con DNI {dni} eliminado.")  # Confirmación de eliminación
                return  # Finaliza el proceso de baja
        print("No se pudo eliminar: Usuario no encontrado.")  # Error si el DNI no existe
