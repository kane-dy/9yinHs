from win32gui import GetWindowRect
import utils.global_variable as gv
from time import sleep
import keyboard
class automated_tasks:
    def __init__(self, hwnd):
        left, top, right, bottom = GetWindowRect(hwnd)
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
        self.keytool = gv.KEYTOOL

    def exchange_autotask(self):
        # self.keytool.DD_move(int(self.right/2), int(self.bottom/2))
        self.keytool.DD_key("q")
        sleep(0.5)
        self.keytool.DD_key("e")
        sleep(0.5)
        self.keytool.DD_key("1")
        sleep(0.5)
        self.keytool.DD_key("2")
        sleep(0.5)
        self.keytool.DD_key("r")
        sleep(0.5)
        self.keytool.DD_key("q")

    def app_autotask(self):
        while True:
            self.exchange_autotask()
            if keyboard.is_pressed('alt'):
                break
            sleep(0.3)