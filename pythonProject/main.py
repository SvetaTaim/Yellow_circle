import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class YellowCircle(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.active = False
        self.pushButton.clicked.connect(self.run)

    def paintEvent(self, event):
        if self.active:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def run(self):
        self.active = True
        self.update()

    def draw(self, qp):
        kolvo = random.randrange(1, 10, 1)
        for i in range(kolvo):
            x = random.randrange(0, 590, 1)
            y = random.randrange(0, 500, 1)
            r = random.randrange(1, 100, 1)
            qp.setBrush(QColor('yellow'))
            qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowCircle()
    ex.show()
    sys.exit(app.exec())
