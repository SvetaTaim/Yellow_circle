import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from ui_file import Ui_MainWindow

class YellowCircle(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
            red = random.randrange(0, 255, 1)
            green = random.randrange(0, 255, 1)
            blue = random.randrange(0, 255, 1)
            qp.setBrush(QColor(red, green, blue))
            qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowCircle()
    ex.show()
    sys.exit(app.exec())
