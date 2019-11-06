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
        self.show()

    def OpenFileNameDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            'c:\\', "Image files (*.jpg *.gif *.png)")

        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.FileType)
        dlg.setFilter("Image files (*.jpg *.gif *.png)")
      #  filenames = QStringList()

      #  if dlg.exec_():
       #     filenames = dlg.selectedFiles()
def main():
    app = QApplication([])
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
main()

