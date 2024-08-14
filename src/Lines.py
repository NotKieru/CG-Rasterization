import matplotlib.pyplot as plt
import numpy as np


# Código baseado no algoritmo DDA(Digital Differential Analyzer)
def raster_line(x0, y0, x1, y1, res_width, res_height):
    x0 = x0 + res_width
    x1 = x1 + res_width

    y0 = y0 + res_height
    y1 = y1 + res_height

    res_width = res_width * 2
    res_height = res_height * 2

    imagem = np.zeros((res_width, res_height))

    # definir |Δx|, |Δy| e seus valores absolutos
    dx = x1 - x0
    dy = y1 - y0
    steps = max(abs(dx), abs(dy))

    # Verifica de a linha está na vertical
    if dx == 0:
        for y in range(min(int(round(y0)), int(round(y1))), max(int(round(y0)), int(round(y1)) + 1)):
            if 0 <= int(round(x0)) < res_width and 0 <= y < res_height:
                imagem[int(round(x0)), y] = 1
        return imagem

    # Verifica de a linha está na vertical
    if dy == 0:
        for x in range(min(int(round(x0)), int(round(x1))), max(int(round(x0)), int(round(x1)) + 1)):
            if 0 <= x < res_width and 0 <= int(round(y0)) < res_height:
                imagem[x, int(round(y0))] = 1
        return imagem

    # Calculo dos incrementos
    incremento_X = dx / steps
    incremento_Y = dy / steps

    x = x0
    y = y0

    for _ in range(steps):
        try:
            if 0 <= int(round(x)) < res_width and 0 <= int(round(y)) < res_height:
                imagem[int(round(x)), int(round(y))] = 1
            x += incremento_X
            y += incremento_Y
        except Exception as e:
            dummy = 0

    return imagem


def plot_image(image, title, resolution_width, resolution_height):
    extent = [resolution_width * -1, resolution_width, resolution_height * -1, resolution_height]

    plt.figure(figsize=(12, 12))
    plt.imshow(image, extent=extent, origin='lower', cmap='gray', vmin=-1, vmax=1)
    plt.xlim(resolution_width * -1, resolution_width)

    x_ticks, y_ticks = [-resolution_width, 0, resolution_width], [-resolution_height, 0, resolution_height],
    tick_labels = ["-1", "0", "1"]

    plt.xticks(ticks=x_ticks, labels=tick_labels)
    plt.yticks(ticks=y_ticks, labels=tick_labels)

    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')

    plt.ylim(resolution_height * -1, resolution_height)
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.title(f'{title}')
    plt.axis('on')
    plt.suptitle(f'resolucao: {resolution_width}x{resolution_height}')
    plt.show()
