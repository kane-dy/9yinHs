from  win32gui import GetWindowRect
import utils.global_variable as gv
from time import sleep
import keyboard

class task_ldq:
        def __init__(self, hwnd):
            left, top, right, bottom = GetWindowRect(hwnd)
            self.left = left
            self.top = top
            self.right = right
            self.bottom = bottom
            self.keytool = gv.KEYTOOL

        def button_task_ldq(self):
            # 点击左键
            self.keytool.DD_btn(1, 2)

        def app_task_ldq(self):
            while True:
                self.button_task_ldq()
                if keyboard.is_pressed('alt'):
                    break
                sleep(0.3)