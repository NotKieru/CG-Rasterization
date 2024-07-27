import numpy as np
import matplotlib.pyplot as plt

#trambiques da lógica do Hermite
def curva_Hermite(p0, p1, t0, t1, numero_de_Pontos):
    t = np.linspace(0, 1, numero_de_Pontos)
    x = (2*t**3 - 3*t**2 + 1) * p0[0] + (t**3 - 2*t**2 + t) * t0[0] + (-2*t**3 + 3*t**2) * p1[0] + (t**3 - t**2) * t1[0]
    y = (2*t**3 - 3*t**2 + 1) * p0[1] + (t**3 - 2*t**2 + t) * t0[1] + (-2*t**3 + 3*t**2) * p1[1] + (t**3 - t**2) * t1[1]
    return np.column_stack((x, y))

def dda_reta(x0, y0, x1, y1, resolucao):
    imagem = np.zeros((resolucao, resolucao))
    dx = x1 - x0
    dy = y1 - y0
    steps = int(max(abs(dx), abs(dy)))  #converte os steps para inteiros #OBS: AJEITAR, dá erro sem ser inteiro
    if steps == 0:
        return imagem
    
    incremento_x = dx / steps
    incremento_y = dy / steps
    x = x0
    y = y0
    for _ in range(steps + 1):  # Adiciona o . final
        if 0 <= int(round(x)) < resolucao and 0 <= int(round(y)) < resolucao:
            imagem[int(round(y)), int(round(x))] = 1
        x += incremento_x
        y += incremento_y
    return imagem

def rasterizar_curva_Hermite(p0, p1, t0, t1, resolucao, numero_de_Segmentos):
    numero_de_Pontos = numero_de_Segmentos + 1
    pontos_Curva = curva_Hermite(p0, p1, t0, t1, numero_de_Pontos)
    
    imagem = np.zeros((resolucao, resolucao))
    for i in range(numero_de_Pontos - 1):
        x0, y0 = pontos_Curva[i]
        x1, y1 = pontos_Curva[i + 1]
        line_imagem = dda_reta(x0, y0, x1, y1, resolucao)
        imagem = np.maximum(imagem, line_imagem)
    
    return imagem

# Definindo diferentes curvas de Hermite
curvas = [
    ((10, 10), (90, 90), (10, 70), (300, 10)),
    ((10, 10), (90, 90), (0, 0), (0, 0))  # P1 e P2 iguais
]

resolucoes = [400]
lista_num_segmentos = [10, 20, 30]

# Pinta e exibe as curvas
for resolucao in resolucoes:
    plt.figure(figsize=(110, 110))
    for i, curva in enumerate(curvas):
        p0, p1, t0, t1 = curva
        for num_segmentos in lista_num_segmentos:
            imagem = rasterizar_curva_Hermite(p0, p1, t0, t1, resolucao, num_segmentos)
            plt.subplot(len(curvas), len(lista_num_segmentos), i * len(lista_num_segmentos) + lista_num_segmentos.index(num_segmentos) + 1)
            plt.imshow(imagem, cmap='gray', vmin=0, vmax=1)
            plt.title(f'Curvas {i+1} Segments {num_segmentos} Res {resolucao}')
            plt.axis('off')
    plt.suptitle(f'resolucao: {resolucao}')
    plt.show()
