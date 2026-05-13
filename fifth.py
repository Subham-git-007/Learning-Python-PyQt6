"""Application that contains a button that changes the window title"""
# To demonstrate how a chain of signals can be fired and understand how to manipulate them.

import sys

from PyQt6.QtWidgets  import QApplication, QMainWindow, QPushButton
from random import choice


window_titles = [
    "My App",
    "My App",
    "Still My App",
    "Still My App",
    "What On Earth",
    "What On Earth",
    "This Is Surprising",
    "This Is Surprising",
    "Something Went Wrong"
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.n_times_clicked = 0

        self.setWindowTitle("My App")

        self.button = QPushButton("CLICK ME!!!")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.windowTitleChanged.connect(self.window_title_changed)

        self.setCentralWidget(self.button)


    def the_button_was_clicked(self):
        print("Clicked.")
        new_window_title = choice(window_titles)
        print(f"Setting title to: {new_window_title}")
        self.setWindowTitle(new_window_title)


    def window_title_changed(self, window_title):
        print(f"Window title changed to: {window_title}")

        if window_title == "Something Went Wrong":
            self.button.setDisabled(True)




app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()