import sys
from PyQt5.QtWidgets import *
from FiltersUI import *
class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Filters()
        self.ui.setupUi(self)
        self.ui.dilatationButton.clicked.connect(self.dispmessage)
        self.show()
    def dispmessage(self):
        self.ui.filtersLabel.setText("Hello "
        +self.ui.filtersLabel.text())
def main():
    app = QApplication([])
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
main()

