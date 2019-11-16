import sys
from PyQt5.QtWidgets import *
from FiltersUI import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image, ImageFilter
from MedianDialog import *

class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Filters()
        self.ui.setupUi(self)
        self.ui.loadButton.clicked.connect(self.OpenFileNameDialog)
        self.ui.medianButton.clicked.connect(self.MedianFilter)
        self.ui.erosionButton.clicked.connect(self.ErosionFilter)
        self.ui.dilatationButton.clicked.connect(self.DilationFilter)
        self.ui.smoothButton.clicked.connect(self.SmoothingFilter)
        self.ui.sobelButton.clicked.connect(self.SobelFilter)


        self.show()

    def OpenFileNameDialog(self):
        global fname
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            'Obrazy', "Image files (*.jpg *.gif *.png)")

        pixmap = QPixmap(fname[0])
        h = self.ui.photoLabel.height()
        w = self.ui.photoLabel.width()
        self.ui.photoLabel.setPixmap(QPixmap(pixmap).scaled(w, h, Qt.KeepAspectRatio))

    def MedianFilter(self):
        #DialogFunc()
        src = cv2.imread(fname[0], 7)
        img2 = cv2.medianBlur(src, 7)
        cv2.imshow("Median", img2)

    def ErosionFilter(self):
        src = cv2.imread(fname[0])
        kernel = np.ones((5, 5), np.uint8)
        img_erosion = cv2.erode(src, kernel, 1)
        cv2.imshow('Erosion', img_erosion)

    def DilationFilter(self):

        def nothing(x):
            pass

        src = cv2.imread(fname[0])
        cv2.namedWindow("Dilation")
        cv2.createTrackbar("Kernel", "Dilation", 1, 7, nothing)
        kernel = np.ones((5, 5), np.uint8)
        img_dilation = cv2.dilate(src, kernel, 1)

        while (1):
            cv2.imshow("Dilation", img_dilation)
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break
            ker1 = cv2.getTrackbarPos("Kernel", "Dilation")
            img_dilation[:] = [ker1]
            kernel = np.ones((ker1, ker1), np.uint8)
            img_dilation = cv2.dilate(src, kernel, 1)

        cv2.destroyAllWindows()

    def SmoothingFilter(self):
        src = cv2.imread(fname[0])
        blur = cv2.blur(src, (5,5))
        cv2.imshow("Smoothing", blur)

    def SobelFilter(self):
        src = cv2.imread(fname[0], 0)
        sobelx64f = cv2.Sobel(src, cv2.CV_64F, 1, 0, 7)
        abs_sobel64f = np.absolute(sobelx64f)
        sobel_8u = np.uint8(abs_sobel64f)
        cv2.imshow("Sobel", sobel_8u)



def main():
    app = QApplication([])
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
main()

