import sys
import random

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.clicked = False
        self.setWindowTitle('Git и желтые окружности')
        self.pushButton.clicked.connect(self.make_circle)
        self.x, self.y = None, None
        self.circle_size = 0
        self.color = QColor(255, 255, 0)

    def make_circle(self):
        self.circle_size = random.randint(50, 150)
        # self.color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.clicked = True
        self.update()

    def paintEvent(self, event):
        if self.clicked:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(self.color)
            qp.setBrush(self.color)
            qp.drawEllipse(random.randint(100, 500), random.randint(100, 500), self.circle_size, self.circle_size)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
