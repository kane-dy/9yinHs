from PyQt6.QtWidgets import QTableWidgetItem
from utils.hwnd_utils import get_win_all
import json
#表格模型
def table_models(table):
    hwnd_data = get_win_all()
    len_hwnd_data = len(hwnd_data)
    table.setRowCount(len_hwnd_data)
    table.setColumnCount(7)
    table.setHorizontalHeaderLabels(['编号', '句柄', '显示', '任务', '开始', '结束', '备注'])
    for i in range(len_hwnd_data):
        data = hwnd_data[i]
        data = json.dumps(data)
        dict_json = json.loads(data)
        for key in  dict_json :
            hwnd= key
            title =  dict_json[key]
            for j in range(7):
                data = QTableWidgetItem()
                data.setText(hwnd)
                table.setItem(i, 0, data)
                data1 = QTableWidgetItem()
                data1.setText(title)
                table.setItem(i, 1, data1)
                data2 = QTableWidgetItem("asdf")
                table.setItem(i, j+1, data2)
        
    return table
