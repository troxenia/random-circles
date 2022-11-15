import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from UI import Ui_Form


class Circles(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
            color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
            qp.setPen(color)
            r = randint(5, self.width() // 3)
            crds = randint(r, self.width() - r), randint(r, self.height() - r)
            qp.drawEllipse(*crds, r, r)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec_())
