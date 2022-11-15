import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class Circles(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.btn.clicked.connect(self.draw)
        self.flag = False

    def draw(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            from random import randint
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(255, 255, 0))
            r = randint(5, self.width() // 3)
            crds = randint(r, self.width() - r), randint(r, self.height() - r)
            qp.drawEllipse(*crds, r, r)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec_())
