import os
import sys

import qtmodern.styles
import qtmodern.windows
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication

from Modules.Interface.DataClass.UIElement import UIElements
from Modules.Interface.InitializeUI import InitUI


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        UIElements.main_window = self
        InitUI().init_layout()
        print("[INFO] Use console for more information.")


if __name__ == '__main__':
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    basedir = os.path.dirname(__file__)

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(os.path.join(basedir, 'Resources/img/icon.ico')))
    qtmodern.styles.dark(app)

    window = Main()
    window.setWindowTitle("XML Similarity Calculator")

    mw = qtmodern.windows.ModernWindow(window)
    mw.setFixedSize(1280, 720)

    # move to center of screen
    qr = mw.frameGeometry()
    sc = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
    cp = QApplication.desktop().screenGeometry(sc).center()
    qr.moveCenter(cp)
    mw.move(qr.topLeft())

    mw.show()

    sys.exit(app.exec_())
