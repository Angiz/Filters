import sys
from PyQt5.QtWidgets import *
from FiltersUI import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Filters()
        self.ui.setupUi(self)
        self.ui.loadButton.clicked.connect(self.OpenFileNameDialog)
        label = QLabel(self)
        label.setGeometry(20, 20, 540, 540)

        pixmap = QPixmap("image.jpg")
        label.setPixmap(QPixmap(pixmap))
        #self.resize(pixmap.width(), pixmap.height())


        self.show()


    def OpenFileNameDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            'Obrazy', "Image files (*.jpg *.gif *.png)")

        if fname[0]:
           # label = QLabel(self)
            #label.setGeometry(20, 20, 540, 540)

            pixmap = QPixmap(fname[0])

           ## self.label.setPixmap(QPixmap(pixmap))



def main():
    app = QApplication([])
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
main()

