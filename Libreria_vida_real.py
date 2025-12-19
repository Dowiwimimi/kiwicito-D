# este es un sistema básico de biblioteca, simula el préstamo y devolución de libros como una biblioteca real

# primera clase: la clase sera libro, el libro 
class Libro:
 # la clase, representa un libro dentro de la biblioteca
    
    def __init__(self, titulo, autor):
        # inicio los datos del libro
        self.titulo = titulo        
        self.autor = autor          
        self.disponible = True    # estado del libro (si esta disponible o no disponible)

    def mostrar_info(self):
        #muestra en la pantalla la información del libro
        if self.disponible:
            estado = "Disponible"
        else:
            estado = "Prestado"

        print("Libro:", self.titulo)
        print("Autor:", self.autor)
        print("Estado:", estado)

    def prestar(self):
        # este cambia el estado del libro a prestado si está disponible
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' fue prestado.")
        else:
            print(f"El libro '{self.titulo}' no está disponible.")

    def devolver(self):
        # cambia el estado del libro a disponible nuevamente
        self.disponible = True
        print(f"El libro '{self.titulo}' ha sido devuelto.")


#segunda clase: esta clase sera el usuario 
class Usuario:
    # la clase representara a una persona que usa la biblioteca

    def __init__(self, nombre):
        # inicio los datos del usuario 
        self.nombre = nombre
        self.libros_prestados = []    # es la lista de libros que el usuario ha prestado

    def prestar_libro(self, libro):
        #permite  al usuario solicitar un libro
        print(f"\n{self.nombre} pide el libro '{libro.titulo}'")

        # verifica si el libro cuenta con disponibilidad 
        if libro.disponible:
            libro.prestar()
            self.libros_prestados.append(libro)
        else:
            print("No hay disponibilidad.")

    def devolver_libro(self, libro):
        print(f"\n{self.nombre} devuelve el libro '{libro.titulo}'")

        #se verifica si el libro pertenece al usuario
        if libro in self.libros_prestados:
            libro.devolver()
            self.libros_prestados.remove(libro)
        else:
            print("Este libro no estaba prestado a este usuario.")



# se crean los libros disponibles en la biblioteca
libro_1 = Libro("La metamorfosis", "Franz Kafka")
libro_2 = Libro("Crimen y castigo", "Fiódor Dostoievski")

#se crea un usuario de la biblioteca
usuario_1 = Usuario("dowiwi")

#hacer una muestra la información inicial de los libros
libro_1.mostrar_info()
libro_2.mostrar_info()

#el usuario interactúa con los libros
usuario_1.prestar_libro(libro_1)
libro_1.mostrar_info()

usuario_1.prestar_libro(libro_2)
libro_2.mostrar_info()

usuario_1.devolver_libro(libro_1)
libro_1.mostrar_info()
