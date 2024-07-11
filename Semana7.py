class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(f"Persona {self.nombre}, {self.edad} edad, ha sido creada.")

    def __del__(self):
        # Destructor: Realiza alguna forma de limpieza
        print(f"Persona {self.nombre}, {self.edad} edad, ha sido eliminada.")

# Ejemplo de uso
Persona1 = Persona("Ernesto", 45)
Persona2 = Persona("Wendy", 31)

# Se puede acceder a los atributos del objeto
print(f"Nombre: {Persona1.nombre}, Edad: {Persona1.edad}")
print(f"Nombre: {Persona2.nombre}, Edad: {Persona2.edad}")

# Los objetos serán destruidos automáticamente al final del programa
# o cuando se usa del explícitamente
del Persona1
del Persona2
