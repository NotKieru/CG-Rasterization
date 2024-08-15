import numpy as np
import matplotlib.pyplot as plt
from src.Lines import raster_line, plot_image
from src.Polygons import combine_matrices, scanline_fill
from src.hermiteCurve import Ponto, CurvaHermite

def handle_line_event(resolution, x0, y0, x1, y1):
    image = raster_line(x0, y0, x1, y1, resolution[0] // 2, resolution[1] // 2)
    plot_image(image, 'Reta', resolution[0] // 2, resolution[1] // 2)

def handle_polygon_event(resolution, points):
    points = [(points[i], points[i + 1]) for i in range(0, len(points), 2)]
    matrices = [raster_line(p1[0], p1[1], p2[0], p2[1], resolution[0] // 2, resolution[1] // 2)
                for p1, p2 in zip(points[:-1], points[1:])]
    combined = combine_matrices(matrices)
    filled_polygon = scanline_fill(combined)
    plot_image(filled_polygon, 'Polígono', resolution[0] // 2, resolution[1] // 2)

def handle_curve_event(resolution, points, num_segments):
    pontos = [Ponto(points[i], points[i + 1]) for i in range(0, len(points), 2)]
    tangentes = [Ponto(0, 0) for _ in pontos]  # Exemplo simples: tangentes nulas
    curva = CurvaHermite(pontos, tangentes)
    curva.plotar_curva(num_segments, resolution)
