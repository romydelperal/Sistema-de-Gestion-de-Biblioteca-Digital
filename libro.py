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