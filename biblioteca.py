from metavalidadora import validar_disponibilidad
from singletonmeta import SingletonMeta
from prestamo import Prestamo
class Biblioteca(metaclass=SingletonMeta):  # Clase principal usando Singleton para ser única instancia
    def __init__(self, nombre):  # Constructor de la biblioteca
        self.nombre = nombre
        self.libros = []      # Agregación: Los libros existen fuera de la biblioteca 
        self.usuarios = []
        self.prestamos = []   # Composición: Los registros de préstamo pertenecen a la biblioteca 

    def agregar_libro(self, libro):  # Alta de libro
        self.libros.append(libro)

    @validar_disponibilidad  # Aplicación del decorador propio para restringir préstamos duplicados
    def registrar_prestamo(self, usuario, libro, fecha_inicio):  # Método para crear un nuevo préstamo
        nuevo_prestamo = Prestamo(usuario, libro, fecha_inicio)  # Se crea la instancia de Prestamo
        self.prestamos.append(nuevo_prestamo)  # Se guarda en el registro histórico de la biblioteca
        print(f"Préstamo registrado: {libro.titulo} a {usuario.nombre}")  # Confirmación en sistema

    def devolver_libro(self, isbn, fecha_fin):  # Método para gestionar la devolución
        for p in self.prestamos:  # Busca en la lista de préstamos de la biblioteca
            if p.libro.isbn == isbn and p.activo:  # Si coincide el ISBN y el préstamo está vigente
                p.fecha_devolucion = fecha_fin  # Se registra la fecha de entrega
                p.activo = False  # Se marca como finalizado para liberar el libro
                print(f"Libro {p.libro.titulo} devuelto con éxito.")  # Confirmación de éxito 
                return  # Sale del método una vez procesada la devolución
        print("No se encontró un préstamo activo para ese ISBN.")  # Error si no hay préstamo pendiente
