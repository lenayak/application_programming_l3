import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QThread, QObject

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
                self.path_to_folder = QFileDialog.getExistingDirectory(self, 'Select Folder')
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

    def set_widgets(self) -> None:
        """Sets all widgets on the form"""
        self.set_label(0, 10, "< 1 >")
        self.set_label(300, 10, "< 2 >")
        self.set_label(600, 10, "< 3 >")
        self.set_label(900, 10, "< 4 >")
        self.set_label(1200, 10, "< 5 >")
        self.lineedit1 = self.set_lineedit(0, 90)
        self.lineedit2 = self.set_lineedit(300, 90)
        self.lineedit3 = self.set_lineedit(600, 90)
        self.lineedit4 = self.set_lineedit(900, 90)
        self.lineedit5 = self.set_lineedit(1200, 90)
        self.set_button(0, 610, "Next", self.next_one)
        self.set_button(300, 610, "Next", self.next_two)
        self.set_button(600, 610, "Next", self.next_three)
        self.set_button(900, 610, "Next", self.next_four)
        self.set_button(1200, 610, "Next", self.next_five)
        self.set_button(300, 700, "Copy", self.copy)
        self.set_button(900, 700, "Random", self.rand)

    def next_one(self) -> None:
        """Display next review"""
        path = self.one.__next__()
        file = open(path, 'r', encoding='utf-8')
        self.lineedit1.setText(file.read())
    
    def next_two(self) -> None:
        """Display next review"""
        path = self.two.__next__()
        file = open(path, 'r', encoding='utf-8')
        self.lineedit2.setText(file.read())

    def next_three(self) -> None:
        """Display next review"""
        path = self.three.__next__()
        file = open(path, 'r', encoding='utf-8')
        self.lineedit3.setText(file.read())    

    def next_four(self) -> None:
        """Display next review"""
        path = self.four.__next__()
        file = open(path, 'r', encoding='utf-8')
        self.lineedit4.setText(file.read())   

    def next_five(self) -> None:
        """Display next review"""
        path = self.five.__next__()
        file = open(path, 'r', encoding='utf-8')
        self.lineedit5.setText(file.read())     

    def copy(self) -> None:
        """Create new dataset and annotation"""
        path_to_files = task2.get_path_to_files(self.path_to_folder) 
        new_dataset_path = task2.copy_dataset(self.path_to_folder) 
        task2.write_as_csv(new_dataset_path, path_to_files) 

    def rand(self) -> None:
        """Create random dataset and annotation"""
        task3.create_copy(self.path_to_folder)
        copy_dataset_path = task3.path_to_copy_dataset()
        path_to_files = task3.get_path_to_files(copy_dataset_path)
        task3.write_as_csv(copy_dataset_path, path_to_files)

    def initUI(self) -> None:
        self.resize(1400, 700)
        self.set_widgets()
        self.msg = QMessageBox()
        self.setWindowTitle("Reviews")
        self.setWindowIcon(QIcon('web.png'))


def application():
    """Create an application"""
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
