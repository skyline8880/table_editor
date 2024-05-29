
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from buttons.filepicker import FilePicker
from buttons.menu_button import action_menu_bar
from core.ui_app import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.fp = FilePicker(main_window=self)
        self.ui.setupUi(self)
        self.ui.menu_button.clicked.connect(
            lambda _: action_menu_bar(self)
        )
        self.ui.open_firstfile_button.clicked.connect(
            self.fp.main_table_upload
        )
        self.ui.open_secondfile_button.clicked.connect(
            self.fp.secondary_table_upload
        )
        self.ui.delete_phone_button.clicked.connect(
            self.fp.remove_phone_from_main
        )
        self.ui.check_fullname_button.clicked.connect(
            self.fp.check_fullname
        )
        self.ui.save_button.clicked.connect(
            self.fp.save_table
        )
        self.ui.clear_panel_button.clicked.connect(
            self.fp.clean_panel
        )
        self.show()


app = QApplication(sys.argv)
window = MainWindow()
