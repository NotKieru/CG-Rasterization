import numpy as np
import matplotlib.pyplot as plt

def normalize_point(x, y, x_min, x_max, y_min, y_max):
    """
    Normaliza um ponto (x, y) para o intervalo [-1, 1] com base nos intervalos fornecidos.
    """
    x_normalized = 2 * (x - x_min) / (x_max - x_min) - 1
    y_normalized = 2 * (y - y_min) / (y_max - y_min) - 1
    return x_normalized, y_normalized

def denormalize_point(x, y, x_min, x_max, y_min, y_max):
    """
    Desnormaliza um ponto (x, y) do intervalo [-1, 1] para os intervalos fornecidos.
    """
    x_denormalized = (x + 1) * (x_max - x_min) / 2 + x_min
    y_denormalized = (y + 1) * (y_max - y_min) / 2 + y_min
    return x_denormalized, y_denormalized

def rasterize_line(x0, y0, x1, y1, width, height):
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

# Definir os pontos de início e fim da reta no intervalo [-1, 1]
x0, y0 = -0.5, -0.5
x1, y1 = 0.5, 0.5

# Definir a resolução da imagem
width = 100
height = 100

# Rasterizar a reta
image = rasterize_line(x0, y0, x1, y1, width, height)

# Mostrar a imagem
plt.imshow(image, cmap='gray', origin='upper')
plt.title('Rasterização de Segmento de Reta em Imagem 100x100')
# plt.xlim(0, resolution[0])
# plt.ylim(0, resolution[1])
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
