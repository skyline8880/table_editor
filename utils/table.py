from PySide6.QtWidgets import QTableWidgetItem


class TableData():
    def __init__(self, data, main_window):
        super().__init__()
        self.data = data
        self.mw = main_window
        self.headers = None
        self.columns = None
        self.rows = None

    def columns_and_rows_count(self):
        return self.data.shape

    def get_headers(self):
        return self.data.columns.tolist()

    def create_table(self):
        self.rows, self.columns = self.columns_and_rows_count()
        self.headers = self.get_headers()
        self.mw.ui.tableView.setRowCount(self.rows)
        self.mw.ui.tableView.setColumnCount(self.columns)
        self.mw.ui.tableView.setHorizontalHeaderLabels(self.headers)
        self.insert_data()

    def insert_data(self):
        for col_id, _ in enumerate(self.headers):
            for row_id, row_value in enumerate(self.data.to_numpy().tolist()):
                self.mw.ui.tableView.setItem(
                    row_id, col_id, QTableWidgetItem(str(row_value[col_id]))
                )

    def hide_table(self):
        self.mw.ui.tableView.clear()
        self.mw.ui.tableView.setRowCount(0)
        self.mw.ui.tableView.setColumnCount(0)
