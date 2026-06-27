from singletonmeta import SingletonMeta
from metavalidadora import MetaValidadora
from cuenta import Cuenta
from persona import Persona
from usuario import Usuario
from gestorusuarios import GestorUsuarios
from libro import Libro
from prestamo import Prestamo
from biblioteca import Biblioteca

#Singleton
# Aunque intentemos crear dos bibliotecas, ambas apuntan al mismo objeto en memoria
biblio1 = Biblioteca("Biblioteca Central")
biblio2 = Biblioteca("Biblioteca Sucursal")
print(f"¿Son la misma instancia? {biblio1 is biblio2}") 

#Gestor de Usuarios
gestor = GestorUsuarios()
gestor.alta_usuario("Ana", "García", "11223344", "ana@correo.com")
usuario_ana = gestor.usuarios[0]

#Registro de Libro
libro_python = Libro("Python Pro", "Guido", "ISBN-999", 2026, 300)
biblio1.agregar_libro(libro_python)

#Prueba del Decorador (Validación)
# Primer préstamo: debería funcionar
biblio1.registrar_prestamo(usuario_ana, libro_python, "2026-06-24")

# Intentamos prestar el mismo libro otra vez: el decorador debería bloquearlo
biblio1.registrar_prestamo(usuario_ana, libro_python, "2026-06-25")

#Devolución
biblio1.devolver_libro("ISBN-999", "2026-06-30")

#Polimorfismo y Composición
# Mostramos el perfil del usuario (incluye datos de la Cuenta, que es composición)
gestor.listar_usuarios()
