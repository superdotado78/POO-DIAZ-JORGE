class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto  # ID único del producto
        self.nombre = nombre  # Nombre del producto
        self.cantidad = cantidad  # Cantidad en inventario
        self.precio = precio  # Precio del producto

    # Getters
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    # Representación del producto
    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.productos = []  # Lista de productos en el inventario
        self.archivo = archivo
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """Carga los productos desde un archivo de texto."""
        try:
            with open(self.archivo, 'r') as file:
                for linea in file:
                    id_producto, nombre, cantidad, precio = linea.strip().split(',')
                    producto = Producto(int(id_producto), nombre, int(cantidad), float(precio))
                    self.productos.append(producto)
            print("Productos cargados exitosamente desde el archivo.")
        except FileNotFoundError:
            print("Archivo no encontrado. Se creará uno nuevo al guardar.")
        except PermissionError:
            print("Error: No se tienen permisos para leer el archivo.")
        except Exception as e:
            print(f"Error inesperado al cargar el archivo: {e}")

    def guardar_en_archivo(self):
        """Guarda los productos en un archivo de texto."""
        try:
            with open(self.archivo, 'w') as file:
                for prod in self.productos:
                    file.write(f"{prod.get_id()},{prod.get_nombre()},{prod.get_cantidad()},{prod.get_precio()}\n")
            print("Productos guardados exitosamente en el archivo.")
        except PermissionError:
            print("Error: No se tienen permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error inesperado al guardar el archivo: {e}")

    def añadir_producto(self, producto):
        """Añade un producto al inventario si el ID no existe."""
        for prod in self.productos:
            if prod.get_id() == producto.get_id():
                raise ValueError("Error: El ID ya existe en el inventario.")
        self.productos.append(producto)
        self.guardar_en_archivo()
        print(f"Producto '{producto.get_nombre()}' añadido con éxito.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto del inventario por su ID."""
        for prod in self.productos:
            if prod.get_id() == id_producto:
                self.productos.remove(prod)
                self.guardar_en_archivo()
                print(f"Producto con ID {id_producto} eliminado.")
                return
        raise ValueError("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        """Actualiza la cantidad o el precio de un producto por su ID."""
        for prod in self.productos:
            if prod.get_id() == id_producto:
                if nueva_cantidad is not None:
                    prod.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    prod.set_precio(nuevo_precio)
                self.guardar_en_archivo()
                print(f"Producto con ID {id_producto} actualizado.")
                return
        raise ValueError("Error: Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        """Busca productos en el inventario por nombre."""
        resultados = [prod for prod in self.productos if nombre.lower() in prod.get_nombre().lower()]
        if resultados:
            for prod in resultados:
                print(prod)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for prod in self.productos:
                print(prod)

    def total_productos(self):
        """Devuelve el número total de productos en el inventario."""
        return len(self.productos)

    def valor_total_inventario(self):
        """Calcula el valor total del inventario."""
        return sum(prod.get_precio() * prod.get_cantidad() for prod in self.productos)

def mostrar_menu():
    print("\n--- Menú de Gestión de Inventario ---")
    print("1. Añadir producto")
    print("2. Eliminar producto por ID")
    print("3. Actualizar cantidad o precio de un producto por ID")
    print("4. Buscar productos por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")

# Ejemplo de uso
if __name__ == "__main__":
    inventario = Inventario()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            id_producto = int(input("ID del producto: "))
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            try:
                inventario.añadir_producto(producto)
            except ValueError as e:
                print(e)
        elif opcion == '2':
            id_producto = int(input("ID del producto a eliminar: "))
            try:
                inventario.eliminar_producto(id_producto)
            except ValueError as e:
                print(e)
        elif opcion == '3':
            id_producto = int(input("ID del producto a actualizar: "))
            nueva_cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            nuevo_precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None
            try:
                inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)
            except ValueError as e:
                print(e)
        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)
        elif opcion == '5':
            inventario.mostrar_todos()
        elif opcion == '6':
            break
        else:
            print("Opción no válida. Intente de nuevo.")
