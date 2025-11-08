from win32gui import *
from ctypes import *
from time import sleep

vk = {'esc': 100,'tab': 300,'space': 603,'~': 200,'5': 205, 'c': 503, 'n': 506, 'z': 501, '3': 203, '1': 201, 'd': 403, '0': 210, 'l': 409, '8': 208, 'w': 302, 'u': 307, '4': 204, 'e': 303, '[': 311, 'f': 404, 'y': 306, 'x': 502, 'g': 405, 'v': 504, 'r': 304, 'i': 308, 'a': 401, 'm': 507, 'h': 406, '.': 509, ',': 508, ']': 312, '/': 510, '6': 206, '2': 202, 'b': 505, 'k': 408, '7': 207, 'q': 301, "'": 411, '\\': 313, 'j': 407, '`': 200, '9': 209, 'p': 310, 'o': 309, 't': 305, '-': 211, '=': 212, 's': 402, ';': 410}
vk_sy ={1:709,2:712,3:711,4:710,5:408,6:407}

class key_tool:
    def __init__(self,path):
        self.ddl_path =path+"\models"+'\\dd.54900.dll'
        self.dd_dll = windll.LoadLibrary(self.ddl_path)
        self.dd_dll.DD_btn(0) #DD Initialize
    # 键盘按键
    def DD_key(self,key):
        k = vk[key]
        self.dd_dll.DD_key(k,1)
        sleep(0.2)
        self.dd_dll.DD_key(k,2)

    # 鼠标移动
    def DD_move(self,x,y):
        self.dd_dll.DD_mov(x, y)
        sleep(0.4)

    ''' 
    鼠标按键
    1 = 左键按下 ，2 = 左键放开
    4 = 右键按下 ，8 = 右键放开
    16 = 中键按下 ，32 = 中键放开
    64 =4键按下 ，128 =4键放开
    256 =5键按下 ，512 =5键放开
    '''

    def DD_btn(self,d,u):
        self.dd_dll.DD_btn(d, u)
        sleep(0.1)
        self.dd_dll.DD_btn(u)