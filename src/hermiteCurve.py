import numpy as np
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        # Inicializa um ponto com coordenadas (x, y)
        self.x = x
        self.y = y

class HermiteCurve:
    def __init__(self, points, tangents):
        # Verifica se o número de pontos é igual ao número de tangentes
        if len(points) != len(tangents):
            raise ValueError("O número de pontos deve ser igual ao número de tangentes.")
        self.points = points
        self.tangents = tangents

    def compute_curve(self, num_points, p1, t1, p2, t2):
        """
        Calcula os pontos da curva de Hermite entre dois pontos p1 e p2, 
        usando as tangentes t1 e t2, para um número especificado de pontos.
        
        :param num_points: Número de pontos a serem calculados na curva.
        :param p1: Primeiro ponto de controle da curva.
        :param t1: Tangente no primeiro ponto.
        :param p2: Segundo ponto de controle da curva.
        :param t2: Tangente no segundo ponto.
        :return: Coordenadas x e y dos pontos da curva.
        """
        # Gera um vetor de valores t de 0 a 1 com num_points elementos
        t = np.linspace(0, 1, num_points)
        
        # Calcula os coeficientes da base de Hermite
        h00 = 2 * t**3 - 3 * t**2 + 1
        h01 = -2 * t**3 + 3 * t**2
        h10 = t**3 - 2 * t**2 + t
        h11 = t**3 - t**2

        # Calcula as coordenadas x e y da curva usando os coeficientes e os pontos/tangentes
        x = h00 * p1.x + h01 * p2.x + h10 * t1.x + h11 * t2.x
        y = h00 * p1.y + h01 * p2.y + h10 * t1.y + h11 * t2.y

        return x, y

    def normalize_coordinates(self, x, y):
        """
        Normaliza as coordenadas x e y para o intervalo [-1, 1].
        
        :param x: Coordenadas x a serem normalizadas.
        :param y: Coordenadas y a serem normalizadas.
        :return: Coordenadas normalizadas x e y.
        """
        x_min, x_max = np.min(x), np.max(x)
        y_min, y_max = np.min(y), np.max(y)
        
        # Calcula o intervalo para x e y
        x_range = x_max - x_min
        y_range = y_max - y_min

        # Evita divisão por zero, no caso de intervalo zero
        x_range = x_range if x_range != 0 else 1
        y_range = y_range if y_range != 0 else 1

        # Normaliza para o intervalo [-1, 1]
        x = 2 * (x - x_min) / x_range - 1
        y = 2 * (y - y_min) / y_range - 1

        return x, y

    def scale_to_resolution(self, x, y, resolution):
        """
        Escalona as coordenadas normalizadas para uma resolução específica.
        
        :param x: Coordenadas x normalizadas.
        :param y: Coordenadas y normalizadas.
        :param resolution: Resolução da imagem (largura, altura).
        :return: Coordenadas x e y escalonadas para a resolução.
        """
        width, height = resolution
        # Converte as coordenadas normalizadas para coordenadas de pixel
        x = (x + 1) / 2 * width
        y = (y + 1) / 2 * height
        return x, y

    def rasterize_line(self, x1, y1, x2, y2):
        """
        Rasteriza uma linha entre os pontos (x1, y1) e (x2, y2) usando o algoritmo de Bresenham.
        
        :param x1: Coordenada x do ponto inicial.
        :param y1: Coordenada y do ponto inicial.
        :param x2: Coordenada x do ponto final.
        :param y2: Coordenada y do ponto final.
        :return: Lista de pontos da linha rasterizada.
        """
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

    def normalize_tangents(self):
        """
        Normaliza as tangentes para o intervalo [-1, 1].
        
        :return: Lista de tangentes normalizadas como objetos Point.
        """
        # Converte as tangentes para um array numpy para operações vetorizadas
        tangents = np.array([(t.x, t.y) for t in self.tangents])
        x_min, x_max = np.min(tangents[:, 0]), np.max(tangents[:, 0])
        y_min, y_max = np.min(tangents[:, 1]), np.max(tangents[:, 1])

        x_range = x_max - x_min
        y_range = y_max - y_min

        # Evita divisão por zero, no caso de intervalo zero
        x_range = x_range if x_range != 0 else 1
        y_range = y_range if y_range != 0 else 1

        # Normaliza para o intervalo [-1, 1]
        tangents[:, 0] = 2 * (tangents[:, 0] - x_min) / x_range - 1
        tangents[:, 1] = 2 * (tangents[:, 1] - y_min) / y_range - 1

        # Cria uma lista de objetos Point com as tangentes normalizadas
        return [Point(x, y) for x, y in tangents]

    def plot_curve(self, num_segments, resolution, ax1):
        """
        Plota a curva de Hermite em uma imagem rasterizada usando matplotlib.
        
        :param num_segments: Número de segmentos de curva para gerar.
        :param resolution: Resolução da imagem (largura, altura).
        :param ax1: Eixo do matplotlib onde a curva será plotada.
        """
        num_points = num_segments * 10 + 1  # Aumentar a densidade dos pontos para melhor visualização

        if len(self.points) < 2:
            print("Número insuficiente de pontos para gerar a curva.")
            return

        # Normaliza as tangentes antes de calcular a curva
        tangents_normalized = self.normalize_tangents()

        # Cria uma imagem em branco para rasterizar a curva
        width, height = resolution
        combined_image = np.zeros((height, width), dtype=np.uint8)

        for i in range(len(self.points) - 1):
            # Calcula a curva de Hermite entre cada par de pontos
            x, y = self.compute_curve(num_points, self.points[i], tangents_normalized[i], self.points[i + 1], tangents_normalized[i + 1])
            x, y = self.normalize_coordinates(x, y)  # Normaliza as coordenadas
            x, y = self.scale_to_resolution(x, y, resolution)  # Escalona para a resolução da imagem

            for j in range(len(x) - 1):
                # Rasteriza cada segmento da curva
                segment_points = self.rasterize_line(x[j], y[j], x[j + 1], y[j + 1])
                for px, py in segment_points:
                    if 0 <= int(round(py)) < height and 0 <= int(round(px)) < width:
                        # Marca o ponto na imagem
                        combined_image[int(round(py)), int(round(px))] = 1

        # Exibe a imagem rasterizada usando matplotlib
        ax1.clear()
        ax1.imshow(combined_image, cmap='gray', origin='lower')
        ax1.set_title("Rasterized Image")
        ax1.set_xlim(0, width)
        ax1.set_ylim(0, height)
        ax1.set_aspect('equal', adjustable='box')
        ax1.grid(True)
