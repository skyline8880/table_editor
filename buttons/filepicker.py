import os

import pandas as pd
from PySide6.QtWidgets import QFileDialog, QWidget

from core.constants import DEVELOPER
from utils.messages import MessageDialog
from utils.table import TableData
from utils.utils import empty_duplicates, fullname_duplicates, phone_corrector


class FilePicker():
    def __init__(self, main_window=None):
        self.main_window = main_window
        self.parent = QWidget()
        self.main_file = None
        self.main_phone_column = None
        self.main_person_column = None
        self.main_birth_day = None
        self.main_birth_month = None
        self.secondary_file = None
        self.secondary_phone_column = None
        self.secondary_person_column = None
        self.result = None
        self.relative_person = None
        self.model_view = None

    def create_table(self):
        self.model_view = TableData(self.result, self.main_window)
        self.model_view.create_table()

    def check_both_files(self):
        if self.main_file is not None and self.secondary_file is None:
            self.main_window.ui.save_button.setDisabled(False)
            if self.main_birth_day is not None:
                (self.main_window.ui.
                    include_birthday_checkbox.setDisabled(False))
            if self.main_person_column is not None:
                (self.main_window.ui.
                    include_fullname_checkbox.setDisabled(False))
        elif self.main_file is not None and self.secondary_file is not None:
            self.main_window.ui.save_button.setDisabled(False)
            self.main_window.ui.delete_phone_button.setDisabled(False)
            if self.main_birth_day is not None:
                (self.main_window.ui.
                    include_birthday_checkbox.setDisabled(False))
            if self.main_person_column is not None:
                (self.main_window.ui.
                    include_fullname_checkbox.setDisabled(False))
                if self.secondary_person_column is not None:
                    (self.main_window.ui.
                        check_fullname_button.setDisabled(False))
        else:
            (self.main_window.ui.
                save_button.setDisabled(True))
            (self.main_window.ui.
                delete_phone_button.setDisabled(True))
            (self.main_window.ui.
                check_fullname_button.setDisabled(True))
            (self.main_window.ui.
                include_fullname_checkbox.setChecked(False))
            (self.main_window.ui.
                include_fullname_checkbox.setDisabled(True))
            (self.main_window.ui.
                include_birthday_checkbox.setChecked(False))
            (self.main_window.ui.
                include_birthday_checkbox.setDisabled(True))

    def main_table_upload(self):
        filename = QFileDialog().getOpenFileName(
            parent=self.parent,
            caption="Выберите основную таблицу",
            dir=os.path.abspath("."),
            filter="Excel (*.xls *.xlsx);;CSV (*.csv)",
            selectedFilter=""
        )
        data_file = filename[0]
        if data_file == "":
            return
        if filename[-1].split()[0].lower() == "excel":
            try:
                dataframe = pd.read_excel(data_file, dtype="str")
            except Exception as e:
                MessageDialog(
                    "Ошибка",
                    (f"Файл: {data_file.split('/')[-1]}.\n"
                     f"Описание: {e}\n")
                    )
                return
        else:
            try:
                dataframe = pd.read_csv(
                    data_file,
                    sep=";",
                    dtype="str",
                    encoding="utf_8",
                    on_bad_lines="skip"
                )
            except Exception as e:
                MessageDialog(
                    "Ошибка",
                    (f"Файл: {data_file.split('/')[-1]}.\n"
                     f"Описание: {e}\n")
                    )
                return
        self.main_phone_column = None
        self.main_person_column = None
        self.relative_person = None
        self.main_birth_day = None
        self.main_birth_month = None
        for column in dataframe.columns.to_list():
            if self.main_phone_column is None:
                if "телефон" in column.strip().lower():
                    self.main_phone_column = column
            if "персона" in column.lower():
                self.main_person_column = column
            if "фио персоны" in column.lower():
                self.main_person_column = column
            if "фио связи" in column.lower():
                self.relative_person = column
            if "день" in column.lower():
                self.main_birth_day = column
            if "рождения" in column.lower():
                self.main_birth_month = column
            if self.main_birth_day is None:
                if ("дата рождения" in column.lower() 
                        or "день рождения" in column.lower()):
                    self.main_birth_day = column
        if (self.main_phone_column is None
                and self.main_person_column is None):
            MessageDialog(
                "Ошибка",
                (
                    "В таблице отсутствует поле: Телефон!\n"
                    "Добавьте название столбца в любом регистре."
                )
            )
            return
        progressbar = self.main_window.ui.progressbar
        progressbar.setVisible(True)
        self.main_window.ui.dev_label.setText("Загрузка")
        dataframe = dataframe.drop_duplicates(
            subset=[self.main_phone_column])
        dataframe = dataframe.dropna(subset=[self.main_phone_column])
        progressbar.setMaximum(dataframe.shape[0])
        dataframe["correct_phone"] = dataframe.apply(
            phone_corrector,
            axis=1,
            args=(progressbar, self.main_phone_column)
        )
        dataframe = dataframe.dropna(subset=["correct_phone"])
        self.main_file = dataframe
        self.result = self.main_file
        progressbar.setVisible(False)
        progressbar.setValue(0)
        self.main_window.ui.dev_label.setText(DEVELOPER)
        self.main_window.ui.label_1.setText(
            f"Файл: {data_file.split('/')[-1]}"
        )
        self.main_window.ui.total_label.setText(
            f"Основной: {dataframe.shape[0]}"
        )
        self.check_both_files()
        self.create_table()

    def secondary_table_upload(self):
        filename = QFileDialog().getOpenFileName(
            parent=self.parent,
            caption="Выберите вторую таблицу",
            dir=os.path.abspath("."),
            filter="Excel (*.xls *.xlsx);;CSV (*.csv)",
            selectedFilter=""
        )
        data_file = filename[0]
        if data_file == "":
            return
        progressbar = self.main_window.ui.progressbar
        progressbar.setVisible(True)
        self.main_window.ui.dev_label.setText("Загрузка")
        if filename[-1].split()[0].lower() == "excel":
            try:
                dataframe = pd.read_excel(data_file, dtype="str")
            except Exception as e:
                MessageDialog(
                    "Ошибка",
                    (f"Файл: {data_file.split('/')[-1]}.\n"
                     f"Описание: {e}\n")
                    )
                return
        else:
            try:
                dataframe = pd.read_csv(
                    data_file,
                    sep=";",
                    dtype="str",
                    encoding="utf_8",
                    on_bad_lines="skip"
                )
            except Exception as e:
                MessageDialog(
                    "Ошибка",
                    (f"Файл: {data_file.split('/')[-1]}.\n"
                     f"Описание: {e}\n")
                    )
                return
        self.secondary_phone_column = None
        self.secondary_person_column = None
        for column in dataframe.columns.to_list():
            if self.secondary_phone_column is None:
                if "телефон" in column.strip().lower():
                    self.secondary_phone_column = column
            if "персона" in column.lower():
                self.secondary_person_column = column
        if (self.secondary_phone_column is None
                and self.secondary_person_column is None):
            MessageDialog(
                "Ошибка",
                (
                    "В таблице отсутствует поле: Телефон и Персона!\n"
                    "Добавьте одно из полей в любом регистре."
                )
            )
            return
        if self.secondary_phone_column is not None:
            dataframe = dataframe.drop_duplicates(
                subset=[self.secondary_phone_column])
            dataframe = dataframe.dropna(subset=[self.secondary_phone_column])
            progressbar.setMaximum(dataframe.shape[0])
            dataframe["correct_phone"] = dataframe.apply(
                phone_corrector,
                axis=1,
                args=(progressbar, self.secondary_phone_column)
            )
            dataframe = dataframe.dropna(subset=["correct_phone"])
        self.secondary_file = dataframe
        progressbar.setVisible(False)
        progressbar.setValue(0)
        self.main_window.ui.dev_label.setText(DEVELOPER)
        self.main_window.ui.label_2.setText(
            f"Файл: {data_file.split('/')[-1]}"
        )
        self.main_window.ui.label_3.setText(
            f"Второй: {dataframe.shape[0]}"
        )
        self.check_both_files()

    def remove_phone_from_main(self, main_window):
        if self.main_file is not None and self.secondary_file is not None:
            progressbar = self.main_window.ui.progressbar
            progressbar.setVisible(True)
            self.main_window.ui.dev_label.setText("Удаление")
            secondary_list = self.secondary_file[
                "correct_phone"
            ].to_numpy().tolist()
            progressbar.setMaximum(self.main_file.shape[0])
            self.main_file["removeable"] = self.main_file.apply(
                empty_duplicates,
                axis=1,
                args=(progressbar, "correct_phone", secondary_list)
            )
            progressbar.setVisible(False)
            progressbar.setValue(0)
            self.main_window.ui.dev_label.setText(DEVELOPER)
            self.result = self.main_file.dropna(subset=["removeable"])
            self.main_window.ui.total_label.setText(
                f"Основной: {self.result.shape[0]}"
            )
            self.create_table()

    def check_fullname(self):
        label = self.main_window.ui.dev_label
        progressbar = self.main_window.ui.progressbar
        progressbar.setVisible(True)
        label.setText("Поиск")

        second_person_list = self.secondary_file[
            self.secondary_person_column
        ].to_numpy().tolist()
        checkable = self.main_person_column
        if self.relative_person is not None:
            checkable = self.relative_person
        progressbar.setMaximum(self.main_file.shape[0])
        self.main_file["person_jun"] = self.main_file.apply(
            fullname_duplicates,
            axis=1,
            args=(
                progressbar,
                checkable,
                second_person_list
            )
        )
        self.result = self.main_file.dropna(subset=["person_jun"])
        progressbar.setVisible(False)
        progressbar.setValue(0)
        label.setText(DEVELOPER)
        self.main_window.ui.total_label.setText(
            f"Основной: {self.result.shape[0]}")
        self.create_table()

    def save_table(self):
        filename = QFileDialog().getSaveFileName(
            parent=self.parent,
            caption="Сохранить основную таблицу",
            dir=os.path.abspath("."),
            filter="Excel (*.xlsx);;CSV (*.csv)",
            selectedFilter=""
        )
        data_file = filename[0]
        if data_file == "":
            return
        phone = "correct_phone"
        if "removeable" in self.result.columns.to_list():
            phone = "removeable"
        cols = phone
        if self.main_window.ui.include_fullname_checkbox.isChecked():
            if self.main_person_column is not None:
                cols = [phone, self.main_person_column]
        if self.main_window.ui.include_birthday_checkbox.isChecked():
            if self.main_birth_day is not None:
                cols.append(self.main_birth_day)
                if self.main_birth_month is not None:
                    cols.append(self.main_birth_month)
        to_save = self.result[cols]
        if filename[-1].split()[0].lower() == "excel":
            to_save.to_excel(
                data_file,
                header=False,
                index=False,
                engine="xlsxwriter"
            )
        else:
            to_save.to_csv(
                data_file,
                header=False,
                index=False,
                encoding="cp1251",
                sep=";"
            )

    def clean_panel(self):
        self.main_window.ui.total_label.setText("")
        self.main_window.ui.label_2.setText("")
        self.main_window.ui.label_1.setText("")
        self.main_window.ui.label_3.setText("")
        self.main_window.ui.dev_label.setText(DEVELOPER)
        self.main_window.ui.progressbar.setVisible(False)
        self.main_window.ui.progressbar.setValue(0)
        self.main_file = None
        self.main_phone_column = None
        self.main_person_column = None
        self.secondary_file = None
        self.secondary_phone_column = None
        self.secondary_person_column = None
        self.total_label = None
        self.secondary_label = None
        self.check_both_files()
        if self.model_view is not None:
            self.model_view.hide_table()
