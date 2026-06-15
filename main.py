from singletonmeta import SingletonMeta
from metavalidadora import MetaValidadora
from cuenta import Cuenta
from persona import Persona
from usuario import Usuario
from gestorusuarios import GestorUsuarios
from libro import Libro
from prestamo import Prestamo
from biblioteca import Biblioteca

# --- BLOQUE DE PRUEBA DEL SISTEMA ---
if __name__ == "__main__": # Punto de entrada para ejecutar el script
    biblioteca_gestor = GestorUsuarios() # Instancia el gestor para iniciar operaciones

    # Ejecución de Altas de ejemplo
    biblioteca_gestor.alta_usuario("Juan", "Perez", "12345678", "juan@mail.com") # Registro 1
    biblioteca_gestor.alta_usuario("Ana", "Gomez", "87654321", "ana@mail.com") # Registro 2
    
    biblioteca_gestor.listar_usuarios() # Muestra los usuarios cargados inicialmente
    
    # Prueba de Modificación
    biblioteca_gestor.modificar_usuario("12345678", "juan_nuevo@mail.com") # Cambio de correo
    
    # Prueba de Baja
    biblioteca_gestor.baja_usuario("87654321") # Eliminación de un usuario
    
    biblioteca_gestor.listar_usuarios() # Muestra el estado final de la gestión de usuarios

# Programa principal
biblioteca = Biblioteca()

while True:
    print("\n--- GESTIÓN DE LIBROS ---")
    print("1. Alta de libro")
    print("2. Modificar libro")
    print("3. Eliminar libro")
    print("4. Listar libros")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        titulo = input("Título: ")
        autor = input("Autor: ")
        isbn = input("ISBN: ")
        anio = int(input("Año de publicación: "))
        paginas = int(input("Cantidad de páginas: "))

        libro = Libro(titulo, autor, isbn, anio, paginas)
        biblioteca.agregar_libro(libro)

    elif opcion == "2":
        isbn = input("Ingrese ISBN del libro a modificar: ")
        biblioteca.modificar_libro(isbn)

    elif opcion == "3":
        isbn = input("Ingrese ISBN del libro a eliminar: ")
        biblioteca.eliminar_libro(isbn)

    elif opcion == "4":
        biblioteca.listar_libros()

    elif opcion == "5":
        print("Fin del programa.")
        break

    else:
        print("Opción inválida.")
