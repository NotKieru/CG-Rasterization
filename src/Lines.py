import numpy as np
import matplotlib.pyplot as plt

def normalize_point(x, y, x_min, x_max, y_min, y_max):
    """
    Normaliza um ponto (x, y) para o intervalo [-1, 1] com base nos intervalos fornecidos.
    """
    x_normalized = 2 * (x - x_min) / (x_max - x_min) - 1
    y_normalized = 2 * (y - y_min) / (y_max - y_min) - 1
    return x_normalized, y_normalized

def rasterize_line(x0, y0, x1, y1, width, height):
    """
    Rasteriza uma linha entre (x0, y0) e (x1, y1) em uma imagem de resolução (width, height).
    """
    # Normalizar os pontos para o intervalo [-1, 1]
    x0, y0 = normalize_point(x0, y0, -1, 1, -1, 1)
    x1, y1 = normalize_point(x1, y1, -1, 1, -1, 1)
    
    # Converter as coordenadas normalizadas para a resolução da imagem
    x0 = int((x0 + 1) * (width - 1) / 2)
    y0 = int((y0 + 1) * (height - 1) / 2)
    x1 = int((x1 + 1) * (width - 1) / 2)
    y1 = int((y1 + 1) * (height - 1) / 2)
    
    # Criar uma imagem em branco
    image = np.zeros((height, width), dtype=np.uint8)
    
    # Calcular a diferença entre os pontos
    dx = x1 - x0
    dy = y1 - y0
    
    # Verificar o comprimento da reta
    steps = max(abs(dx), abs(dy))
    
    if steps == 0:
        # Caso trivial onde os dois pontos são o mesmo
        if 0 <= x0 < width and 0 <= y0 < height:
            image[y0, x0] = 1
        return image
    
    # Garantir que steps seja um número inteiro
    steps = int(steps)
    
    # Incrementos em x e y
    x_inc = dx / steps
    y_inc = dy / steps
    
    # Posições atuais
    x = x0
    y = y0
    
    for _ in range(steps + 1):
        # Marcar o pixel atual
        if 0 <= int(round(y)) < height and 0 <= int(round(x)) < width:
            image[int(round(y)), int(round(x))] = 1
        x += x_inc
        y += y_inc
    
    return image

def plot_lines(segments, width, height):
    """
    Plota múltiplos segmentos de reta em uma única imagem.
    
    Parameters:
    - segments: Lista de tuplas ((x0, y0), (x1, y1)) para cada segmento de reta.
    - width: Largura da imagem em pixels.
    - height: Altura da imagem em pixels.
    """
    # Criar uma imagem em branco
    combined_image = np.zeros((height, width), dtype=np.uint8)
    
    # Rasterizar cada segmento de reta
    for (x0, y0), (x1, y1) in segments:
        image = rasterize_line(x0, y0, x1, y1, width, height)
        combined_image = np.maximum(combined_image, image)
    
    # Mostrar a imagem
    plt.imshow(combined_image, cmap='gray', origin='upper')
    plt.title('Rasterização de Segmentos de Reta')
    plt.show()

# Definir os segmentos de reta
segments = [
    # Segmentos com inclinação positiva (crescendo)
    ((-0.8, -0.8), (0.8, 0.8)),  # |Δx| > |Δy|, m > 0
    ((-0.9, -0.4), (0.9, 0.4)),  # |Δx| > |Δy|, m > 0
    
    # Segmentos com inclinação negativa (decrescendo)
    ((-0.8, 0.2), (0.2, 0.8)),   # |Δy| > |Δx|, m < 0
    ((-0.5, -0.9), (0.5, 0.9)),   # |Δy| > |Δx|, m < 0
    
    # Segmentos horizontais e verticais
    ((-0.9, 0.1), (0.4, -0.8)),   # |Δx| > |Δy|, m < 0
    ((-0.5, 0.0), (0.5, 0.0)),    # Horizontal
    ((0.0, -0.5), (0.0, 0.5))     # Vertical
]

# Definir a resolução da imagem
width = 100
height = 100

# Plotar os segmentos de reta
plot_lines(segments, width, height)
