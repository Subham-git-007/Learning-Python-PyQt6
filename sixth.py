"""
Connecting widgets together directly.
Application that changes the label according to user's input text in the LineEdit.
"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.label = QLabel()
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.input)

        container = QWidget()
        container.setLayout(vbox)

        self.setCentralWidget(container)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()