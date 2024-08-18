import numpy as np
from matplotlib.path import Path
from scipy.ndimage import binary_fill_holes
import matplotlib.pyplot as plt

def normalize_point(x, y, x_min, x_max, y_min, y_max):
    """
    Normaliza um ponto (x, y) para o intervalo [-1, 1] com base nos intervalos fornecidos.
    
    :param x: Coordenada x do ponto
    :param y: Coordenada y do ponto
    :param x_min: Valor mínimo do intervalo de x
    :param x_max: Valor máximo do intervalo de x
    :param y_min: Valor mínimo do intervalo de y
    :param y_max: Valor máximo do intervalo de y
    :return: Coordenadas normalizadas (x, y) no intervalo [-1, 1]
    """
    x_normalized = 2 * (x - x_min) / (x_max - x_min) - 1
    y_normalized = 2 * (y - y_min) / (y_max - y_min) - 1
    return x_normalized, y_normalized

def scanline(vertices, width, height):
    """
    Rasteriza um polígono em uma imagem de resolução (width, height) usando o algoritmo de cruzamento.
    
    :param vertices: Lista de vértices do polígono
    :param width: Largura da imagem
    :param height: Altura da imagem
    :return: Imagem binária com o polígono preenchido
    """
    # Normaliza os pontos
    normalized_vertices = [normalize_point(x, y, -1, 1, -1, 1) for x, y in vertices]
    
    # Converte os pontos normalizados para a resolução da imagem
    vertices = [(int((x + 1) * (width - 1) / 2), int((y + 1) * (height - 1) / 2)) for x, y in normalized_vertices]
    
    # Cria uma imagem em branco
    image = np.zeros((height, width), dtype=np.uint8)
    
    # Cria um Path do matplotlib para o polígono
    path = Path(vertices)
    
    # Gera uma grade de coordenadas (x, y)
    x, y = np.meshgrid(np.arange(width), np.arange(height))
    points = np.vstack((x.ravel(), y.ravel())).T
    
    # Verifica se os pontos estão dentro do polígono
    grid = path.contains_points(points)
    
    # Preenche a imagem com os pontos dentro do polígono
    image[grid.reshape(height, width)] = 1
    
    # Preenchimento usando flood-fill para lidar com qualquer lacuna interna
    flood_fill = binary_fill_holes(image).astype(np.uint8)
    
    return flood_fill

def generate_triangle(rotation=0):
    """
    Gera um triângulo equilátero rotacionado.
    
    :param rotation: Ângulo de rotação em graus
    :return: Vértices do triângulo rotacionado
    """
    # Define os vértices do triângulo equilátero no sistema de coordenadas original
    vertices = [
        (0, np.sqrt(3)/3),  # Vértice superior do triângulo
        (-0.5, -np.sqrt(3)/6),  # Vértice inferior esquerdo
        (0.5, -np.sqrt(3)/6)  # Vértice inferior direito
    ]
    
    # Converte o ângulo de rotação de graus para radianos
    angle_rad = np.deg2rad(rotation)
    cos_angle = np.cos(angle_rad)  # Cálculo do cosseno do ângulo de rotação
    sin_angle = np.sin(angle_rad)  # Cálculo do seno do ângulo de rotação
    
    # Aplica a rotação aos vértices usando a matriz de rotação
    rotated_vertices = [
        (x * cos_angle - y * sin_angle, x * sin_angle + y * cos_angle)
        for x, y in vertices
    ]
    
    return rotated_vertices

def generate_square(rotation=0):
    """
    Gera um quadrado rotacionado.
    
    :param rotation: Ângulo de rotação em graus
    :return: Vértices do quadrado rotacionado
    """
    # Define os vértices do quadrado no sistema de coordenadas original
    vertices = [
        (-0.5, -0.5),  # Vértice inferior esquerdo
        (0.5, -0.5),   # Vértice inferior direito
        (0.5, 0.5),    # Vértice superior direito
        (-0.5, 0.5)    # Vértice superior esquerdo
    ]
    
    # Converte o ângulo de rotação de graus para radianos
    angle_rad = np.deg2rad(rotation)
    cos_angle = np.cos(angle_rad)  # Cálculo do cosseno do ângulo de rotação
    sin_angle = np.sin(angle_rad)  # Cálculo do seno do ângulo de rotação
    
    # Aplica a rotação aos vértices usando a matriz de rotação
    rotated_vertices = [
        (x * cos_angle - y * sin_angle, x * sin_angle + y * cos_angle)
        for x, y in vertices
    ]
    
    return rotated_vertices

def generate_hexagon(rotation=0):
    """
    Gera um hexágono regular rotacionado.
    
    :param rotation: Ângulo de rotação em graus
    :return: Vértices do hexágono rotacionado
    """
    # Define os vértices do hexágono regular no sistema de coordenadas original
    vertices = [
        (1, 0),                    # Vértice 1: ponto no eixo x positivo
        (0.5, np.sqrt(3) / 2),  # Vértice 2: ponto a 60 graus do eixo x
        (-0.5, np.sqrt(3) / 2), # Vértice 3: ponto a 120 graus do eixo x
        (-1, 0),                  # Vértice 4: ponto no eixo x negativo
        (-0.5, -np.sqrt(3) / 2), # Vértice 5: ponto a 240 graus do eixo x
        (0.5, -np.sqrt(3) / 2)   # Vértice 6: ponto a 300 graus do eixo x
    ]
    
    # Converte o ângulo de rotação de graus para radianos
    angle_rad = np.deg2rad(rotation)
    cos_angle = np.cos(angle_rad)  # Cálculo do cosseno do ângulo de rotação
    sin_angle = np.sin(angle_rad)  # Cálculo do seno do ângulo de rotação
    
    # Aplica a rotação aos vértices usando a matriz de rotação
    rotated_vertices = [
        (x * cos_angle - y * sin_angle, x * sin_angle + y * cos_angle)
        for x, y in vertices
    ]
    
    return rotated_vertices

def get_polygon_vertices(shape, rotation=0):
    """
    Retorna os vértices do polígono com base na forma e rotação.
    
    :param shape: Tipo de forma do polígono ('Trianuglo', 'Quadrado', 'Hexagono')
    :param rotation: Ângulo de rotação em graus
    :return: Vértices do polígono rotacionado
    """
    if shape == 'Triangulo 1':
        return generate_triangle(rotation)
    elif shape == 'Triangulo 2':
        return generate_triangle(rotation=30)
    elif shape == 'Quadrado 1':
        return generate_square(rotation)
    elif shape == 'Quadrado 2':
        return generate_square(rotation=45)
    elif shape == 'Hexagono 1':
        return generate_hexagon(rotation)
    elif shape == 'Hexagono 2':
        return generate_hexagon(rotation=30)
    else:
        raise ValueError("Unknown shape")

def plot_polygon(shape, rotation=0, width=100, height=100):
    """
    Plota o polígono com a rotação especificada.
    
    :param shape: Tipo de forma do polígono 
    :param rotation: Ângulo de rotação em graus
    :param width: Largura da imagem
    :param height: Altura da imagem
    """
    vertices = get_polygon_vertices(shape, rotation)
    image = scanline(vertices, width, height)
    
    plt.imshow(image, cmap='gray', origin='upper')
    plt.title(f'{shape} with {rotation}° rotation')
    plt.show()

# Exemplo de uso
# plot_polygon('Equilateral Triangle 1', rotation=30)