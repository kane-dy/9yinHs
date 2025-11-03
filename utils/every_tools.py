from pynput import keyboard
import win32api
import win32gui
import time



# 获取窗口大小
def get_Hwnd():
    # 获取当前鼠标【x y】坐标
    point = win32api.GetCursorPos()
    # 通过鼠标坐标 获取鼠标坐标下的【窗口句柄】
    hwnd = win32gui.WindowFromPoint(point)  # 请填写 x 和 y 坐标
    left, top, right, bottom = win32gui.GetWindowRect(hwnd) # 获取窗口大小
    coord_left_up = (left, top) # 左上角坐标
    return left,top,right,bottom
# 获取当前坐标
def get_move_point():
        point_x, point_y  = win32api.GetCursorPos() # 获取当前鼠标【x y】坐标
        return point_x, point_y
# 获取相对坐标
def get_relative_coord():
    point_x,point_y= get_move_point()
    left, top, right, bottom = get_Hwnd()
    x = point_x - left
    y = point_y - top
    return x,y
if __name__ == "__main__":
    while True:
        x,y=get_relative_coord()
        print("坐标：("+str(x)+","+str(y)+")")
        time.sleep(0.5)