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

        def nothing(x):
            pass

        src = cv2.imread(fname[0])
        cv2.namedWindow("Median")
        cv2.createTrackbar("Kernel", "Median", 0, 7, nothing)
        img2 = cv2.medianBlur(src, 1)

        while (1):
            cv2.imshow("Median", img2)
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break
            kernel = (int)(cv2.getTrackbarPos("Kernel", "Median"))
            if kernel==0 or kernel==2 or kernel==4 or kernel==6:
                kernel=kernel+1
            img2[:] = [kernel]
            img2 = cv2.medianBlur(src, kernel)

        cv2.destroyAllWindows()


    def ErosionFilter(self):

        def nothing(x):
            pass

        src = cv2.imread(fname[0])
        cv2.namedWindow("Erosion")
        cv2.createTrackbar("Kernel", "Erosion", 0, 7, nothing)
        kernel = np.ones((5, 5), np.uint8)
        img_erosion = cv2.erode(src, kernel, 1)
        while 1:
            cv2.imshow("Erosion", img_erosion)
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break
            ker = (int)(cv2.getTrackbarPos("Kernel", "Erosion"))
            if ker == 0 or ker == 2 or ker == 4 or ker == 6:
                ker = ker + 1
            img_erosion[:] = [ker]
            kernel = np.ones((ker, ker), np.uint8)
            img_erosion = cv2.erode(src, kernel, 1)

        cv2.destroyAllWindows()

    def DilationFilter(self):

        def nothing(x):
            pass

        src = cv2.imread(fname[0])
        cv2.namedWindow("Dilation")
        cv2.createTrackbar("Kernel", "Dilation", 0, 7, nothing)
        kernel = np.ones((5, 5), np.uint8)
        img_dilation = cv2.dilate(src, kernel, 1)

        while (1):
            cv2.imshow("Dilation", img_dilation)
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break
            ker = (int)(cv2.getTrackbarPos("Kernel", "Dilation"))
            if ker==0 or ker==2 or ker==4 or ker==6:
                ker=ker+1
            img_dilation[:] = [ker]
            kernel = np.ones((ker, ker), np.uint8)
            img_dilation = cv2.dilate(src, kernel, 1)

        cv2.destroyAllWindows()


    def SmoothingFilter(self):

        def nothing(x):
            pass

        src = cv2.imread(fname[0])
        cv2.namedWindow("Smoothing")
        cv2.createTrackbar("Kernel", "Smoothing", 0, 7, nothing)
        blur = cv2.blur(src, (1,1))

        while (1):
            cv2.imshow("Smoothing", blur)
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break
            kernel = (int)(cv2.getTrackbarPos("Kernel", "Smoothing"))
            if kernel==0 or kernel==2 or kernel==4 or kernel==6:
                kernel=kernel+1
            blur[:] = [kernel]
            blur = cv2.blur(src, (kernel, kernel))

        cv2.destroyAllWindows()

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

