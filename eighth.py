"""This program deals with Custom Contex Menus with 2 approaches."""


import sys

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Signal Based Approach
        # Don't use default right-click context menu, use my custom menu instead.
        # self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        # connects signal to slot
        # self.customContextMenuRequested.connect(self.on_context_menu)


    def contextMenuEvent(self, e):
        # When right mouse button is clicked on a window, Qt.ContextMenuEvent signal is raised.
        # when that signal is triggered, .contextMenuEvent() is called
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))

        # e.globalPos() returns mouse position in window as QPoint integer
        # context.exec() starts QMenu's event loop
        # Therefore, context menu is generated with actions at the mouse right-click position
        context.exec(e.globalPos())


    # def on_context_menu(self, pos):
    #     context = QMenu(self)
    #     context.addAction(QAction("test 1", self))
    #     context.addAction(QAction("test 2", self))
    #     context.addAction(QAction("test 3", self))
    #       self.mapToGlobal() takes widget-relative position and returns global screen position
    #     context.exec(self.mapToGlobal(pos))




app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()