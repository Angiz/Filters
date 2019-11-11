# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Filters-untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Filters(object):
    def setupUi(self, Filters):
        Filters.setObjectName("Filters")
        Filters.resize(800, 600)
        Filters.setMaximumSize(QtCore.QSize(16777215, 1677721))
        self.centralwidget = QtWidgets.QWidget(Filters)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(600, 20, 160, 551))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.loadButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.loadButton.setObjectName("loadButton")
        self.verticalLayout.addWidget(self.loadButton)
        self.filtersLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.filtersLabel.setMaximumSize(QtCore.QSize(16777215, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.filtersLabel.setFont(font)
        self.filtersLabel.setObjectName("filtersLabel")
        self.verticalLayout.addWidget(self.filtersLabel)
        self.medianButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.medianButton.setObjectName("medianButton")
        self.verticalLayout.addWidget(self.medianButton)
        self.smoothButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.smoothButton.setObjectName("smoothButton")
        self.verticalLayout.addWidget(self.smoothButton)
        self.sobelButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sobelButton.setObjectName("sobelButton")
        self.verticalLayout.addWidget(self.sobelButton)
        self.dilatationButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.dilatationButton.setObjectName("dilatationButton")
        self.verticalLayout.addWidget(self.dilatationButton)
        self.erosionButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.erosionButton.setObjectName("erosionButton")
        self.verticalLayout.addWidget(self.erosionButton)
        self.photoLabel = QtWidgets.QLabel(self.centralwidget)
        self.photoLabel.setGeometry(QtCore.QRect(40, 30, 521, 531))
        self.photoLabel.setText("")
        self.photoLabel.setPixmap(
            QtGui.QPixmap("../../../../../Pictures/42901586_10158454514613084_6388907296117751808_n.jpg"))
        self.photoLabel.setObjectName("photoLabel")
        Filters.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Filters)
        self.statusbar.setObjectName("statusbar")
        Filters.setStatusBar(self.statusbar)

        self.retranslateUi(Filters)
        QtCore.QMetaObject.connectSlotsByName(Filters)

    def retranslateUi(self, Filters):
        _translate = QtCore.QCoreApplication.translate
        Filters.setWindowTitle(_translate("Filters", "Filters"))
        self.loadButton.setText(_translate("Filters", "Load Picture..."))
        self.filtersLabel.setText(_translate("Filters", "Filters:"))
        self.medianButton.setText(_translate("Filters", "Median"))
        self.smoothButton.setText(_translate("Filters", "Smooth"))
        self.sobelButton.setText(_translate("Filters", "Sobel"))
        self.dilatationButton.setText(_translate("Filters", "Dilatation"))
        self.erosionButton.setText(_translate("Filters", "Erosion"))
