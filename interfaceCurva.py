import tkinter as tk
from tkinter import ttk, messagebox
from src.hermiteCurve import Ponto, CurvaHermite

class Interface:
    def __init__(self, root):
        self.root = root
        self.root.title("Curva de Hermite")

        self.pontos_entries = []
        self.tangentes_entries = []

        self.create_widgets()

    def create_widgets(self):
        # Layout de entrada para pontos e tangentes
        self.ponto_frame = tk.LabelFrame(self.root, text="Pontos e Tangentes", padx=10, pady=10)
        self.ponto_frame.grid(row=0, column=0, padx=10, pady=10)

        # Adicionar entradas iniciais
        self.add_entry_row()

        tk.Button(self.root, text="Adicionar Ponto/Tangente", command=self.add_entry_row).grid(row=1, column=0, pady=5)

        # Resolução
        tk.Label(self.root, text="Resolução").grid(row=2, column=0, padx=10, pady=5)
        self.resolution_var = tk.StringVar(value="800x600")
        resolutions = ["100x100", "300x300", "800x600", "1920x1080"]
        resolution_menu = ttk.Combobox(self.root, textvariable=self.resolution_var, values=resolutions)
        resolution_menu.grid(row=2, column=1, padx=5, pady=5)

        # Botão de Plotar
        tk.Button(self.root, text="Plotar Curva", command=self.plotar_curva).grid(row=3, column=0, columnspan=2, pady=10)

    def add_entry_row(self):
        row_count = len(self.pontos_entries)
        
        # Adicionar linha para pontos
        x_entry = tk.Entry(self.ponto_frame, width=10)
        y_entry = tk.Entry(self.ponto_frame, width=10)
        tk.Label(self.ponto_frame, text=f"Ponto {row_count + 1} (x, y)").grid(row=row_count, column=0, padx=5, pady=5)
        x_entry.grid(row=row_count, column=1, padx=5, pady=5)
        y_entry.grid(row=row_count, column=2, padx=5, pady=5)
        self.pontos_entries.append((x_entry, y_entry))

        # Adicionar linha para tangentes
        x_entry_t = tk.Entry(self.ponto_frame, width=10)
        y_entry_t = tk.Entry(self.ponto_frame, width=10)
        tk.Label(self.ponto_frame, text=f"Tangente {row_count + 1} (x, y)").grid(row=row_count, column=3, padx=5, pady=5)
        x_entry_t.grid(row=row_count, column=4, padx=5, pady=5)
        y_entry_t.grid(row=row_count, column=5, padx=5, pady=5)
        self.tangentes_entries.append((x_entry_t, y_entry_t))

    def validar_entrada(self):
        pontos = []
        tangentes = []

        try:
            for (x_entry, y_entry) in self.pontos_entries:
                x = x_entry.get().strip()
                y = y_entry.get().strip()
                if x and y:
                    pontos.append(Ponto(float(x), float(y)))

            for (x_entry, y_entry) in self.tangentes_entries:
                x = x_entry.get().strip()
                y = y_entry.get().strip()
                if x and y:
                    tangentes.append(Ponto(float(x), float(y)))

            if len(pontos) < 3:
                raise ValueError("Você deve inserir pelo menos 3 pontos")

            return pontos, tangentes
        except ValueError as e:
            messagebox.showerror("Erro", f"Dados inválidos: {e}")
            return None, None

    def plotar_curva(self):
        pontos, tangentes = self.validar_entrada()
        if pontos is None or tangentes is None:
            return

        try:
            resolution_str = self.resolution_var.get()
            resolution = tuple(map(int, resolution_str.split("x")))

            curva = CurvaHermite(pontos, tangentes)
            curva.plotar_curva(num_segments=10, resolution=resolution)
        except ValueError as e:
            messagebox.showerror("Erro", f"Dados inválidos: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Interface(root)
    root.mainloop()
