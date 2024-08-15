import numpy as np
import matplotlib.pyplot as plt

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class CurvaHermite:
    def __init__(self, pontos, tangentes):
        self.pontos = pontos
        self.tangentes = tangentes

    def calcular_curva(self, num_points, p1, t1, p2, t2):
        t = np.linspace(0, 1, num_points)
        h00 = 2*t**3 - 3*t**2 + 1
        h01 = -2*t**3 + 3*t**2
        h10 = t**3 - 2*t**2 + t
        h11 = t**3 - t**2

        x = h00*p1.x + h01*p2.x + h10*t1.x + h11*t2.x
        y = h00*p1.y + h01*p2.y + h10*t1.y + h11*t2.y

        return x, y

    def normalizar_coordenadas(self, x, y):
        x_min, x_max = np.min(x), np.max(x)
        y_min, y_max = np.min(y), np.max(y)
        
        # Normalização para o intervalo [-1, 1]
        x = 2 * (x - x_min) / (x_max - x_min) - 1
        y = 2 * (y - y_min) / (y_max - y_min) - 1
        
        return x, y

    def escalonar_para_resolucao(self, x, y, resolution):
        width, height = resolution
        x = (x + 1) / 2 * width
        y = (y + 1) / 2 * height
        return x, y

    def rasterizar_linha(self, x1, y1, x2, y2):
        pontos = []

        dx = x2 - x1
        dy = y2 - y1
        passos = int(max(abs(dx), abs(dy)))

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

        plt.figure(figsize=(resolution[0] / 100, resolution[1] / 100), dpi=100)
        plt.title(f"Curva de Hermite com {num_segments} segmentos")
        plt.xlim(0, resolution[0])
        plt.ylim(0, resolution[1])
        plt.gca().set_aspect('equal', adjustable='box')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)

        for i in range(len(self.pontos) - 1):
            x, y = self.calcular_curva(num_points, self.pontos[i], self.tangentes[i], self.pontos[i + 1], self.tangentes[i + 1])
            x, y = self.normalizar_coordenadas(x, y)
            x, y = self.escalonar_para_resolucao(x, y, resolution)

            for j in range(len(x) - 1):
                pontos_segmento = self.rasterizar_linha(x[j], y[j], x[j + 1], y[j + 1])
                px, py = zip(*pontos_segmento)
                
                plt.plot(px[1:-1], py[1:-1], 'ks', markersize=2, label='Pontos Internos' if j == 0 and i == 0 else "")
                plt.plot([px[0], px[-1]], [py[0], py[-1]], 'ro', markersize=5, label='Pontos Finais' if j == 0 and i == 0 else "")
        
        plt.legend()
        plt.show()


# Exemplo de uso com 3 pontos
# Código é apenas para testes
# if __name__ == '__main__':
#     pontos = [Ponto(0.2, 0.2), Ponto(-0.3, -0.4), Ponto(0.4, -0.2)]
#     tangentes = [Ponto(0.9, 0.4), Ponto(-1, -0.8), Ponto(0.3, 0.5)]

#     curva = CurvaHermite(pontos, tangentes)
#     resolucoes = [(800, 600)]
#     num_segments_list = [5, 20, 50]

#     for res in resolucoes:
#         for num_segments in num_segments_list:
#             curva.plotar_curva(num_segments, res)
