import win32api
from win32con import SRCCOPY
from win32gui import GetWindowDC,DeleteObject,ReleaseDC,GetWindowRect,GetForegroundWindow,WindowFromPoint
from win32ui import  CreateDCFromHandle,CreateBitmap
import cv2
from numpy import frombuffer,uint8,array,rot90
from time import sleep,time


"""
根据窗口的句柄截图
"""
def get_coordinate(hwnd,w,h):
   
    #获取窗口大小
    # left, top, right, bottom = GetWindowRect(hwnd)

    # width = right-left
    # height = bottom-top
    width = w
    height = h
    #窗口的绘制上下文
    wdc = GetWindowDC(hwnd)

    #上下文创建pydc对象
    pydc = CreateDCFromHandle(wdc)

    #兼容DC
    jrdc = pydc.CreateCompatibleDC()
    #位图对象
    wtdx = CreateBitmap()
    
    wtdx.CreateCompatibleBitmap(pydc,width,height)

    jrdc.SelectObject(wtdx)

    jrdc.BitBlt((0,0),(width,height),pydc,(0,0),SRCCOPY)

    #像素数组
    xssz = wtdx.GetBitmapBits(True)

    img = frombuffer(xssz,dtype='uint8')

    img.shape=(height,width,4)

    DeleteObject(wtdx.GetHandle())

    jrdc.DeleteDC()

    ReleaseDC(hwnd,wdc)

    return img




