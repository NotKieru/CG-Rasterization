import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QInputDialog, QMessageBox, QLabel, QLineEdit, QFormLayout

class RasterApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Rasterização')
        self.setGeometry(100, 100, 300, 200)  # Tamanho padrão da janela

        layout = QVBoxLayout()

        # Botões
        self.btn_line = QPushButton('Reta', self)
        self.btn_line.clicked.connect(self.draw_line)
        layout.addWidget(self.btn_line)

        self.btn_polygon = QPushButton('Polígono', self)
        self.btn_polygon.clicked.connect(self.draw_polygon)
        layout.addWidget(self.btn_polygon)

        self.btn_curve = QPushButton('Curva', self)
        self.btn_curve.clicked.connect(self.draw_curve)
        layout.addWidget(self.btn_curve)

        # Área para entrada de pontos e número de segmentos
        self.point_inputs = QFormLayout()
        self.points_label = QLabel("Pontos (x1,y1 x2,y2 ...):")
        self.point_input = QLineEdit()
        self.point_inputs.addRow(self.points_label, self.point_input)

        self.segments_label = QLabel("Número de segmentos:")
        self.segments_input = QLineEdit()
        self.point_inputs.addRow(self.segments_label, self.segments_input)

        self.segment_inputs_area = QWidget()
        self.segment_inputs_area.setLayout(self.point_inputs)
        layout.addWidget(self.segment_inputs_area)

        self.setLayout(layout)
        self.show()

    def select_resolution(self):
        items = ("100x100", "300x300", "800x600", "1920x1080")
        item, ok = QInputDialog.getItem(self, "Selecione a Resolução", "Resolução:", items, 2, False)
        if ok and item:
            return tuple(map(int, item.split('x')))
        return None

    def draw_line(self):
        resolution = self.select_resolution()
        if resolution:
            points_text, ok = QInputDialog.getText(self, 'Entrada de Pontos', 'Digite os pontos (x0,y0 x1,y1):')
            if ok:
                points = list(map(int, points_text.replace(' ', '').replace(',', ' ').split()))
                if len(points) == 4:
                    from src.events import handle_line_event
                    handle_line_event(resolution, *points)
                else:
                    QMessageBox.warning(self, 'Erro', 'Número de pontos inválido. Deve ser 4 (x0, y0, x1, y1).')

    def draw_polygon(self):
        resolution = self.select_resolution()
        if resolution:
            points_text, ok = QInputDialog.getText(self, 'Entrada de Pontos', 'Digite os pontos (x1,y1 x2,y2 ...):')
            if ok:
                points = list(map(int, points_text.replace(' ', '').replace(',', ' ').split()))
                if len(points) % 2 == 0:
                    from src.events import handle_polygon_event
                    handle_polygon_event(resolution, points)
                else:
                    QMessageBox.warning(self, 'Erro', 'Número de pontos inválido. Deve ser par.')

    def draw_curve(self):
        resolution = self.select_resolution()
        if resolution:
            points_text, ok = QInputDialog.getText(self, 'Entrada de Pontos', 'Digite os pontos (x1,y1 x2,y2 ...):')
            if ok:
                points = list(map(int, points_text.replace(' ', '').replace(',', ' ').split()))
                segments_text, ok = QInputDialog.getText(self, 'Número de Segmentos', 'Digite o número de segmentos:')
                if ok:
                    num_segments = int(segments_text)
                    if len(points) % 4 == 0 and num_segments > 0:
                        from src.events import handle_curve_event
                        handle_curve_event(resolution, points, num_segments)
                    else:
                        QMessageBox.warning(self, 'Erro', 'Número de pontos inválido ou número de segmentos inválido.')
                        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RasterApp()
    sys.exit(app.exec_())
