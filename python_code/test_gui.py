from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 Simple Window'
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        button = QPushButton('Click me!', self)
        button.setToolTip('This is a QPushButton widget')
        button.move(50,50) 
        button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        print('Button clicked!')

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
