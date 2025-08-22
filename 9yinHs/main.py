from PyQt6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QAbstractItemView, QHeaderView
from PyQt6 import uic

import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("./9yinHs.ui")
    table: QTableWidget = ui.tableWidget
    table.setRowCount(6)
    table.setColumnCount(7)
    table.setHorizontalHeaderLabels(['编号', '句柄', '显示', '任务', '开始', '结束', '备注'])
    for i in range(6):
        for j in range(7):
            data = QTableWidgetItem(str(i + j))
            table.setItem(i, j, data)
    table.setAlternatingRowColors(True)
    table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
    table.horizontalHeader().setStretchLastSection(True)
    table.horizontalHeader().setStyleSheet("QHeaderView::section{border-top: 1px solid #9370DB}")
    ui.show()
    sys.exit(app.exec())
