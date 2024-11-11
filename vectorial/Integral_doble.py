import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import grafica_R3 as gr


def funcion(x,y):
    return x**2 + y**2

# aplica la doble sumatoria
def integral_doble(a, b, c, d, n, m):
    dx = (b - a) / n
    dy = (d - c) / m

    volumen_total = 0.0

    for i in range(n):
        for j in range(m):
            x = a + (i + 0.5) * dx
            y = c + (j + 0.5) * dy
            volumen_total += funcion(x, y) * dx * dy

    return volumen_total


#crea la grafica de la función en R3
def plot_function(f, a, b, c, d, nx=100, ny=100):
    x = np.linspace(a, b, nx)
    y = np.linspace(c, d, ny)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='k', alpha=0.7)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('f(X, Y)')
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
    plt.show()

a = int(input("ingrese el intervalo en el que inicia x: "))
b = int(input("ingrese el intervalo en el que finaliza x: "))
c = int(input("ingrese el intervalo en el que inicia x:"))
d = int(input("ingrese el intervalo en el que finaliza x: "))
n = int(input("el numero de veces que desea dividir x: "))
m = int(input("el numero de veces que desea dividir y: "))
resultado = integral_doble( a, b, c, d, n, m)
print("El resultado es: ", resultado)

gr.graficar_3D(funcion,(a,b),(c,d))

