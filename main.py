from PyQt6.QtWidgets import QApplication, QTableWidget, QAbstractItemView
from PyQt6 import uic

from utils.utils_tools import path
from business.table import table_models
from business.qjrj import listen
from PyQt6.QtGui import QIcon
import sys

if __name__ == '__main__':
    icon_path = path()+"\image\icon.ico"
    app = QApplication(sys.argv)
    icon = QIcon(icon_path)
    ui_path = path()+"\models"
    app.setWindowIcon(icon)
    ui = uic.loadUi(ui_path+"\9yinHs.ui")
    table: QTableWidget = ui.tableWidget
    table = table_models(table)
    table.setAlternatingRowColors(True)
    table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
    table.horizontalHeader().setStretchLastSection(True)
    table.horizontalHeader().setStyleSheet("QHeaderView::section{border-top: 1px solid #9370DB}")
    ui.show()
    listen()
    sys.exit(app.exec())