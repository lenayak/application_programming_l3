import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import first as task1
import second as task2
import third as task3
import iterator


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("MainWindow")
        self.setGeometry(300, 250, 800, 500)
        self.path_to_folder = str()
        while self.folderpath == "":
            try:
                self.folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
                paths_to_files = dataset_to_csv.get_paths_to_files(self.folderpath)
                dataset_to_csv.write_as_csv(paths_to_files)
            except:
                print("Датасет не найден")
                self.folderpath = ""

    def message_about_error(self) -> None:
        """Displays error message that dir does not exist"""


def application():
    """Create an application"""
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
