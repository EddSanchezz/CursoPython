import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def graficar_3D(funcion, x_range, y_range, resolution=500):

    x = np.linspace(x_range[0], x_range[1], resolution)
    y = np.linspace(y_range[0], y_range[1], resolution)
    X, Y = np.meshgrid(x, y)

    # Evaluar la función en la malla de puntos
    Z = funcion(X, Y)

    # Crear la figura 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Graficar la superficie
    ax.plot_surface(X, Y, Z, cmap="viridis", edgecolor="none")

    # Etiquetas y título
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Gráfica de la función en R3')

    plt.show()
