
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidgetItem,QPushButton,QComboBox
from utils.hwnd_utils import get_win_all,set_wintop,set_unpinwin
from utils.hwnd_utils import window_resolution,window_maximize
from utils.md5_encryption import md5_encrytion
import utils.global_variable as gv
import json
import time

keytool=gv.KEYTOOL
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

                data3 = QTableWidgetItem("Ctrl 开始，alt 结束")
                data3.setTextAlignment(alignment) 
                table.setItem(i, 4, data3)
    return table

def btnText(hwnd,cbText):
    # print("句柄："+hwnd+",任务："+cbText)
    task_text = md5_encrytion(cbText).get_md5() # 获取任务的加密信息
    gv.HWND_CBTEXT = hwnd + "," +task_text
    # print("加密信息："+gv.HWND_CBTEXT)
    set_wintop(hwnd) # 窗口置顶

    time.sleep(0.5)

    set_unpinwin(hwnd) # 取消窗口置顶

    time.sleep(0.5)

    if gv.TASK_YB == task_text: # 任务是运镖的换窗口分辨率1280 x 720
        # print("正在运镖")
        x = 1280
        y = 720
        window_resolution(hwnd, x, y)
        time.sleep(0.5)
        keytool.DD_move(int(x / 2), int(y / 2))
    else: #换取幸运硬币窗口最大化
        # print("幸运硬币")
        window_maximize(hwnd)