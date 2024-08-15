import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from src.Lines import plot_normalized_lines, plot_rasterized_image

class LineDrawerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interface de Rasterização de Segmentos de Reta")
        
        self.figure, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=(12, 6))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        self.segments = []
        
        self.create_widgets()
        self.update_plots()

    def create_widgets(self):
        self.control_frame = ttk.Frame(self.root)
        self.control_frame.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.x0_entry = ttk.Entry(self.control_frame, width=5)
        self.x0_entry.grid(row=0, column=1)
        self.y0_entry = ttk.Entry(self.control_frame, width=5)
        self.y0_entry.grid(row=0, column=2)
        self.x1_entry = ttk.Entry(self.control_frame, width=5)
        self.x1_entry.grid(row=1, column=1)
        self.y1_entry = ttk.Entry(self.control_frame, width=5)
        self.y1_entry.grid(row=1, column=2)
        
        ttk.Label(self.control_frame, text="x0:").grid(row=0, column=0)
        ttk.Label(self.control_frame, text="x1:").grid(row=1, column=0)
        ttk.Label(self.control_frame, text=":y0").grid(row=0, column=3)
        ttk.Label(self.control_frame, text=":y1").grid(row=1, column=3)
        
        self.add_button = ttk.Button(self.control_frame, text="Adicionar Segmento", command=self.add_segment)
        self.add_button.grid(row=2, column=0, columnspan=4, pady=5)
        
        self.clear_button = ttk.Button(self.control_frame, text="Limpar Segmentos", command=self.clear_segments)
        self.clear_button.grid(row=3, column=0, columnspan=4, pady=5)
        
    def add_segment(self):
        try:
            x0 = float(self.x0_entry.get())
            y0 = float(self.y0_entry.get())
            x1 = float(self.x1_entry.get())
            y1 = float(self.y1_entry.get())
            self.segments.append(((x0, y0), (x1, y1)))
            self.update_plots()
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")

    def clear_segments(self):
        self.segments = []
        self.update_plots()

    def update_plots(self):
        plot_normalized_lines(self.segments, self.ax1)
        plot_rasterized_image(self.segments, 100, 100, self.ax2)
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = LineDrawerApp(root)
    root.mainloop()
