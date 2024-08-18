# Project 1 – 1st Stage of Computer Graphics

Instituto Federal do Ceará - Campus Fortaleza    
Course: Computer Engineering  
Subject: Computer Graphics 2024.1

## Objective

This repository contains the implementation of rasterization algorithms for lines, convex polygons, and Hermite curves, as described in the Computer Graphics 2024.1 course. The implemented methods are based on the book *Computer Graphics: Theory and Practice* by Eduardo Azevedo and Aura Consi.

### Line Rasterization

I implemented the line rasterization algorithm for a model (line segment) in \(\mathbb{R}^2\) for an image. The guidelines are in subsection 5.2.1 of the mentioned book. The Bresenham algorithm was not used.

### Convex Polygon Rasterization

I implemented the convex polygon rasterization algorithm described in subsection 5.2.2 of the book, which uses the line rasterization algorithm.

### Hermite Curves

I implemented Hermite curves as described in subsection 3.1.6 of the book and discussed in class.

### Line Rasterization

- Obtain images of the rasterization of at least 5 different line segments for at least 4 different resolutions.
- Implement for situations where \(|\Delta x| > |\Delta y|\) and \(|\Delta y| > |\Delta x|\).
- Consider situations where the rays grow (\(m > 0\)) or decrease (\(m < 0\)).
- Evaluate and adjust the algorithm for vertical and horizontal lines, including at least one vertical and one horizontal segment.

### Hermite Curve Rasterization

- Obtain images of the rasterization of at least 5 different Hermite curves.
- Generate at least one curve with \(P_1\) and \(P_2\) equal.
- Create curves with at least 3 different numbers of points, based on regularly spaced values for the parameter \(t\). Connect them into line segments to describe the curve and rasterize these curves. Show the dependence of curve quality on the number of line segments used.

### Polygon Rasterization

- Obtain images of the rasterization of at least 6 polygons (equilateral triangles, squares, and hexagons, 2 for each) for at least 4 different resolutions.

### General Considerations

- The elements (line segments, Hermite curves, and polygons) are defined in the continuous 2D normalized space with components \((x_1\) and \(x_2)\) in the range \([-1, +1]\) and converted to resolutions of 100 x 100, 300 x 300, 800 x 600, and 1920 x 1080.
- Compare the generated elements in terms of quality for the various resolutions and number of points, in the case of Hermite curves.
- Evaluate the implementation with more than one element (including different types) in the normalized space.
- Create a graphical interface to display the elements in the normalized space and the generated images. The interface should allow the user to define/create the elements to be placed in the normalized space.

## Libraries Used

### Tkinter

Standard library for creating graphical user interfaces in Python. It is used to create the graphical interface of applications, including buttons, menus, and input fields.

### Matplotlib

Library for creating graphs in Python. Used to draw Hermite curves and polygons. `FigureCanvasTkAgg` is an adapter for integrating Matplotlib graphics with the Tkinter interface.

### src.hermiteCurve

Custom module containing the `Point` and `HermiteCurve` classes, responsible for calculating and plotting Hermite curves.

### src.Polygons

Custom module that includes functions for polygon rasterization, such as `scanline` and `get_polygon_vertices`.

### src.lines

Custom module containing the line rasterization function, as described in subsection 5.2.1 of the book. This module is responsible for rasterizing line segments and handling different cases of slope and resolution.

1. **Instructions to Run This Project**

   ```bash
   clone this project
   pip install matplotlib
   pip install tkinter
   pip install numpy

   python .\main.py
