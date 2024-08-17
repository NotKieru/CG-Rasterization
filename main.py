import tkinter as tk
from tkinter import ttk
from interfaceReta import LineDrawerApp  
from interfacePolygons import PolygonDrawerApp  
from interfaceCurva import HermiteCurveApp  

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interface Principal de Rasterização")
        
        # Definindo o tamanho da janela principal
        self.root.geometry("600x400")  # Largura x Altura
        
        # Botão para Rasterização de Retas
        self.line_button = ttk.Button(root, text="Rasterização de Retas", command=self.open_line_drawer, width=30)
        self.line_button.pack(padx=20, pady=20, fill=tk.X)

        # Botão para Rasterização de Polígonos
        self.polygon_button = ttk.Button(root, text="Rasterização de Polígonos", command=self.open_polygon_drawer, width=30)
        self.polygon_button.pack(padx=20, pady=20, fill=tk.X)

        # Botão para Rasterização de Curvas
        self.curve_button = ttk.Button(root, text="Rasterização de Curvas", command=self.open_curve_drawer, width=30)
        self.curve_button.pack(padx=20, pady=20, fill=tk.X)

    def open_line_drawer(self):
        line_window = tk.Toplevel(self.root)
        LineDrawerApp(line_window)

    def open_polygon_drawer(self):
        polygon_window = tk.Toplevel(self.root)
        PolygonDrawerApp(polygon_window)

    def open_curve_drawer(self):
        curve_window = tk.Toplevel(self.root)
        HermiteCurveApp(curve_window)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
