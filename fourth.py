# PyQt6 Signals, Slots and Events


import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)

        # # Mouse cursor must be within the button to trigger
        # self.button.clicked.connect(self.the_button_was_toggled)
        # # Does not matter if mouse cursor is within the button to trigger
        # self.button.released.connect(self.the_button_was_released)
        self.button.clicked.connect(self.the_button_was_clicked)

        self.button.setChecked(self.button_is_checked)

        # Set the central widget of the Window.
        self.setCentralWidget(self.button)


    def the_button_was_clicked(self):
        # Button becomes one-time-click
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False)

        # Change window title.
        self.setWindowTitle("Button App")


    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        print(f"The current state of the button is: {checked}")


    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()
        print(f"The button was released. The current state of the button is: {self.button_is_checked}")



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()