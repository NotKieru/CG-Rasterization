import numpy as np

def normalize_point(x, y, x_min, x_max, y_min, y_max):
    """
    Normaliza um ponto (x, y) para o intervalo [-1, 1] com base nos intervalos fornecidos.

    Args:
        x (float): Coordenada x do ponto a ser normalizado.
        y (float): Coordenada y do ponto a ser normalizado.
        x_min (float): Valor mínimo de x do intervalo de entrada.
        x_max (float): Valor máximo de x do intervalo de entrada.
        y_min (float): Valor mínimo de y do intervalo de entrada.
        y_max (float): Valor máximo de y do intervalo de entrada.

    Returns:
        tuple: Coordenadas normalizadas (x, y).
    """
    x_normalized = 2 * (x - x_min) / (x_max - x_min) - 1
    y_normalized = 2 * (y - y_min) / (y_max - y_min) - 1
    return x_normalized, y_normalized

def rasterize_line(x0, y0, x1, y1, width, height):
    """
    Rasteriza uma linha entre os pontos (x0, y0) e (x1, y1) em uma imagem de resolução (width, height).

    Args:
        x0 (float): Coordenada x do ponto inicial da linha.
        y0 (float): Coordenada y do ponto inicial da linha.
        x1 (float): Coordenada x do ponto final da linha.
        y1 (float): Coordenada y do ponto final da linha.
        width (int): Largura da imagem de saída.
        height (int): Altura da imagem de saída.

    Returns:
        numpy.ndarray: Uma matriz 2D representando a imagem rasterizada, com 1s indicando os pixels da linha e 0s em outros lugares.
    """
    # Normaliza as coordenadas para o intervalo [-1, 1]
    x0, y0 = normalize_point(x0, y0, -1, 1, -1, 1)
    x1, y1 = normalize_point(x1, y1, -1, 1, -1, 1)
    
    # Converte as coordenadas normalizadas para coordenadas de pixels da imagem
    x0 = int((x0 + 1) * (width - 1) / 2)
    y0 = int((y0 + 1) * (height - 1) / 2)
    x1 = int((x1 + 1) * (width - 1) / 2)
    y1 = int((y1 + 1) * (height - 1) / 2)
    
    # Cria uma imagem em branco
    image = np.zeros((height, width), dtype=np.uint8)
    
    # Calcula a diferença e o número de passos para desenhar a linha
    dx = x1 - x0
    dy = y1 - y0
    steps = max(abs(dx), abs(dy))
    
    # Trata o caso onde a linha é um único ponto
    if steps == 0:
        if 0 <= x0 < width and 0 <= y0 < height:
            image[y0, x0] = 1
        return image
    
    steps = int(steps)
    x_increment = dx / steps
    y_increment = dy / steps
    
    x = x0
    y = y0
    
    # Desenha a linha incrementando as coordenadas x e y
    for _ in range(steps + 1):
        if 0 <= int(round(y)) < height and 0 <= int(round(x)) < width:
            image[int(round(y)), int(round(x))] = 1
        x += x_increment
        y += y_increment
    
    return image

def plot_rasterized_image(segments, width, height, ax):
    """
    Plota a imagem rasterizada com todos os segmentos de linha especificados.

    Args:
        segments (list of tuples): Lista de segmentos de linha, onde cada segmento é uma tupla com dois pontos (x0, y0) e (x1, y1).
        width (int): Largura da imagem de saída.
        height (int): Altura da imagem de saída.
        ax (matplotlib.axes.Axes): O eixo do Matplotlib no qual a imagem rasterizada será plotada.

    Returns:
        None: A função atualiza o eixo fornecido com a imagem rasterizada.
    """
    # Cria uma imagem em branco para combinar todos os segmentos de linha
    combined_image = np.zeros((height, width), dtype=np.uint8)
    
    # Rasteriza cada segmento de linha e combina os resultados
    for (x0, y0), (x1, y1) in segments:
        line_image = rasterize_line(x0, y0, x1, y1, width, height)
        combined_image = np.maximum(combined_image, line_image)
    
    # Plota a imagem rasterizada combinada
    ax.clear()
    ax.imshow(combined_image, cmap='gray', origin='lower')
    ax.set_title('Imagem Rasterizada')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
