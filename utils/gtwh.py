# 在后台录制屏幕



import win32api
import win32gui

def get_Hwnd():
     # 获取当前鼠标【x y】坐标
    point = win32api.GetCursorPos()    
    #通过鼠标坐标 获取鼠标坐标下的【窗口句柄】
    hwnd = win32gui.WindowFromPoint(point)  # 请填写 x 和 y 坐标   
    return  hwnd

     
# if __name__ == "__main__":
#     time.sleep(3)
#      # 获取当前鼠标【x y】坐标
#     point = win32api.GetCursorPos()    
#     #通过鼠标坐标 获取鼠标坐标下的【窗口句柄】
#     hwnd = win32gui.WindowFromPoint(point)  # 请填写 x 和 y 坐标   
#     recording(hwnd)
