
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidgetItem,QPushButton,QComboBox
from utils.hwnd_utils import get_win_all
import json
#表格模型
def table_models(table):
    hwnd_data = get_win_all()
    len_hwnd_data = len(hwnd_data)
    table.setRowCount(len_hwnd_data)
    alignment = Qt.AlignmentFlag.AlignCenter
    table.setColumnCount(5)
    table.setHorizontalHeaderLabels(['编号', '句柄', '显示', '任务', '启动'])
    for i in range(len_hwnd_data):
        data = hwnd_data[i]
        data = json.dumps(data)
        dict_json = json.loads(data)
        for key in  dict_json :
            hwnd= key
            title =  dict_json[key]
            for j in range(5):

                data = QTableWidgetItem()
                data.setText(hwnd)
                data.setTextAlignment(alignment) 
                table.setItem(i, 0, data)

                data1 = QTableWidgetItem()
                data1.setText(title)
                data1.setTextAlignment(alignment) 
                table.setItem(i, 1, data1)
                
                view_button = QPushButton("显示")
                table.setCellWidget(i, 2, view_button)

                cb = QComboBox()
                cb.addItems(["幸运硬币"])
                table.setCellWidget(i, 3, cb)

                data3 = QTableWidgetItem("F1 开始，F2 结束")
                data3.setTextAlignment(alignment) 
                table.setItem(i, 4, data3)
    return table
