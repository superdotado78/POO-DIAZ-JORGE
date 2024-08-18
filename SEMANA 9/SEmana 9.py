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
    def __init__(self):
        self.productos = []  # Lista de productos en el inventario

    def añadir_producto(self, producto):
        # Verificar si el ID ya existe
        for prod in self.productos:
            if prod.get_id() == producto.get_id():
                print("Error: El ID ya existe en el inventario.")
                return
        self.productos.append(producto)
        print(f"Producto '{producto.get_nombre()}' añadido con éxito.")

    def eliminar_producto(self, id_producto):
        for prod in self.productos:
            if prod.get_id() == id_producto:
                self.productos.remove(prod)
                print(f"Producto con ID {id_producto} eliminado.")
                return
        print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for prod in self.productos:
            if prod.get_id() == id_producto:
                if nueva_cantidad is not None:
                    prod.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    prod.set_precio(nuevo_precio)
                print(f"Producto con ID {id_producto} actualizado.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        resultados = [prod for prod in self.productos if nombre.lower() in prod.get_nombre().lower()]
        if resultados:
            for prod in resultados:
                print(prod)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for prod in self.productos:
                print(prod)

def mostrar_menu():
    print("\n--- Menú de Gestión de Inventario ---")
    print("1. Añadir producto")
    print("2. Eliminar producto por ID")
    print("3. Actualizar cantidad o precio de un producto por ID")
    print("4. Buscar productos por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")

def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese ID del producto a actualizar: ")
            nueva_cantidad = input("Ingrese nueva cantidad (o presione Enter para omitir): ")
            nuevo_precio = input("Ingrese nuevo precio (o presione Enter para omitir): ")

            if nueva_cantidad:
                nueva_cantidad = int(nueva_cantidad)
            else:
                nueva_cantidad = None

            if nuevo_precio:
                nuevo_precio = float(nuevo_precio)
            else:
                nuevo_precio = None

            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print("Saliendo del sistema de gestión de inventario.")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
