class Libro:  #Se crea la clase Libro
    def __init__(self, titulo, autor, isbn, anio_publicacion, cantidad_paginas):  # Constructor con los 5 atributos mínimos
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.anio_publicacion = anio_publicacion
        self.cantidad_paginas = cantidad_paginas

    def mostrar_datos(self):
        return (f"Título: {self.titulo} | "
                f"Autor: {self.autor} | "
                f"ISBN: {self.isbn} | "
                f"Año: {self.anio_publicacion} | "
                f"Páginas: {self.cantidad_paginas}")

class Prestamo:  #Clase que será parte de una composición en Biblioteca.
    def __init__(self, usuario, libro, fecha_prestamo): # Constructor del registro de préstamo
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = None  # Se inicializa vacío hasta que se devuelva el libro
        self.activo = True  # Marca el préstamo como vigente (necesario para la restricción de préstamo)

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