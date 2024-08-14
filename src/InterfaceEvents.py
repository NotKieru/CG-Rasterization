from src.Lines import *


def draw_line(resolution, coordinates):
    # Define a resolução (Largura x Altura)
    resolution_width, resolution_height = (
        int(resolution.split("x")[0]), int(resolution.split("x")[1]))

    # Define os dois únicos pontos da reta.
    first_point_coordinates, second_point_coordinates = (
        coordinates[0].split(" "), coordinates[1].split(" "))

    # Gera a reta baseado na diferença entre os 2 pontos
    return raster_line(
        x0=int(float(first_point_coordinates[0]) * resolution_width),
        y0=int(float(first_point_coordinates[1]) * resolution_height),
        x1=int(float(second_point_coordinates[0]) * resolution_width),
        y1=int(float(second_point_coordinates[1]) * resolution_height),
        res_width=resolution_width,
        res_height=resolution_height,
    )


def draw_polygon(resolution, coordinates):
    # Cria a lista que vai salvar todas as imagens para posteriormente sobrepor as linhas
    images_list = []

    # Tamanho da lista de coordenadas -1 para reutilização:
    decreased_list_size = len(coordinates) - 1

    # Define a resolução (Largura x Altura)
    resolution_width, resolution_height = (
        int(resolution.split("x")[0]), int(resolution.split("x")[1]))

    # Para cada elemento de coordinates, cria a ligação elemento -> próximoElemento.
    for index in range(decreased_list_size):
        first_point_coordinates, second_point_coordinates = (
            coordinates[index].split(" "), coordinates[index + 1].split(" "))

        images_list.append(raster_line(
            x0=int(float(first_point_coordinates[0]) * resolution_width),
            y0=int(float(first_point_coordinates[1]) * resolution_height),
            x1=int(float(second_point_coordinates[0]) * resolution_width),
            y1=int(float(second_point_coordinates[1]) * resolution_height),
            res_width=resolution_width,
            res_height=resolution_height,
        ))

    # Faz a última ligação entre o último ponto e o primeiro ponto para fechar o polígono.
    first_point_coordinates, second_point_coordinates = (
        coordinates[decreased_list_size].split(" "), coordinates[0].split(" "))

    images_list.append(raster_line(
        x0=int(float(first_point_coordinates[0]) * resolution_width),
        y0=int(float(first_point_coordinates[1]) * resolution_height),
        x1=int(float(second_point_coordinates[0]) * resolution_width),
        y1=int(float(second_point_coordinates[1]) * resolution_height),
        res_width=resolution_width,
        res_height=resolution_height,
    ))

    return images_list

def draw_curve(self, resolution, coordenadas):
    print("x")
    # TODO Desenhar curva