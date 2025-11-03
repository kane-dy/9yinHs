import win32api
import win32con
from win32gui import *
from time import sleep
from fuzzywuzzy import fuzz



# 获取窗口句柄
def get_hwnd():
    sleep(3)
    coordinate = win32api.GetCursorPos()
    x = coordinate[0]
    y = coordinate[1]
    # # 通过坐标获取坐标下的【窗口句柄】
    hwnd = WindowFromPoint(coordinate) 
    return hwnd
 # 通过句柄窗口置顶
def set_wintop(hwnd):
   SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,win32con.SWP_NOMOVE | win32con.SWP_NOACTIVATE | win32con.SWP_NOOWNERZORDER | win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE)

# 通过句柄取消窗口置顶
def set_unpinwin(hwnd):
    SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)

# 判断窗口是否置顶
def isWndTopMost(hwnd):
        return GetWindowLong(hwnd, win32con.GWL_EXSTYLE) & win32con.WS_EX_TOPMOST

#获取所有窗口句柄
def get_all_windows():
    hwnd_list = []
    EnumWindows(lambda hWnd, param: param.append(hWnd), hwnd_list)
    return hwnd_list
# 通过句柄获得标题
def get_title(hwnd):
    title = GetWindowText(hwnd)
    return title
# 获取全部
def get_win_all():
    hwnd_l = []
    hWnd_list = get_all_windows()
    for i in range(len(hWnd_list)):
            title = get_title(hWnd_list[i])
            
            nine_yin = fuzz.partial_ratio('九阴真经',title) 
            g_yin = fuzz.partial_ratio('Google',title) 
            IE_yin = fuzz.partial_ratio('Internet',title) 
            if nine_yin  and g_yin != 100 and IE_yin != 100:
                data ={}
                hwnd = hWnd_list[i]
                data[hwnd] = title
                hwnd_l.append(data)
    return hwnd_l

# 调节屏幕分辨率
def window_resolution(hwnd,x,y):
    MoveWindow(hwnd, 0, 0, x, y, True)


#最大化窗口
def window_maximize(hwnd):
    ShowWindow(hwnd, win32con.SW_MAXIMIZE)