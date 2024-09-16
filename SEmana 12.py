class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __repr__(self):
        return f"'{self.titulo}' de {self.autor} (ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __repr__(self):
        return f"{self.nombre} (ID: {self.id_usuario})"


class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}
        self.usuarios_registrados = set()

    def añadir_libro(self, libro):
        if libro.isbn in self.libros_disponibles:
            print(f"El libro con ISBN {libro.isbn} ya está en la biblioteca.")
        else:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' añadido a la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} ha sido retirado de la biblioteca.")
        else:
            print(f"No se encontró el libro con ISBN {isbn}.")

    def registrar_usuario(self, nombre, id_usuario):
        if id_usuario in [u.id_usuario for u in self.usuarios_registrados]:
            print(f"El usuario con ID {id_usuario} ya está registrado.")
        else:
            nuevo_usuario = Usuario(nombre, id_usuario)
            self.usuarios_registrados.add(nuevo_usuario)
            print(f"Usuario '{nombre}' registrado con ID {id_usuario}.")

    def dar_baja_usuario(self, id_usuario):
        usuario_a_baja = next((u for u in self.usuarios_registrados if u.id_usuario == id_usuario), None)
        if usuario_a_baja:
            self.usuarios_registrados.remove(usuario_a_baja)
            print(f"Usuario con ID {id_usuario} ha sido dado de baja.")
        else:
            print(f"No se encontró el usuario con ID {id_usuario}.")

    def prestar_libro(self, isbn, id_usuario):
        if isbn not in self.libros_disponibles:
            print(f"El libro con ISBN {isbn} no está disponible.")
            return

        usuario = next((u for u in self.usuarios_registrados if u.id_usuario == id_usuario), None)
        if usuario is None:
            print(f"No se encontró el usuario con ID {id_usuario}.")
            return

        libro = self.libros_disponibles.pop(isbn)
        usuario.libros_prestados.append(libro)
        print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")

    def devolver_libro(self, isbn, id_usuario):
        usuario = next((u for u in self.usuarios_registrados if u.id_usuario == id_usuario), None)
        if usuario is None:
            print(f"No se encontró el usuario con ID {id_usuario}.")
            return

        libro = next((l for l in usuario.libros_prestados if l.isbn == isbn), None)
        if libro is None:
            print(f"El usuario con ID {id_usuario} no tiene el libro con ISBN {isbn} prestado.")
            return

        usuario.libros_prestados.remove(libro)
        self.libros_disponibles[isbn] = libro
        print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")

    def buscar_libro(self, criterio):
        resultados = [libro for libro in self.libros_disponibles.values()
                      if (criterio.lower() in libro.titulo.lower() or
                          criterio.lower() in libro.autor.lower() or
                          criterio.lower() in libro.categoria.lower())]

        if resultados:
            print("Libros encontrados:")
            for libro in resultados:
                print(libro)
        else:
            print(f"No se encontraron libros con el criterio '{criterio}'.")

    def listar_libros_prestados(self, id_usuario):
        usuario = next((u for u in self.usuarios_registrados if u.id_usuario == id_usuario), None)
        if usuario is None:
            print(f"No se encontró el usuario con ID {id_usuario}.")
            return

        if usuario.libros_prestados:
            print(f"Libros prestados por {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(libro)
        else:
            print(f"{usuario.nombre} no tiene libros prestados.")


# Ejemplo de uso
biblioteca = Biblioteca()

# Añadir libros
biblioteca.añadir_libro(Libro("1984", "George Orwell", "Distopía", "978-0451524935"))
biblioteca.añadir_libro(Libro("El Hobbit", "J.R.R. Tolkien", "Fantástico", "978-0345339683"))

# Registrar usuarios
biblioteca.registrar_usuario("Jorge Dìaz", "001")
biblioteca.registrar_usuario("Luis Mancheno", "002")

# Prestar libros
biblioteca.prestar_libro("978-0451524935", "001")

# Listar libros prestados
biblioteca.listar_libros_prestados("001")

# Devolver libros
biblioteca.devolver_libro("978-0451524935", "001")

# Buscar libros
biblioteca.buscar_libro("Tolkien")
