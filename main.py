import sys
import ctypes
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QLabel
from PyQt5.QtGui import QIcon,QPixmap


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 simple window - pythonspot.com'
        self.left = 0
        self.top = 26
        self.width = 0
        self.height = 0
        self.setWindowSize()
        self.initUI()

    def initUI(self):
        #button = QPushButton('PyQt5 button', self)
        #button.setToolTip('This is an example button')
        #button.move(100, 70)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        label = QLabel(self)
        pixmap = QPixmap('tec3.png')
        label.setPixmap(pixmap)
        label.move(self.width/2-pixmap.width()/2,self.height/2-pixmap.height()/2)
        self.show()

    def closeEvent(self, event):
        self.deleteLater()
        event.accept()

    def setWindowSize(self):
        user32 = ctypes.windll.user32
        screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        self.width = screensize[0]
        self.height = screensize[1]-self.top


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
