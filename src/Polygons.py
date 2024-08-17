import numpy as np
import matplotlib.pyplot as plt

def normalize_point(x, y, x_min, x_max, y_min, y_max):
    """
    Normaliza um ponto (x, y) para o intervalo [-1, 1] com base nos intervalos fornecidos.
    """
    x_normalized = 2 * (x - x_min) / (x_max - x_min) - 1
    y_normalized = 2 * (y - y_min) / (y_max - y_min) - 1
    return x_normalized, y_normalized

def rasterize_polygon(vertices, width, height):
    """
    Rasteriza um polígono em uma imagem de resolução (width, height) usando o algoritmo de cruzamento.
    """
    # Normaliza os pontos
    normalized_vertices = [normalize_point(x, y, -1, 1, -1, 1) for x, y in vertices]
    # Converte os pontos normalizados para a resolução da imagem
    vertices = [(int((x + 1) * (width - 1) / 2), int((y + 1) * (height - 1) / 2)) for x, y in normalized_vertices]
    
    image = np.zeros((height, width), dtype=np.uint8)
    num_vertices = len(vertices)
    
    # Preenchimento de scanline
    for y in range(height):
        intersections = []
        for i in range(num_vertices):
            x0, y0 = vertices[i]
            x1, y1 = vertices[(i + 1) % num_vertices]
            
            # Verifica se a linha cruza a linha horizontal na coordenada y
            if min(y0, y1) <= y <= max(y0, y1):
                if y0 != y1:
                    x_intersection = x0 + (y - y0) * (x1 - x0) / (y1 - y0)
                    intersections.append(x_intersection)
        
        intersections.sort()
        
        # Preenche os pixels entre os pontos de interseção
        for i in range(0, len(intersections) - 1, 2):
            x_start = int(round(intersections[i]))
            x_end = int(round(intersections[i + 1]))
            if 0 <= x_start < width and 0 <= x_end < width:
                image[y, x_start:x_end + 1] = 1
    
    return image

def plot_rasterized_image(images, titles, width, height, ax):
    """
    Plota a imagem rasterizada com todos os polígonos.
    """
    ax.clear()
    for image, title in zip(images, titles):
        ax.imshow(image, cmap='gray', origin='lower')
        ax.set_title(title)
        plt.pause(1)
    plt.show()

def plot_normalized_polygon(vertices, ax, title):
    """
    Plota o polígono em um espaço normalizado [-1, 1].
    """
    ax.clear()
    vertices.append(vertices[0])  # Fecha o polígono
    xs, ys = zip(*vertices)
    ax.plot(xs, ys, marker='o')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.set_title(title)

def generate_triangle(rotation=0):
    """
    Gera um triângulo equilátero.
    """
    angle = np.deg2rad(rotation)
    cos_a = np.cos(angle)
    sin_a = np.sin(angle)
    vertices = [
        (0, 1),
        (np.sqrt(3)/2, -0.5),
        (-np.sqrt(3)/2, -0.5)
    ]
    rotated_vertices = [
        (x * cos_a - y * sin_a, x * sin_a + y * cos_a)
        for x, y in vertices
    ]
    return rotated_vertices

def generate_square(rotation=0):
    """
    Gera um quadrado.
    """
    angle = np.deg2rad(rotation)
    cos_a = np.cos(angle)
    sin_a = np.sin(angle)
    vertices = [
        (-0.5, -0.5),
        (0.5, -0.5),
        (0.5, 0.5),
        (-0.5, 0.5)
    ]
    rotated_vertices = [
        (x * cos_a - y * sin_a, x * sin_a + y * cos_a)
        for x, y in vertices
    ]
    return rotated_vertices

def generate_hexagon(rotation=0):
    """
    Gera um hexágono regular.
    """
    angle = np.deg2rad(rotation)
    cos_a = np.cos(angle)
    sin_a = np.sin(angle)
    vertices = [
        (np.cos(np.deg2rad(60 * i)), np.sin(np.deg2rad(60 * i)))
        for i in range(6)
    ]
    rotated_vertices = [
        (x * cos_a - y * sin_a, x * sin_a + y * cos_a)
        for x, y in vertices
    ]
    return rotated_vertices

def main():
    width, height = 600, 600
    
    # Definindo os polígonos
    polygons = [
        (generate_triangle(), "Triângulo Equilátero 1"),
        (generate_triangle(rotation=30), "Triângulo Equilátero 2"),
        (generate_square(), "Quadrado 1"),
        (generate_square(rotation=45), "Quadrado 2"),
        (generate_hexagon(), "Hexágono 1"),
        (generate_hexagon(rotation=30), "Hexágono 2")
    ]
    
    images = []
    titles = []
    
    for vertices, title in polygons:
        image = rasterize_polygon(vertices, width, height)
        images.append(image)
        titles.append(title)
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    plot_rasterized_image(images, titles, width, height, ax)

if __name__ == "__main__":
    main()
