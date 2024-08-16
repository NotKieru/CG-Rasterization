# poligonos.py
import numpy as np
import matplotlib.pyplot as plt

def create_empty_image(size):
    return np.zeros((size, size), dtype=np.uint8)

def normalize_to_image_coords(normalized_coords, size):
    return ((normalized_coords + 1) / 2 * (size - 1)).astype(int)

def draw_polygon(image, vertices):
    image_coords = normalize_to_image_coords(np.array(vertices), image.shape[0])
    fill_polygon(image, image_coords)

def fill_polygon(image, points):
    matrix = np.zeros_like(image)
    scanline_fill(matrix, points)
    image[np.where(matrix == 1)] = 1

def scanline_fill(matrix, points):
    rows, cols = matrix.shape
    min_x, min_y = np.min(points, axis=0).astype(int)
    max_x, max_y = np.max(points, axis=0).astype(int)
    
    min_x = max(min_x, 0)
    max_x = min(max_x, cols - 1)
    min_y = max(min_y, 0)
    max_y = min(max_y, rows - 1)
    
    for y in range(min_y, max_y + 1):
        intersections = []
        for i in range(len(points)):
            x0, y0 = points[i]
            x1, y1 = points[(i + 1) % len(points)]
            
            if (y0 < y <= y1) or (y1 < y <= y0):
                if y0 != y1:
                    x = int(x0 + (y - y0) * (x1 - x0) / (y1 - y0))
                    intersections.append(x)
        
        intersections.sort()
        for i in range(0, len(intersections), 2):
            x0 = max(min(intersections[i], cols - 1), 0)
            x1 = max(min(intersections[i + 1], cols - 1), 0)
            if x0 < x1:
                matrix[y, x0:x1 + 1] = 1

def show_image(image, title):
    plt.imshow(image, cmap='gray', interpolation='none')
    plt.title(title)
    plt.axis('off')
    plt.show()
