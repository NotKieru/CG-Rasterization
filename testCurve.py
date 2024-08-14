import numpy as np
import matplotlib.pyplot as plt
from tkinter.simpledialog import askstring
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
def calculator_difference(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return dx, dy
def calculator_mb(p1, dx, dy):
    m = None if dx == 0 else dy / dx
    b = None if m is None else p1[1] - m * p1[0]
    return m, b

def calculator_x_points(p1, p2, m, b):
    x1, y1 = p1
    x2, y2 = p2
    points = []

    if x1 > x2:
        x1, x2 = x2, x1
    while x1 <= x2:
        y = m * x1 + b if m is not None else y1
        points.append((x1, round(y)))
        x1 += 1

    return points

def calculator_y_points(p1, p2, m, b):
    x1, y1 = p1
    x2, y2 = p2
    points = []
    if y1 > y2:
        y1, y2 = y2, y1
    while y1 <= y2:
        x = (y1 - b) / m if m is not None else x1
        points.append((round(x), y1))
        y1 += 1

    return points

def mid_point(p1, p2):
    p1, p2 = p1, p2
    if p1[0] > p2[0] or p1[1] > p2[1]:
        p1, p2 = p2, p1

    dx, dy = calculator_difference(p1, p2)
    m, b = calculator_mb(p1, dx, dy)

    points = []

    if abs(dx) >= abs(dy):
        points += calculator_x_points(p1, p2, m, b)
    else:
        points += calculator_y_points(p1, p2, m, b)

    return points

def curvaHermite(P0, T0, P1, T1, numeroDePontos):
    pontos = []

    for t in np.linspace(0, 1, numeroDePontos):
        H1 = 2*t*3 - 3*t*2 + 1 # P0
        H2 = t*3 - 2*t*2 + t # T0
        H3 = -2*t*3 + 3*t*2 # P1
        H4 = t*3 - t*2 # T1

        x = H1 * P0[0] + H2 * T0[0] + H3 * P1[0] + H4 * T1[0]
        y = H1 * P0[1] + H2 * T0[1] + H3 * P1[1] + H4 * T1[1]
        x_round = round(x)
        y_round = round(y)
        pontos.append((x_round, y_round))

    return pontos

def plot_points(points, size_view, window):
  img = np.ones((size_view, size_view))
  for i in points:
    img[i[0]][i[1]] = 0

  plt.clf()
  fig, ax = plt.subplots(figsize=(8, 8))
  ax.imshow(img, cmap='gray', origin='lower', vmin=0, vmax=1)

  if not hasattr(window, 'canvas'):
      window.canvas = FigureCanvasTkAgg(fig, master=window)
      window.canvas.get_tk_widget().pack()
  else:
      window.canvas.figure = fig
      window.canvas.draw()


def nossa(window):
    #p1 = (int(x1_entry.get()), int(y1_entry.get()))
    #p2 = (int(x2_entry.get()), int(y2_entry.get()))


    points = curvaHermite((20,20),(40,40), (20,20), (-40,40), 20)

    plot_points(points, 50, window)
def view():
    window = Tk()
    window.title('Trabalho de CG')
    window.geometry("800x600")

    # Frame para o botão
    control_frame = Frame(window)
    control_frame.pack(side=RIGHT, fill=Y, padx=10, pady=10)

    x1_point = Label(control_frame,text='Ponto 1 - X')
    x1_point.pack(pady=5)
    global x1_entry
    x1_entry = Entry(control_frame)
    x1_entry.pack(pady=5)

    y1_point = Label(control_frame,text='Ponto 1 - Y')
    y1_point.pack(pady=5)
    global y1_entry
    y1_entry = Entry(control_frame)
    y1_entry.pack(pady=5)

    x2_point = Label(control_frame,text='Ponto 2 - Y')
    x2_point.pack(pady=5)
    global x2_entry
    x2_entry = Entry(control_frame)
    x2_entry.pack(pady=5)

    y2_point = Label(control_frame,text='Ponto 2 - Y')
    y2_point.pack(pady=5)
    global y2_entry
    y2_entry = Entry(control_frame)
    y2_entry.pack(pady=5)

    # Botão para plotar o gráfico
    plot_button = Button(master=control_frame, command=lambda: nossa(window),
                            height=2, width=10, text="Plot")
    plot_button.pack(pady=20)

    window.mainloop()

view()