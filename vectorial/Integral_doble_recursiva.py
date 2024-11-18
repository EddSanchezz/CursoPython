import Grafica_R3 as gr
from vectorial.Integral_doble import funcion


class Volumen:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.n = 0
        self.m = 0
        self.dX = 0.0
        self.dY = 0.0
        self.suma = 0.0

    def calcular(self):
        self.suma = self._calcular(0, 0)
        print(f"El volumen aproximado bajo la superficie es de: {self.suma}")

    def _calcular(self, p, q):
        if self.n <= 0:
            print("Error: No se puede calcular el volumen con divisiones de 0.")
            return -1

        if p >= self.n:
            return 0.0

        if q >= self.m:
            return self._calcular(p + 1, 0)

        x = self.a + p * self.dX + self.dX / 2.0
        y = self.c + q * self.dY + self.dY / 2.0
        calcular_volum = (x**2 + y**2) * self.dX * self.dY
        return calcular_volum + self._calcular(p, q + 1)


if __name__ == "__main__":
    vol = Volumen()
    try:
        vol.a = int(input("Ingrese el valor inferior del eje x: "))
        vol.b = int(input("Ingrese el valor superior del eje x: "))
        vol.c = int(input("Ingrese el valor inferior del eje y: "))
        vol.d = int(input("Ingrese el valor superior del eje y: "))
        vol.n = int(input("Ingrese el valor por el que quiere dividir el eje x: "))
        vol.m = int(input("Ingrese el valor por el que quiere dividir el eje y: "))

        if vol.n <= 0 or vol.m <= 0:
            print("Los valores de n y m deben ser mayores a 0.")
        else:
            vol.dX = (vol.b - vol.a) / vol.n
            vol.dY = (vol.d - vol.c) / vol.m
            vol.calcular()
    except ValueError:
        print("Por favor, ingrese valores válidos.")

    gr.graficar_3D(funcion, (vol.a, vol.b), (vol.c, vol.d))
