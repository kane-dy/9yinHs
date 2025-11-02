
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidgetItem,QPushButton,QComboBox
from utils.hwnd_utils import get_win_all,set_wintop,set_unpinwin
import utils.global_variable as gv
import json
import time
#表格模型
def table_models(table):
    hwnd_data = get_win_all()
    len_hwnd_data = len(hwnd_data)
    table.setRowCount(len_hwnd_data)
    alignment = Qt.AlignmentFlag.AlignCenter
    table.setColumnCount(5)
    table.setHorizontalHeaderLabels(['编号', '句柄', '任务', '显示', '启动'])
    table.setColumnWidth(1, 200)
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

                cb = QComboBox()
                cb.addItems(["幸运硬币","拉镖"])
                table.setCellWidget(i, 2, cb)

                view_button = QPushButton("显示")
                view_button.clicked.connect(lambda: btnText(hwnd,cb.currentText()))
                table.setCellWidget(i, 3, view_button)

                data3 = QTableWidgetItem("F1 开始，F2 结束")
                data3.setTextAlignment(alignment) 
                table.setItem(i, 4, data3)
    return table

def btnText(hwnd,cbText):
    print(hwnd)
    print(cbText)
    gv.HWND_CBTEXT=hwnd + "," + cbText
    set_wintop(hwnd)
    time.sleep(1)
    set_unpinwin(hwnd)