import sys
import random
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QTableWidget, QPushButton
from PyQt5.QtGui import QColor, QPainter
from PyQt5 import uic


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.f = False
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.f = True
        self.repaint()

    def paintEvent(self, event):
        if self.f:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def draw_flag(self, qp):
        qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        d = random.randint(10, 350)
        qp.drawEllipse(random.randint(0, 300), random.randint(0, 300), d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())