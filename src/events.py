from src.Lines import raster_line, plot_image
from src.Polygons import combine_matrices

def draw_line(resolution, coordinates):
    resolution_width, resolution_height = (
        int(resolution.split("x")[0]), int(resolution.split("x")[1]))

    first_point_coordinates, second_point_coordinates = (
        coordinates[0].split(" "), coordinates[1].split(" "))

    return raster_line(
        x0=int(float(first_point_coordinates[0]) * resolution_width),
        y0=int(float(first_point_coordinates[1]) * resolution_height),
        x1=int(float(second_point_coordinates[0]) * resolution_width),
        y1=int(float(second_point_coordinates[1]) * resolution_height),
        res_width=resolution_width,
        res_height=resolution_height,
    )

def draw_polygon(resolution, coordinates):
    images_list = []
    resolution_width, resolution_height = (
        int(resolution.split("x")[0]), int(resolution.split("x")[1]))

    for index in range(len(coordinates) - 1):
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

    last_index = len(coordinates) - 1
    first_point_coordinates, second_point_coordinates = (
        coordinates[last_index].split(" "), coordinates[0].split(" "))

    images_list.append(raster_line(
        x0=int(float(first_point_coordinates[0]) * resolution_width),
        y0=int(float(first_point_coordinates[1]) * resolution_height),
        x1=int(float(second_point_coordinates[0]) * resolution_width),
        y1=int(float(second_point_coordinates[1]) * resolution_height),
        res_width=resolution_width,
        res_height=resolution_height,
    ))

    return images_list
