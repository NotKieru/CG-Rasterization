# Trabalho 1 – 1ª Etapa de Computação Gráfica

Instituto Federal do Ceará - Campus Fortaleza  
Departamento de Telemática  
Curso: Engenharia da Computação  
Disciplina: Computação Gráfica  

## Objetivo

Este repositório contém a implementação de algoritmos de rasterização para retas, polígonos convexos e curvas de Hermite, conforme descrito na disciplina de Computação Gráfica 2024.1. Os métodos implementados são baseados no livro *Computação Gráfica: Teoria e Prática* de Eduardo Azevedo e Aura Consi.

### Rasterização de Retas

Implementei o algoritmo de rasterização de retas para um modelo (segmento de reta) no \(\mathbb{R}^2\) para uma imagem. As diretrizes estão na subseção 5.2.1 do livro mencionado. O algoritmo de Bresenham não foi utilizado.

### Rasterização de Polígonos Convexos

Implementei o algoritmo de rasterização de polígonos convexos descrito na subseção 5.2.2 do livro, que utiliza o algoritmo de rasterização de retas.

### Curvas de Hermite

Implementei as curvas de Hermite conforme descrito na subseção 3.1.6 do livro e discutido em sala de aula.


### Rasterização de Retas

- Obtenha imagens da rasterização de pelo menos 5 segmentos de retas diferentes para pelo menos 4 resoluções diferentes.
- Implemente para situações onde \(|\Delta x| > |\Delta y|\) e \(|\Delta y| > |\Delta x|\).
- Considere situações em que as semirretas crescem (\(m > 0\)) ou decrescem (\(m < 0\)).
- Avalie e ajuste o algoritmo para retas verticais e horizontais, incluindo pelo menos um segmento vertical e um horizontal.

### Rasterização de Curvas de Hermite

- Obtenha imagens da rasterização de pelo menos 5 curvas de Hermite diferentes.
- Gere pelo menos uma curva com \(P_1\) e \(P_2\) iguais.
- Crie curvas com pelo menos 3 quantidades de pontos diferentes, baseados em valores regularmente espaçados para o parâmetro \(t\). Conecte-os em segmentos de reta para descrever a curva e realize a rasterização dessas curvas. Mostre a dependência da qualidade da curva em relação à quantidade de segmentos de reta usados.

### Rasterização de Polígonos

- Obtenha imagens da rasterização de pelo menos 6 polígonos (triângulos equiláteros, quadrados e hexágonos, 2 para cada) para pelo menos 4 resoluções diferentes.

### Considerações Gerais

- Os elementos (segmentos de reta, curvas de Hermite e polígonos) são definidos no contínuo em um espaço normalizado bidimensional com componentes \((x_1\) e \(x_2)\) no intervalo \([-1, +1]\) e convertidos para as resoluções 100 x 100, 300 x 300, 800 x 600 e 1920 x 1080.
- Compare os elementos gerados em termos de qualidade para as diversas resoluções e número de pontos, no caso das curvas de Hermite.
- Avalie a implementação com mais de um elemento (inclusive de tipos diferentes) no espaço normalizado.
- Crie uma interface gráfica para mostrar os elementos no espaço normalizado e as imagens geradas. A interface deve permitir ao usuário definir/criar os elementos a serem colocados no espaço normalizado.

## Bibliotecas Utilizadas

### Tkinter

Biblioteca padrão para a criação de interfaces gráficas em Python. É utilizada para criar a interface gráfica dos aplicativos, incluindo botões, menus e campos de entrada.

### Matplotlib

Biblioteca para a criação de gráficos em Python. Utilizada para desenhar as curvas de Hermite e os polígonos. `FigureCanvasTkAgg` é um adaptador para integrar gráficos Matplotlib com a interface Tkinter.

### src.hermiteCurve

Módulo personalizado que contém a classe `Point` e `HermiteCurve`, responsável por calcular e plotar as curvas de Hermite.

### src.Polygons

Módulo personalizado que inclui funções para rasterização de polígonos, como `scanline` e `get_polygon_vertices`.

### src.lines

Módulo personalizado que contém a função de rasterização de linhas, conforme descrito na subseção 5.2.1 do livro. Este módulo é responsável por rasterizar segmentos de reta e lidar com diferentes casos de inclinação e resolução.

1. **Clone o Repositório**

   Clone este repositório para o seu ambiente local usando o comando:

   ```bash
   clone este projeto
   pip install matplotlib
   pip install tkinter
   pip install numpy

   python .\main.py

