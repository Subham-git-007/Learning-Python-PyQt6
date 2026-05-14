"""
PyQt6 Widgets
The range of PyQt widgets
"""


import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget
)


# Window full of widgets laid out vertically
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("PyQt6 Widgets")
#
#         layout = QVBoxLayout()
#         widgets = [
#             QCheckBox,
#             QComboBox,
#             QDateEdit,
#             QDateTimeEdit,
#             QDial,
#             QDoubleSpinBox,
#             QFontComboBox,
#             QLabel,
#             QLCDNumber,
#             QLineEdit,
#             QProgressBar,
#             QPushButton,
#             QRadioButton,
#             QSlider,
#             QSpinBox,
#             QTimeEdit,
#         ]
#
#         for w in widgets:
#             layout.addWidget(w())
#
#         widget = QWidget()
#         widget.setLayout(layout)
#
#         self.setCentralWidget(widget)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        # LABEL
        # label = QLabel("Hello")

        # font = label.font()
        # font.setPointSize(30)
        # label.setFont(font)
        # label.setAlignment(
        #     Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        # )

        # label.setPixmap(QPixmap("otje.webp"))
        # label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # label.setScaledContents(True)


        # CHECKBOX
        # checkbox = QCheckBox("This is a checkbox")
        # By default, two state:
        # checkbox.setCheckState(Qt.CheckState.Checked)

        # For tristate:
        # checkbox.setCheckState(Qt.CheckState.PartiallyChecked)
        # OR, checkbox.setTristate(True)


        # COMBOBOX
        # self.combobox = QComboBox()
        # self.combobox.addItems(["One", "Two", "Three"])
        # self.combobox.setEditable(True)

        # Signal that sends the current index of the selected item.
        # self.combobox.currentIndexChanged.connect(self.index_changed)

        # Signal that sends the text of item if changed.
        # self.combobox.currentTextChanged.connect(self.text_changed)


        # LISTWIDGET
        # widget = QListWidget()
        # widget.addItems(["One", "Two", "Three"])

        # widget.currentItemChanged.connect(self.index_changed)
        # widget.currentTextChanged.connect(self.text_changed)


        # LINEEDIT
        # widget = QLineEdit()
        # widget.setMaxLength(10)
        # widget.setPlaceholderText("Enter your text here")
        # widget.setInputMask("000 . 000")

        # make uneditable / read only
        # widget.setReadOnly(True)

        # widget.returnPressed.connect(self.return_pressed)
        # widget.selectionChanged.connect(self.selection_changed)
        # widget.textChanged.connect(self.text_changed)
        # widget.textEdited.connect(self.text_edited)


        # SPINBOX
        # widget = QSpinBox()
        # widget = QDoubleSpinBox()

        # widget.setMinimum(-2.5)
        # widget.setMaximum(10)
        # Or: widget.setRange(-9, 3)

        # widget.lineEdit().setReadOnly(True)
        #
        # widget.setPrefix("$")
        # widget.setSuffix("c")
        # widget.setSingleStep(0.25)
        # widget.valueChanged.connect(self.value_changed)
        # widget.textChanged.connect(self.value_changed_str)


        # SLIDER
        # widget = QSlider(Qt.Orientation.Horizontal)

        # widget.setMinimum(-10)
        # widget.setMaximum(3)
        # Or: widget.setRange(-10, 3)
        # widget.setSingleStep(3)

        # widget.valueChanged.connect(self.value_changed)
        # widget.sliderMoved.connect(self.slider_position)
        # widget.sliderPressed.connect(self.slider_pressed)
        # widget.sliderReleased.connect(self.slider_released)


        # DIAL
        widget = QDial()
        widget.setRange(-10, 100)
        widget.setSingleStep(1)

        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(widget)



    # def index_changed(self, index):
    #     print(f"Index: {index}")
    #
    #
    # def text_changed(self, text: str):
    #     print(f"Text changed to: {text}")

    # def return_pressed(self):
    #     print("Return pressed!")
    #     self.centralWidget().setText("BOOM!")
    #
    # def selection_changed(self):
    #     print("Selection changed")
    #     print(self.centralWidget().selectedText())
    #
    # def text_changed(self, s):
    #     print("Text changed...")
    #     print(s)
    #
    # def text_edited(self, s):
    #     print("Text edited...")
    #     print(s)

    # def value_changed(self, i):
    #     print(i)
    #
    # def value_changed_str(self, s):
    #     print(s)

    def value_changed(self, i):
        print(i)

    def slider_position(self, p):
        print("Position", p)

    def slider_pressed(self):
        print("Pressed!")

    def slider_released(self):
        print("Released")



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()