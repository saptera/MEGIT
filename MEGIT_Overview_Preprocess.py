import sys
from PyQt5 import QtWidgets
from megit.gui.app_preproc_over import MainLoader

app = QtWidgets.QApplication(sys.argv)
window = MainLoader()
window.show()
app.exec_()