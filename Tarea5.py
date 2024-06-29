#El programa transforma un temporatura ingresada en grados centigrados a grados farenheit
def centig_fahren(centig):
    fah = (centig * 9/5) + 32
    return fah

# Ejemplo de uso
grados_cent = float(input("Ingresa la temperatura en grados centigrados: "))
grados_fah = centig_fahren(grados_cent)
print(f"{grados_cent} grados centigrados son equivalentes a {grados_fah} grados Fahrenheit.")
