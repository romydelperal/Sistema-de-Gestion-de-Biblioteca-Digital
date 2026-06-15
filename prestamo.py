class Prestamo:  #Clase que será parte de una composición en Biblioteca.
    def __init__(self, usuario, libro, fecha_prestamo): # Constructor del registro de préstamo
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = None  # Se inicializa vacío hasta que se devuelva el libro
        self.activo = True  # Marca el préstamo como vigente (necesario para la restricción de préstamo)
