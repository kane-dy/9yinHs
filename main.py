from PyQt6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QAbstractItemView, QHeaderView
from PyQt6 import uic
from utils.utils_tools import path
from solutions.table import table_models
import sys

if __name__ == '__main__':
    
    ui_path = path()+"\models"
    app = QApplication(sys.argv)
    ui = uic.loadUi(ui_path+"\9yinHs.ui")
    table: QTableWidget = ui.tableWidget
    table = table_models(table)
    table.setAlternatingRowColors(True)
    table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
    table.horizontalHeader().setStretchLastSection(True)
    table.horizontalHeader().setStyleSheet("QHeaderView::section{border-top: 1px solid #9370DB}")
    ui.show()
    sys.exit(app.exec())