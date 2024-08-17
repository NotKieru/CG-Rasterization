import numpy as np
import matplotlib.pyplot as plt

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class CurvaHermite:
    def __init__(self, pontos, tangentes):
        if len(pontos) != len(tangentes):
            raise ValueError("O número de pontos deve ser igual ao número de tangentes.")
        self.pontos = pontos
        self.tangentes = tangentes

    def calcular_curva(self, num_points, p1, t1, p2, t2):
        t = np.linspace(0, 1, num_points)
        h00 = 2 * t**3 - 3 * t**2 + 1
        h01 = -2 * t**3 + 3 * t**2
        h10 = t**3 - 2 * t**2 + t
        h11 = t**3 - t**2

        x = h00 * p1.x + h01 * p2.x + h10 * t1.x + h11 * t2.x
        y = h00 * p1.y + h01 * p2.y + h10 * t1.y + h11 * t2.y

        return x, y

    def normalizar_coordenadas(self, x, y):
        x_min, x_max = np.min(x), np.max(x)
        y_min, y_max = np.min(y), np.max(y)
        
        # Normalização para o intervalo [-1, 1]
        x_range = x_max - x_min
        y_range = y_max - y_min

        # Evita divisão por zero
        x_range = x_range if x_range != 0 else 1
        y_range = y_range if y_range != 0 else 1

        x = 2 * (x - x_min) / x_range - 1
        y = 2 * (y - y_min) / y_range - 1

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

    def normalizar_tangentes(self):
        """Normaliza as tangentes para o intervalo [-1, 1]."""
        tangentes = np.array([(t.x, t.y) for t in self.tangentes])
        x_min, x_max = np.min(tangentes[:, 0]), np.max(tangentes[:, 0])
        y_min, y_max = np.min(tangentes[:, 1]), np.max(tangentes[:, 1])

        x_range = x_max - x_min
        y_range = y_max - y_min

        # Evita divisão por zero
        x_range = x_range if x_range != 0 else 1
        y_range = y_range if y_range != 0 else 1

        tangentes[:, 0] = 2 * (tangentes[:, 0] - x_min) / x_range - 1
        tangentes[:, 1] = 2 * (tangentes[:, 1] - y_min) / y_range - 1

        return [Ponto(x, y) for x, y in tangentes]

    def plotar_curva(self, num_segments, resolution, ax1):
        num_points = num_segments * 10 + 1  # Aumentar a densidade dos pontos para melhor visualização

        if len(self.pontos) < 2:
            print("Número insuficiente de pontos para gerar a curva.")
            return

        # Normalizar as tangentes
        tangentes_normalizadas = self.normalizar_tangentes()

        # # Gráfico normalizado
        # for i in range(len(self.pontos) - 1):
        #     x, y = self.calcular_curva(num_points, self.pontos[i], tangentes_normalizadas[i], self.pontos[i + 1], tangentes_normalizadas[i + 1])
        #     x, y = self.normalizar_coordenadas(x, y)
        #     ax1.plot(x, y, 'k-', lw=1)

        # ax1.set_title("Espaço Normalizado")
        # ax1.set_xlim(-1, 1)
        # ax1.set_ylim(-1, 1)
        # ax1.set_aspect('equal', adjustable='box')
        # ax1.grid(True)

        # Gráfico rasterizado
        width, height = resolution
        combined_image = np.zeros((height, width), dtype=np.uint8)

        for i in range(len(self.pontos) - 1):
            x, y = self.calcular_curva(num_points, self.pontos[i], tangentes_normalizadas[i], self.pontos[i + 1], tangentes_normalizadas[i + 1])
            x, y = self.normalizar_coordenadas(x, y)
            x, y = self.escalonar_para_resolucao(x, y, resolution)

            for j in range(len(x) - 1):
                pontos_segmento = self.rasterizar_linha(x[j], y[j], x[j + 1], y[j + 1])
                for px, py in pontos_segmento:
                    if 0 <= int(round(py)) < height and 0 <= int(round(px)) < width:
                        combined_image[int(round(py)), int(round(px))] = 1

        ax1.clear()
        ax1.imshow(combined_image, cmap='gray', origin='lower')
        ax1.set_title("Imagem Rasterizada")
        ax1.set_xlim(0, width)
        ax1.set_ylim(0, height)
        ax1.set_aspect('equal', adjustable='box')
        ax1.grid(True)
