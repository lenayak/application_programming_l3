import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow

import first as task1
import second as task2
import third as task3
import iterator as it


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("MainWindow")
        self.setGeometry(300, 250, 800, 500)
        self.path_to_folder = str()
        while self.path_to_folder == "":
            try:
                self.path_to_folder = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
                paths_to_files = task1.get_paths_to_files(self.path_to_folder)
                task1.write_as_csv(paths_to_files)
            except:
                print("Датасет не найден")
                self.path_to_folder = ""
        self.star_one = it.SimpleIterator("annotation.csv", "1")
        self.star_two = it.SimpleIterator("annotation.csv", "2")
        self.star_three = it.SimpleIterator("annotation.csv", "3")
        self.star_four = it.SimpleIterator("annotation.csv", "4")
        self.star_five = it.SimpleIterator("annotation.csv", "5")
        self.initUI()

    def set_label(self, x: int, y: int, text: str) -> None:
        """Sets the label on the form by coordinates"""
        reviews = QLabel(text, self)
        reviews.resize(reviews.sizeHint())
        reviews.move(x, y)

    def set_lineedit(self, x: int, y: int) -> QTextEdit:
        """Sets the TextEdit on the form by coordinates"""
        reviews_edit = QTextEdit(' ', self)
        reviews_edit.resize(300, 500)
        reviews_edit.setReadOnly(True)
        reviews_edit.move(x, y)
        return reviews_edit

    def set_button(self, x: int, y: int, text: str, function) -> QPushButton:
        """Sets the PushButton on the form by coordinates"""
        button = QPushButton(text, self)
        button.resize(button.sizeHint())
        button.move(x, y)
        button.clicked.connect(function)
        return button



def application():
    """Create an application"""
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
