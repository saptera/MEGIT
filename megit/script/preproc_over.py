import sys
import os
sys.path.append(os.getcwd())

from PySide6 import QtWidgets
from megit.gui.app_preproc_over import MainLoader


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainLoader()
    window.show()
    app.exec()
