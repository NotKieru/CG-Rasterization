import numpy as np
import matplotlib.pyplot as plt

class FiguraR2:
    def __init__(self):
        self.listaPontos = []

    def addPonto(self, x, y):
        if [x, y] not in self.listaPontos:
            self.listaPontos.append([x, y])
        else:
            print(f"O ponto [{x},{y}] já existe na figura.")

    @staticmethod
    def normalizaPontos(pontos):
        pontosNormalizados = []
        for i in pontos:
            x = 2 * i[0] - 1  # Normalização de 0 a resolucao[0] para -1 a 1
            y = 2 * i[1] - 1  # Normalização de 0 a resolucao[1] para -1 a 1
            pontosNormalizados.append([x, y])
        return pontosNormalizados

    @staticmethod
    def convertePontos(pontos, resolucao):
        pontosConvertidos = []
        for i in pontos:
            x = int((resolucao[0] * (i[0] + 1)) / 2)
            y = int((resolucao[1] * (i[1] + 1)) / 2)
            # Garantir que os pontos estejam dentro dos limites da imagem
            x = min(max(x, 0), resolucao[0] - 1)
            y = min(max(y, 0), resolucao[1] - 1)
            pontosConvertidos.append([x, y])
        return pontosConvertidos

    @staticmethod
    def addPonto(x, y, lista, resolucao):
        x_, y_ = FiguraR2.produzFrag(x, y)
        x_ = int(min(max(x_, 0), resolucao[0] - 1))
        y_ = int(min(max(y_, 0), resolucao[1] - 1))
        if [x_, y_] not in lista:
            lista.append([x_, y_])
        return lista

    @staticmethod
    def produzFrag(x, y):
        xm = int(x)
        ym = int(y)
        xp = xm + 0.5
        yp = ym + 0.5
        return xp, yp

    @staticmethod
    def rasterizacaoRetas(p1o, p2o, resolucao, passo=1):
        p1, p2 = FiguraR2.convertePontos([p1o, p2o], resolucao)
        listaPontos = []
        x1, y1 = p1
        x2, y2 = p2
        dx = x2 - x1
        dy = y2 - y1

        if dx == 0:
            if dy > 0:
                while y1 <= y2:
                    listaPontos = FiguraR2.addPonto(x1, y1, listaPontos, resolucao)
                    y1 += passo
            else:
                while y1 >= y2:
                    listaPontos = FiguraR2.addPonto(x1, y1, listaPontos, resolucao)
                    y1 -= passo
            return listaPontos

        m = dy / dx
        b = y1 - m * x1

        if abs(dx) > abs(dy):
            if dx > 0:
                while x1 <= x2:
                    y1 = m * x1 + b
                    listaPontos = FiguraR2.addPonto(x1, y1, listaPontos, resolucao)
                    x1 += passo
            else:
                while x1 >= x2:
                    y1 = m * x1 + b
                    listaPontos = FiguraR2.addPonto(x1, y1, listaPontos, resolucao)
                    x1 -= passo
        else:
            if dy > 0:
                while y1 <= y2:
                    x1 = (y1 - b) / m
                    listaPontos = FiguraR2.addPonto(x1, y1, listaPontos, resolucao)
                    y1 += passo
            else:
                while y1 >= y2:
                    x1 = (y1 - b) / m
                    listaPontos = FiguraR2.addPonto(x1, y1, listaPontos, resolucao)
                    y1 -= passo

        return listaPontos

    def plotar_reta(self, p1, p2, resolucao):
        # Normaliza os pontos para o intervalo [-1, 1]
        p1_normalizado = FiguraR2.normalizaPontos([p1])[0]
        p2_normalizado = FiguraR2.normalizaPontos([p2])[0]

        # Converte os pontos normalizados para o sistema de coordenadas da imagem
        p1_convertido, p2_convertido = FiguraR2.convertePontos([p1_normalizado, p2_normalizado], resolucao)
        
        # Rasteriza a linha entre os dois pontos
        pontos_rasterizados = FiguraR2.rasterizacaoRetas(p1_normalizado, p2_normalizado, resolucao)
        
        # Se não houver pontos rasterizados, nada para plotar
        if not pontos_rasterizados:
            print("Nenhum ponto foi rasterizado.")
            return
        
        # Cria a figura para o plot
        plt.figure(figsize=(resolucao[0] / 100, resolucao[1] / 100), dpi=100)
        plt.title("Plotagem de Reta")
        plt.xlim(0, resolucao[0])
        plt.ylim(0, resolucao[1])
        plt.gca().set_aspect('equal', adjustable='box')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)

        # Adiciona os pontos rasterizados ao gráfico
        px, py = zip(*pontos_rasterizados)
        plt.plot(px, py, 'k-', markersize=2, label='Reta Rasterizada')

        # Adiciona os pontos finais
        plt.plot([p1_convertido[0], p2_convertido[0]], [p1_convertido[1], p2_convertido[1]], 'ro', markersize=8, label='Pontos Finais')

        # Adiciona uma legenda
        plt.legend()
        
        # Exibe o gráfico
        plt.show()

# Exemplo de uso
if __name__ == "__main__":
    figura = FiguraR2()
    p1 = [0, 0]
    p2 = [10, 10]
    resolucao = (800, 600)  # Resolução da imagem

    figura.plotar_reta(p1, p2, resolucao)
