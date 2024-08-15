import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from src.Lines import FiguraR2  # Certifique-se de que o caminho esteja correto

class PlotWindow:
    def __init__(self, master, resolution, p1, p2):
        self.top = tk.Toplevel(master)
        self.top.title("Segmento de Reta")

        self.resolution = resolution
        self.p1 = p1
        self.p2 = p2

        self.create_widgets()

    def create_widgets(self):
        # Criar a imagem
        listaPontos = FiguraR2.rasterizacaoRetas(self.p1, self.p2, self.resolution)
        img = np.ones((self.resolution[1], self.resolution[0]))

        for ponto in listaPontos:
            img[int(ponto[1])][int(ponto[0])] = 0

        fig, ax = plt.subplots(figsize=(self.resolution[0] / 100, self.resolution[1] / 100), dpi=100)
        ax.imshow(img, cmap='gray', origin='lower', vmin=0, vmax=1)
        ax.set_title("Plotagem de Reta")
        ax.set_xlim(0, self.resolution[0])
        ax.set_ylim(0, self.resolution[1])
        ax.set_aspect('equal', adjustable='box')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.grid(True)

        # Adiciona os pontos rasterizados ao gráfico
        px, py = zip(*listaPontos)
        ax.plot(px, py, 'k-', markersize=3, label='Reta Rasterizada')

        # Adiciona os pontos finais
        ax.plot([self.p1[0], self.p2[0]], [self.p1[1], self.p2[1]], 'ro', markersize=8, label='Pontos Finais')

        # Adiciona uma legenda
        ax.legend()

        # Adiciona o gráfico ao canvas da nova janela
        canvas = FigureCanvasTkAgg(fig, master=self.top)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        canvas.draw()

class Interface:
    def __init__(self, root):
        self.root = root
        self.root.title("Segmento de Reta")

        self.create_widgets()

    def create_widgets(self):
        # Layout de entrada para segmento de reta
        self.segmento_frame = tk.LabelFrame(self.root, text="Segmento de Reta", padx=10, pady=10)
        self.segmento_frame.grid(row=0, column=0, padx=10, pady=10)

        tk.Label(self.segmento_frame, text="Ponto 1 (x, y)").grid(row=0, column=0, padx=5, pady=5)
        self.x1_entry = tk.Entry(self.segmento_frame, width=10)
        self.y1_entry = tk.Entry(self.segmento_frame, width=10)
        self.x1_entry.grid(row=0, column=1, padx=5, pady=5)
        self.y1_entry.grid(row=0, column=2, padx=5, pady=5)

        tk.Label(self.segmento_frame, text="Ponto 2 (x, y)").grid(row=1, column=0, padx=5, pady=5)
        self.x2_entry = tk.Entry(self.segmento_frame, width=10)
        self.y2_entry = tk.Entry(self.segmento_frame, width=10)
        self.x2_entry.grid(row=1, column=1, padx=5, pady=5)
        self.y2_entry.grid(row=1, column=2, padx=5, pady=5)

        # Resolução
        tk.Label(self.root, text="Resolução").grid(row=2, column=0, padx=10, pady=5)
        self.resolution_var = tk.StringVar(value="800x600")
        resolutions = ["100x100", "300x300", "800x600", "1920x1080"]
        resolution_menu = ttk.Combobox(self.root, textvariable=self.resolution_var, values=resolutions)
        resolution_menu.grid(row=2, column=1, padx=5, pady=5)

        # Botão de Plotar
        tk.Button(self.root, text="Plotar Segmento", command=self.plotar_segmento).grid(row=3, column=0, columnspan=2, pady=10)

    def validar_entrada(self):
        try:
            x1 = float(self.x1_entry.get().strip())
            y1 = float(self.y1_entry.get().strip())
            x2 = float(self.x2_entry.get().strip())
            y2 = float(self.y2_entry.get().strip())

            return (x1, y1), (x2, y2)
        except ValueError as e:
            messagebox.showerror("Erro", f"Dados inválidos: {e}")
            return None, None

    def plotar_segmento(self):
        p1, p2 = self.validar_entrada()
        if p1 is None or p2 is None:
            return

        try:
            resolution_str = self.resolution_var.get()
            resolution = tuple(map(int, resolution_str.split("x")))

            # Abrir uma nova janela para exibir o gráfico
            PlotWindow(self.root, resolution, p1, p2)
        except ValueError as e:
            messagebox.showerror("Erro", f"Dados inválidos: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Interface(root)
    root.mainloop()
