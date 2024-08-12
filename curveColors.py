import numpy as np
import matplotlib.pyplot as plt

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class CurvaHermite:
    def __init__(self, p1, t1, p2, t2):
        self.p1 = p1
        self.t1 = t1
        self.p2 = p2
        self.t2 = t2

    def calcular_curva(self, num_points):
        t = np.linspace(0, 1, num_points)
        h00 = 2*t**3 - 3*t**2 + 1
        h01 = -2*t**3 + 3*t**2
        h10 = t**3 - 2*t**2 + t
        h11 = t**3 - t**2

        x = h00*self.p1.x + h01*self.p2.x + h10*self.t1.x + h11*self.t2.x
        y = h00*self.p1.y + h01*self.p2.y + h10*self.t1.y + h11*self.t2.y

        return x, y

    def normalizar_coordenadas(self, x, y, resolution):
        width, height = resolution
        x = (x + 1) / 2 * width
        y = (y + 1) / 2 * height
        return x, y

    def rasterizar_linha(self, x1, y1, x2, y2, num_points):
        pontos = []

        dx = x2 - x1
        dy = y2 - y1
        passos = int(max(abs(dx), abs(dy)))  # Converter para inteiro

        if passos == 0:
            return [(x1, y1)]

        x_inc = dx / passos
        y_inc = dy / passos

        x = x1
        y = y1

        for _ in range(passos + 1):
            pontos.append((round(x), round(y)))
            x += x_inc
            y += y_inc

        return pontos

    def plotar_curva(self, num_segments, resolution):
        num_points = num_segments + 1  # Número de pontos na curva
        x, y = self.calcular_curva(num_points)
        x, y = self.normalizar_coordenadas(x, y, resolution)
        
        plt.figure(figsize=(resolution[0] / 100, resolution[1] / 100), dpi=100)
        plt.title(f"Curva de Hermite com {num_segments} segmentos")
        plt.xlim(0, resolution[0])
        plt.ylim(0, resolution[1])
        plt.gca().set_aspect('equal', adjustable='box')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)

        for i in range(len(x) - 1):
            pontos_segmento = self.rasterizar_linha(x[i], y[i], x[i + 1], y[i + 1], num_segments)
            px, py = zip(*pontos_segmento)
            
            # Plotar os pontos internos
            plt.plot(px[1:-1], py[1:-1], 'ks', markersize=2, label='Pontos Internos' if i == 0 else "")
            # Plotar as pontas dos segmentos
            plt.plot([px[0], px[-1]], [py[0], py[-1]], 'ro', markersize=5, label='Pontos Finais' if i == 0 else "")
        
        plt.legend()
        plt.show()

# Pontos e tangentes para a curva de Hermite
p1 = Ponto(0.2, 0.2)
t1 = Ponto(0.4, 0.4)
p2 = Ponto(0.2, 0.2)
t2 = Ponto(-0.4, 0.4)

curva = CurvaHermite(p1, t1, p2, t2)
resolucoes = [(800, 600)]
num_segments_list = [5, 20, 50]

for res in resolucoes:
    for num_segments in num_segments_list:
        curva.plotar_curva(num_segments, res)
