import math
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg

#Código baseado no algoritmo DDA(Digital Differential Analyzer)
def rasterizar_reta(x0, y0, x1, y1, resolucao):

    imagem = np.zeros((resolucao, resolucao))

    #definir |Δx|, |Δy| e seus valores absolutos
    dx = x1 - x0
    dy = y1 - y0
    steps = max(abs(dx), abs(dy))


    #Verifica de a linha está na vertical
    if dx == 0:  
        for y in range(min(int(round(y0)), int(round(y1))), max(int(round(y0)), int(round(y1)) + 1)):
            if 0 <= int(round(x0)) < resolucao and 0 <= y < resolucao:
                imagem[y, int(round(x0))] = 1
        return imagem
    
    #Verifica de a linha está na vertical
    if dy == 0:
        for x in range(min(int(round(x0)), int(round(x1))), max(int(round(x0)), int(round(x1)) + 1)):
            if 0 <= x < resolucao and 0 <= int(round(y0)) < resolucao:
                imagem[int(round(y0)), x] = 1
        return imagem

    #Calculo dos incrementos
    incremento_X = dx / steps
    incremento_Y = dy / steps

    x = x0
    y = y0

    for _ in range(steps):
            if 0 <= int(round(x)) < resolucao and 0 <= int(round(y)) < resolucao:
                imagem[int(round(y)), int(round(x))] = 1
            x += incremento_X
            y += incremento_Y
        
    return imagem

#OBS: AJEITAR ISSO DAQUI DEPOIS< AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# Exemplo de criação de 5 segmentos de retas e 4 resoluções. 
resolutions = [100, 200, 300, 400]
lines = [
    (10, 10, 90, 90),
    (20, 10, 70, 80),
    (30, 30, 90, 10),
    (40, 50, 90, 50),
    (10, 20, 10, 80)
]

#pinta nas resoluções
for resolution in resolutions:
    plt.figure(figsize=(10, 10))
    for i, (x0, y0, x1, y1) in enumerate(lines):
        image = rasterizar_reta(x0, y0, x1, y1, resolution)
        plt.subplot(2, 3, i+1)
        plt.imshow(image, cmap='gray', vmin=0, vmax=1)
        plt.title(f'Line {i+1}')
        plt.axis('off')
    plt.suptitle(f'Resolution: {resolution}')
    plt.show()