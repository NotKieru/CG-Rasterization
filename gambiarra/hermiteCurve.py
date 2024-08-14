import numpy as np
import matplotlib.pyplot as plt

def hermite_curve(p1, t1, p2, t2, num_points):
    t = np.linspace(0, 1, num_points)
    h00 = 2*t**3 - 3*t**2 + 1
    h01 = -2*t**3 + 3*t**2
    h10 = t**3 - 2*t**2 + t
    h11 = t**3 - t**2

    x = h00*p1[0] + h01*p2[0] + h10*t1[0] + h11*t2[0]
    y = h00*p1[1] + h01*p2[1] + h10*t1[1] + h11*t2[1]

    return x, y

def normalize_coordinates(x, y, resolution):
    width, height = resolution
    x = (x + 1) / 2 * width  # Transformar x de [-1, 1] para [0, width]
    y = (y + 1) / 2 * height  # Transformar y de [-1, 1] para [0, height]
    return x, y

def plot_segments(x, y, num_segments, resolution):
    plt.figure(figsize=(resolution[0] / 100, resolution[1] / 100), dpi=100)
    plt.title(f"Curva de Hermite com {num_segments} segmentos")
    plt.xlim(0, resolution[0])
    plt.ylim(resolution[1], 0)  # Inverter y para alinhar com o sistema de coordenadas da imagem
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)

    for i in range(len(x) - 1):
        plt.plot([x[i], x[i+1]], [y[i], y[i+1]], marker='o', linestyle='-', color='blue')

    plt.show()

def rasterize_curve(p1, t1, p2, t2, num_segments, resolution):
    # Obtendo pontos da curva de Hermite
    x, y = hermite_curve(p1, t1, p2, t2, num_segments + 1)  # +1 para incluir o último ponto
    
    # Normalizando coordenadas
    x, y = normalize_coordinates(x, y, resolution)

    # Plotar segmentos
    plot_segments(x, y, num_segments, resolution)

def generate_rasterized_curves(p1, t1, p2, t2, resolutions, num_segments_list):
    for res in resolutions:
        for num_segments in num_segments_list:
            rasterize_curve(p1, t1, p2, t2, num_segments, res)

# Curvas de exemplo
p1 = (0.2, 0.2)
t1 = (0.9, 0.4)
p2 = (-0.3, -0.4)
t2 = (-1, -0.8)

resolutions = [(800, 600)]  # Resolução em pixels
num_segments_list = [5, 20, 50]

generate_rasterized_curves(p1, t1, p2, t2, resolutions, num_segments_list)
