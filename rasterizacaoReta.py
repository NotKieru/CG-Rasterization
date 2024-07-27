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

