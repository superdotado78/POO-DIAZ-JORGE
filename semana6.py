#clase madre: operaciones matematicas basicas  entre dos numeros
class OperMatem:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def operacion(self):
        pass
#clases hijas:
class Suma (OperMatem):
    def operacion(self) :
        return self.a+self.b
    def __str__(self):
        return f"La Suma de {self.a} y {self.b} es {self.operacion()}"


class Resta (OperMatem):
    def operacion(self):
        return self.a - self.b
    def __str__(self):
        return f"La resta de {self.a} menos {self.b} es {self.operacion()}"

class Mult (OperMatem):
    def operacion(self):
        return self.a * self.b
    def __str__(self):
        return f"La multiplicaion de {self.a} con {self.b} es {self.operacion()}"

class Div (OperMatem):
    def operacion(self):
        return self.a/ self.b
    def __str__(self):
        return f"La dividion entre {self.a} y {self.b} es {self.operacion()}"

def calculo(numeros):
    print(numeros)

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

sum=Suma(a,b)
res=Resta(a,b)
multi=Mult(a,b)
divi=Div(a,b)
calculo(sum)
calculo(res)
calculo(multi)
calculo(divi)


