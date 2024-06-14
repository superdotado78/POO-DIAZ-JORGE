class ClimaDiario:
    def __init__(self, temperatura=0.0):
        self._temperatura = temperatura

    @property
    def temperatura(self):
        return self._temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if isinstance(valor, (int, float)):
            self._temperatura = valor
        else:
            raise ValueError("La temperatura debe ser un número.")

class SemanaClimatica:
    def __init__(self):
        self._dias = [ClimaDiario() for _ in range(7)]

    def ingresar_temperaturas(self):
        print("Por favor, ingrese las temperaturas diarias para una semana (7 días).")
        for i in range(7):
            while True:
                try:
                    temp = float(input(f"Día {i+1}: "))
                    self._dias[i].temperatura = temp
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número válido.")

    def calcular_promedio_semanal(self):
        total = sum(dia.temperatura for dia in self._dias)
        promedio = total / len(self._dias)
        return promedio

    def mostrar_temperaturas(self):
        return [dia.temperatura for dia in self._dias]

def main():
    semana_climatica = SemanaClimatica()
    semana_climatica.ingresar_temperaturas()
    promedio = semana_climatica.calcular_promedio_semanal()
    print(f"\nLas temperaturas ingresadas son: {semana_climatica.mostrar_temperaturas()}")
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}")

if __name__ == "__main__":
    main()
