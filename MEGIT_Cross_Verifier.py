import sys
from PyQt5 import QtWidgets
from megit.gui.app_chkres import MainLoader

app = QtWidgets.QApplication(sys.argv)
window = MainLoader()
window.show()
app.exec_()
