# To show that all widgets can act as a window, not very useful but
# it shows a way to create UI that only has single controls.


# Window with a single pushable button.
# import sys
# from PyQt6.QtWidgets import QApplication, QPushButton
#
# app = QApplication(sys.argv)
#
# window = QPushButton("Push Me")
# window.show()
#
# app.exec()


# QMainWindow, is a pre-made widget which provides standard window features.
# toolbars, menus, statusbar, dockable widgets, etc.
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)

window = QMainWindow()
window.show()

app.exec()