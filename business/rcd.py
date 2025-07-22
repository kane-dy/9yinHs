import win32api
import win32gui
import cv2
import numpy as np
import utils.sbowh as sbowh
import utils.gtwh as gtwh
from ultralytics import YOLO

def recording(hwnd):
    #通过窗口句柄 获取当前窗口的【左、上、右、下】四个方向的坐标位置
    left, top, right, bottom = win32gui.GetWindowRect(hwnd) 
    #获取窗口宽高
    width = right-left
    height = bottom-top
    model = YOLO("9YinHsbest.pt")
    # cnt = 0
    while True:
        img = sbowh.get_coordinate(hwnd,width,height)
        frame = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
        # results =  model.predict(frame)
        results = model(frame)
        
        annotated_frame = results[0].plot()
        cv2.namedWindow("img", 0)
        cv2.resizeWindow("img", 1024, 768)
        cv2.imshow("img",annotated_frame)
        if cv2.waitKey(1) == ord('q'): # 按'q'键推出
            break