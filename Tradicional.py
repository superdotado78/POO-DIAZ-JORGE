def ingresar_temperaturas():
    temperaturas = []
    print("Ingrese las temperaturas diarias para una semana (7 días).")
    for i in range(7):
        while True:
            try:
                temp = float(input(f"Día {i+1}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número válido.")
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio_semanal(temperaturas):
    total = sum(temperaturas)
    promedio = total / len(temperaturas)
    return promedio

# Función principal para coordinar el flujo del programa
def main():
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio_semanal(temperaturas)
    print(f"\nLas temperaturas ingresadas son: {temperaturas}")
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}")

# Ejecución del programa
if __name__ == "__main__":
    main()