import os
import sys

from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QFont, QIcon, QPixmap
from PySide6.QtWidgets import (QCheckBox, QFrame, QHBoxLayout, QLabel,
                               QProgressBar, QPushButton, QSizePolicy,
                               QTableWidget, QVBoxLayout, QWidget)

from core.constants import DEVELOPER


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, relative_path)


custom_img = resource_path("icons\\sp_icon.png")
menu_ing = resource_path("icons\\menu.png")
upload_img = resource_path("icons\\upload_files.png")
circle_phone_img = resource_path("icons\\circle-phone-flip.png")
chalkboard_user_img = resource_path("icons\\chalkboard-user.png")
save_excel_img = resource_path("icons\\save_to_excel.png")
broom_img = resource_path("icons\\broom.png")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth()
        )
        MainWindow.setSizePolicy(sizePolicy)
        self.MainWidget = QWidget(MainWindow)
        self.MainWidget.setObjectName(u"MainWidget")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.MainWidget.sizePolicy().hasHeightForWidth()
        )
        self.MainWidget.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.MainWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.topframe = QFrame(self.MainWidget)
        self.topframe.setObjectName(u"topframe")
        self.topframe.setFrameShape(QFrame.StyledPanel)
        self.topframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.topframe)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.menuframe = QFrame(self.topframe)
        self.menuframe.setObjectName(u"menuframe")
        self.menuframe.setFrameShape(QFrame.StyledPanel)
        self.menuframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.menuframe)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menu_button = QPushButton(self.menuframe)
        self.menu_button.setObjectName(u"menu_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.menu_button.sizePolicy().hasHeightForWidth()
        )
        self.menu_button.setSizePolicy(sizePolicy2)
        icon = QIcon()
        icon.addFile(menu_ing, QSize(), QIcon.Normal, QIcon.Off)
        self.menu_button.setIcon(icon)
        self.menu_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.menu_button)

        self.horizontalLayout.addWidget(self.menuframe, 0, Qt.AlignLeft)

        self.headerframe = QFrame(self.topframe)
        self.headerframe.setObjectName(u"headerframe")
        sizePolicy3 = QSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Preferred
        )
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.headerframe.sizePolicy().hasHeightForWidth()
        )
        self.headerframe.setSizePolicy(sizePolicy3)
        self.headerframe.setFrameShape(QFrame.StyledPanel)
        self.headerframe.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.headerframe)

        self.verticalLayout.addWidget(self.topframe)

        self.bodyframe = QFrame(self.MainWidget)
        self.bodyframe.setObjectName(u"bodyframe")
        sizePolicy1.setHeightForWidth(
            self.bodyframe.sizePolicy().hasHeightForWidth()
        )
        self.bodyframe.setSizePolicy(sizePolicy1)
        self.bodyframe.setFrameShape(QFrame.StyledPanel)
        self.bodyframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.bodyframe)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.left_bodyframe = QFrame(self.bodyframe)
        self.left_bodyframe.setMinimumWidth(2)
        self.left_bodyframe.setMaximumWidth(2)
        self.left_bodyframe.size()
        self.left_bodyframe.setObjectName(u"left_bodyframe")
        self.left_bodyframe.setFrameShape(QFrame.StyledPanel)
        self.left_bodyframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.left_bodyframe)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.left_buttonframe = QFrame(self.left_bodyframe)
        self.left_buttonframe.setObjectName(u"left_buttonframe")
        sizePolicy1.setHeightForWidth(
            self.left_buttonframe.sizePolicy().hasHeightForWidth()
        )
        self.left_buttonframe.setSizePolicy(sizePolicy1)
        self.left_buttonframe.setFrameShape(QFrame.StyledPanel)
        self.left_buttonframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_buttonframe)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.open_firstfile_button = QPushButton(self.left_buttonframe)
        self.open_firstfile_button.setObjectName(u"open_firstfile_button")
        icon1 = QIcon()
        icon1.addFile(upload_img, QSize(), QIcon.Normal, QIcon.Off)
        self.open_firstfile_button.setIcon(icon1)
        self.open_firstfile_button.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.open_firstfile_button)

        self.open_secondfile_button = QPushButton(self.left_buttonframe)
        self.open_secondfile_button.setObjectName(u"open_secondfile_button")
        self.open_secondfile_button.setIcon(icon1)
        self.open_secondfile_button.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.open_secondfile_button)

        self.delete_phone_button = QPushButton(self.left_buttonframe)
        self.delete_phone_button.setObjectName(u"delete_phone_button")
        icon2 = QIcon()
        icon2.addFile(circle_phone_img, QSize(), QIcon.Normal, QIcon.Off)
        self.delete_phone_button.setIcon(icon2)
        self.delete_phone_button.setIconSize(QSize(20, 20))
        self.delete_phone_button.setDisabled(True)

        self.verticalLayout_2.addWidget(self.delete_phone_button)

        self.check_fullname_button = QPushButton(self.left_buttonframe)
        self.check_fullname_button.setObjectName(u"check_fullname_button")
        font = QFont()
        font.setItalic(False)
        self.check_fullname_button.setFont(font)
        icon3 = QIcon()
        icon3.addFile(chalkboard_user_img, QSize(), QIcon.Normal, QIcon.Off)
        self.check_fullname_button.setIcon(icon3)
        self.check_fullname_button.setIconSize(QSize(20, 20))
        self.check_fullname_button.setDisabled(True)

        self.verticalLayout_2.addWidget(self.check_fullname_button)

        self.save_button = QPushButton(self.left_buttonframe)
        self.save_button.setObjectName(u"save_button")
        icon4 = QIcon()
        icon4.addFile(save_excel_img, QSize(), QIcon.Normal, QIcon.Off)
        self.save_button.setIcon(icon4)
        self.save_button.setIconSize(QSize(20, 20))
        self.save_button.setDisabled(True)

        self.verticalLayout_2.addWidget(self.save_button)

        self.clear_panel_button = QPushButton(self.left_buttonframe)
        self.clear_panel_button.setObjectName(u"clear_panel_button")
        self.clear_panel_button.setAutoFillBackground(False)
        icon5 = QIcon()
        icon5.addFile(broom_img, QSize(), QIcon.Normal, QIcon.Off)
        self.clear_panel_button.setIcon(icon5)
        self.clear_panel_button.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.clear_panel_button)

        self.include_fullname_checkbox = QCheckBox(self.left_buttonframe)
        self.include_fullname_checkbox.setObjectName(
            u"include_fullname_checkbox"
        )
        self.include_fullname_checkbox.setDisabled(True)

        self.verticalLayout_2.addWidget(self.include_fullname_checkbox)

        self.label_1 = QLabel(self.left_buttonframe)
        self.label_1.setObjectName(u"label_1")

        self.verticalLayout_2.addWidget(self.label_1)

        self.total_label = QLabel(self.left_buttonframe)
        self.total_label.setObjectName(u"total_label")

        self.verticalLayout_2.addWidget(self.total_label)

        self.label_2 = QLabel(self.left_buttonframe)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.left_buttonframe)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.verticalLayout_3.addWidget(
            self.left_buttonframe, 0, Qt.AlignLeft
        )

        self.horizontalLayout_6.addWidget(self.left_bodyframe, 0, Qt.AlignTop)

        self.right_bodyframe = QFrame(self.bodyframe)
        self.right_bodyframe.setObjectName(u"right_bodyframe")
        sizePolicy1.setHeightForWidth(
            self.right_bodyframe.sizePolicy().hasHeightForWidth()
        )
        self.right_bodyframe.setSizePolicy(sizePolicy1)
        self.right_bodyframe.setFrameShape(QFrame.StyledPanel)
        self.right_bodyframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.right_bodyframe)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tableView = QTableWidget(self.right_bodyframe)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_4.addWidget(self.tableView)

        self.horizontalLayout_6.addWidget(self.right_bodyframe)

        self.verticalLayout.addWidget(self.bodyframe)

        self.botomframe = QFrame(self.MainWidget)
        self.botomframe.setObjectName(u"botomframe")
        sizePolicy1.setHeightForWidth(
            self.botomframe.sizePolicy().hasHeightForWidth()
        )
        self.botomframe.setSizePolicy(sizePolicy1)
        self.botomframe.setFrameShape(QFrame.StyledPanel)
        self.botomframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.botomframe)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.devlabel_frame = QFrame(self.botomframe)
        self.devlabel_frame.setObjectName(u"devlabel_frame")
        self.devlabel_frame.setFrameShape(QFrame.StyledPanel)
        self.devlabel_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.devlabel_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, 0, 9, 0)
        self.dev_label = QLabel(self.devlabel_frame)
        self.dev_label.setObjectName(u"dev_label")
        sizePolicy1.setHeightForWidth(
            self.dev_label.sizePolicy().hasHeightForWidth()
        )
        self.dev_label.setSizePolicy(sizePolicy1)
        self.dev_label.setTextFormat(Qt.AutoText)
        self.dev_label.setAlignment(Qt.AlignCenter)
        self.dev_label.setOpenExternalLinks(False)

        self.horizontalLayout_4.addWidget(self.dev_label)

        self.horizontalLayout_3.addWidget(
            self.devlabel_frame, 0, Qt.AlignLeft
        )

        self.progressbar_frame = QFrame(self.botomframe)
        self.progressbar_frame.setObjectName(u"progressbar_frame")
        self.progressbar_frame.setFrameShape(QFrame.StyledPanel)
        self.progressbar_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.progressbar_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.progressbar = QProgressBar(self.progressbar_frame)
        self.progressbar.setObjectName(u"progressbar")
        self.progressbar.setValue(0)
        self.progressbar.setVisible(False)

        self.horizontalLayout_5.addWidget(self.progressbar)

        self.horizontalLayout_3.addWidget(self.progressbar_frame)

        self.verticalLayout.addWidget(self.botomframe, 0, Qt.AlignBottom)

        MainWindow.setCentralWidget(self.MainWidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate(
                "Редактор таблиц", u"Редактор таблиц", None
            )
        )
        icon = QIcon()
        icon.addPixmap(QPixmap(custom_img))
        MainWindow.setWindowIcon(icon)
        self.menu_button.setText(
            QCoreApplication.translate(
                "MainWindow", u"\u041c\u0415\u041d\u042e", None
            )
        )
        self.open_firstfile_button.setText(
            QCoreApplication.translate(
                "MainWindow",
                (u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c "
                 u"\u043e\u0441\u043d\u043e\u0432\u043d\u0443\u044e "
                 u"\u0442\u0430\u0431\u043b\u0438\u0446\u0443"),
                None
            )
        )
        self.open_secondfile_button.setText(
            QCoreApplication.translate(
                "MainWindow",
                (u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c "
                 u"\u0432\u0442\u043e\u0440\u0443\u044e "
                 u"\u0442\u0430\u0431\u043b\u0438\u0446\u0443"),
                None
            )
        )
        self.delete_phone_button.setText(
            QCoreApplication.translate(
                "MainWindow",
                (u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c "
                 u"\u043d\u043e\u043c\u0435\u0440\u0430 \u0438\u0437 "
                 u"\u043e\u0441\u043d\u043e\u0432\u043d\u043e\u0439"),
                None
            )
        )
        self.check_fullname_button.setText(
            QCoreApplication.translate(
                "MainWindow",
                (u"\u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430 "
                 u"\u0424\u0418\u041e \u0432 "
                 u"\u043e\u0441\u043d\u043e\u0432\u043d\u043e\u0439"),
                None
            )
        )
        self.save_button.setText(
            QCoreApplication.translate(
                "MainWindow",
                (u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c"),
                None
            )
        )
        self.clear_panel_button.setText(
            QCoreApplication.translate(
                "MainWindow",
                (u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c "
                 u"\u043f\u0430\u043d\u0435\u043b\u044c"),
                None
            )
        )
        self.include_fullname_checkbox.setText(
            QCoreApplication.translate(
                "MainWindow",
                (u"\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c "
                 u"\u0424\u0418\u041e \u0432 "
                 u"\u0441\u043f\u0438\u0441\u043e\u043a"),
                None
            )
        )
        self.label_1.setText("")
        self.total_label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.dev_label.setText(DEVELOPER)
