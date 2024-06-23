
class Paciente:
    def __init__(self, nombre, sexo, edad):
        self.nombre=nombre
        self.sexo=sexo.lower()
        self.edad=edad
        self.estatura=0.5
        self.peso=5
    def pesoideal (self, estatura):
        self.estatura=estatura
        if self.sexo not in ['hombre', 'mujer']:
            raise ValueError("Sexo debe ser 'hombre' o 'mujer'")
        if self.sexo.lower == 'hombre':
            peso_ideal_kg = 50 + 2.3 * ((self.estatura / 2.54) - 60)
        else:
            peso_ideal_kg = 45.5 + 2.3 * ((self.estatura / 2.54) - 60)

        return peso_ideal_kg
    def __str__(self):
        return f"Paciente: {self.nombre},Sexo: {self.sexo},edad {self.edad}"

paciente1=Paciente("Carlos","hombre",35)
print (paciente1)
estat = float(input("Ingrese la estatura del paciente en centímetros: ").strip())

try:
    peso_ideal = paciente1.pesoideal(estat)
    print(f"El peso ideal para {paciente1.nombre}, que es {paciente1.sexo} y mide {paciente1.estatura} cm, es {peso_ideal} kg")
except ValueError as e:
    print(e)
