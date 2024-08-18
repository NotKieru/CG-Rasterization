import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from src.hermiteCurve import Point, HermiteCurve

class HermiteCurveApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Curva de Hermite")

        # Configura a figura e os eixos para gráficos
        self.figure, (self.ax1) = plt.subplots(1, figsize=(12, 6))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.point_entries = []
        self.tangent_entries = []

        self.create_widgets()
        self.update_plots()

    def create_widgets(self):
        self.control_frame = ttk.Frame(self.root)
        self.control_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Layout para entrada de pontos e tangentes
        self.point_frame = tk.LabelFrame(self.control_frame, text="Pontos e Tangentes", padx=10, pady=10)
        self.point_frame.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Adiciona entradas iniciais
        self.add_entry_row()

        tk.Button(self.control_frame, text="Adicionar Pontos/Tangentes", command=self.add_entry_row).grid(row=1, column=0, columnspan=4, pady=5)

        # Resolução
        tk.Label(self.control_frame, text="Resolução").grid(row=2, column=0, padx=10, pady=5)
        self.resolution_var = tk.StringVar(value="100x100")
        resolutions = ["100x100", "300x300", "800x600", "1920x1080"]
        resolution_menu = ttk.Combobox(self.control_frame, textvariable=self.resolution_var, values=resolutions)
        resolution_menu.grid(row=2, column=1, padx=5, pady=5)

        # Quantidade de segmentos
        tk.Label(self.control_frame, text="Número de segmentos").grid(row=2, column=2, padx=10, pady=5)
        self.num_segments_var = tk.IntVar(value=5)
        tk.Spinbox(self.control_frame, from_=1, to_=100, textvariable=self.num_segments_var).grid(row=2, column=3, padx=5, pady=5)

        # Botão para plotar a curva
        tk.Button(self.control_frame, text="Plot Curva", command=self.plot_curve).grid(row=3, column=0, columnspan=4, pady=10)

    def add_entry_row(self):
        row_count = len(self.point_entries)

        # Adiciona linha para pontos
        x_entry = tk.Entry(self.point_frame, width=10)
        y_entry = tk.Entry(self.point_frame, width=10)
        tk.Label(self.point_frame, text=f"Ponto {row_count + 1} (x, y)").grid(row=row_count, column=0, padx=5, pady=5)
        x_entry.grid(row=row_count, column=1, padx=5, pady=5)
        y_entry.grid(row=row_count, column=2, padx=5, pady=5)
        self.point_entries.append((x_entry, y_entry))

        # Adiciona linha para tangentes
        x_entry_t = tk.Entry(self.point_frame, width=10)
        y_entry_t = tk.Entry(self.point_frame, width=10)
        tk.Label(self.point_frame, text=f"Tangente {row_count + 1} (x, y)").grid(row=row_count, column=3, padx=5, pady=5)
        x_entry_t.grid(row=row_count, column=4, padx=5, pady=5)
        y_entry_t.grid(row=row_count, column=5, padx=5, pady=5)
        self.tangent_entries.append((x_entry_t, y_entry_t))

    def validate_input(self):
        """
        Valida a entrada dos pontos e tangentes. Verifica se os valores estão no intervalo [-1, 1].
        
        :return: Tuple contendo listas de pontos e tangentes ou (None, None) em caso de erro.
        """
        points = []
        tangents = []

        try:
            for (x_entry, y_entry) in self.point_entries:
                x = x_entry.get().strip()
                y = y_entry.get().strip()
                if x and y:
                    x = float(x)
                    y = float(y)
                    if not (-1 <= x <= 1 and -1 <= y <= 1):
                        raise ValueError("Os valores devem estar no intervalo [-1, 1].")
                    points.append(Point(x, y))

            for (x_entry, y_entry) in self.tangent_entries:
                x = x_entry.get().strip()
                y = y_entry.get().strip()
                if x and y:
                    x = float(x)
                    y = float(y)
                    if not (-1 <= x <= 1 and -1 <= y <= 1):
                        raise ValueError("Os valores devem estar no intervalo [-1, 1].")
                    tangents.append(Point(x, y))

            return points, tangents
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid data: {e}")
            return None, None

    def plot_curve(self):
        """
        Plota a curva de Hermite com base na entrada do usuário.
        """
        points, tangents = self.validate_input()
        if points is None or tangents is None:
            return

        try:
            resolution_str = self.resolution_var.get()
            resolution = tuple(map(int, resolution_str.split("x")))
            num_segments = self.num_segments_var.get()

            curve = HermiteCurve(points, tangents)
            self.ax1.clear()
            curve.plot_curve(num_segments=num_segments, resolution=resolution, ax1=self.ax1)
            self.figure.tight_layout()  # Ajusta o layout da figura
            self.canvas.draw()
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid data: {e}")


    def update_plots(self):
        """
        Atualiza os gráficos na interface.
        """
        self.ax1.clear()
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = HermiteCurveApp(root)
    root.mainloop()
