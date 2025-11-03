from  win32gui import GetWindowRect
import utils.global_variable as gv
from time import sleep
import keyboard
class task_xyyb_theory:
    def __init__(self,hwnd):
        left, top, right, bottom = GetWindowRect(hwnd)
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
        self.keytool = gv.KEYTOOL
    def exchange_xyyb(self):

        # 1、找到天魔追魂刀换取点
        self.keytool.DD_move(int(888+self.left), int(592+self.top))
        # 2、按下左键点击
        self.keytool.DD_btn(1,2)
        # 3、移动到兑换按钮 1036 614
        self.keytool.DD_move(int(1036+self.left),int(614+self.top))
        # 4、按下左键点击兑现
        self.keytool.DD_btn(1, 2)
        # 5、移动到包裹已经换好的书 1850 719
        self.keytool.DD_move(int(1850 + self.left), int(719 + self.top))
        # 6、点击左键选中书籍
        self.keytool.DD_btn(1, 2)
        # 7、移动到回收物品框 坐标：(131,194)
        self.keytool.DD_move(int(131 + self.left), int(194 + self.top))
        # 8、点击回收物品框
        self.keytool.DD_btn(1, 2)
        # 9、移动到回收物品框确认 坐标：(197,550)
        self.keytool.DD_move(int(197 + self.left), int(550 + self.top))
        # 10、点击回收物品框确认
        self.keytool.DD_btn(1, 2)
        # 11、 移动到兑换确认 坐标：(977,614)
        self.keytool.DD_move(int(977 + self.left), int(614 + self.top))
        # 12、 点击确认
        self.keytool.DD_btn(1, 2)
        # 等待0.5秒
        sleep(0.3)

    def app_exchange(self):
        while True:
            self.exchange_xyyb()
            if keyboard.is_pressed('alt'):
                break
            sleep(0.3)