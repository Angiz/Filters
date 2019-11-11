import sys
from PyQt5.QtWidgets import *
from FiltersUI import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image, ImageFilter


class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Filters()
        self.ui.setupUi(self)
        self.ui.loadButton.clicked.connect(self.OpenFileNameDialog)
        self.ui.medianButton.clicked.connect(self.MedianFilter)

        self.show()


    def OpenFileNameDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            'Obrazy', "Image files (*.jpg *.gif *.png)")

        pixmap = QPixmap(fname[0])
        h = self.ui.photoLabel.height()
        w = self.ui.photoLabel.width()
        self.ui.photoLabel.setPixmap(QPixmap(pixmap).scaled(w, h, Qt.KeepAspectRatio))

    def MedianFilter(self):
        new_image = cv2.medianBlur(self.pixmap)
        plt.figure((11, 6))
        plt.subplot(121), plt.imshow(cv2.cvtColor(self.pixmap, cv2.COLOR_HSV2RGB)), plt.title('Original')
        plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_HSV2RGB)), plt.title('Median Filter')
        plt.xticks([]), plt.yticks([])
        plt.show()

def main():
    app = QApplication([])
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
main()

