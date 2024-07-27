import numpy as np
import matplotlib.pyplot as plt

def curva_Hermite(p0, p1, t0, t1, numero_de_Pontos):
    t = np.linspace(0, 1, numero_de_Pontos)
    x = (2*t**3 - 3*t**2 + 1) * p0[0] + (t**3 - 2*t**2 + t) * t0[0] + (-2*t**3 + 3*t**2) * p1[0] + (t**3 - t**2) * t1[0]
    y = (2*t**3 - 3*t**2 + 1) * p0[1] + (t**3 - 2*t**2 + t) * t0[1] + (-2*t**3 + 3*t**2) * p1[1] + (t**3 - t**2) * t1[1]
    return np.column_stack((x, y))

def dda_reta(x0, y0, x1, y1, resolucao):
    imagem = np.zeros((resolucao, resolucao))
    dx = x1 - x0
    dy = y1 - y0
    steps = int(max(abs(dx), abs(dy)))  #converte os steps para inteiros #AJEITAR, dá erro sem ser inteiro
    if steps == 0:
        return imagem
    
    incremento_x = dx / steps
    incremento_y = dy / steps
    x = x0
    y = y0
    for _ in range(steps + 1):  # Adiciona o ponto final
        if 0 <= int(round(x)) < resolucao and 0 <= int(round(y)) < resolucao:
            imagem[int(round(y)), int(round(x))] = 1
        x += incremento_x
        y += incremento_y
    return imagem

def rasterize_curva_Hermite(p0, p1, t0, t1, resolucao, numero_de_Segmentos):
    numero_de_Pontos = numero_de_Segmentos + 1
    pontos_Curva = curva_Hermite(p0, p1, t0, t1, numero_de_Pontos)
    
    imagem = np.zeros((resolucao, resolucao))
    for i in range(numero_de_Pontos - 1):
        x0, y0 = pontos_Curva[i]
        x1, y1 = pontos_Curva[i + 1]
        line_imagem = dda_reta(x0, y0, x1, y1, resolucao)
        imagem = np.maximum(imagem, line_imagem)
    
    return imagem

