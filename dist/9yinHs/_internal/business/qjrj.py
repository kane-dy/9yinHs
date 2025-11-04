from time import sleep

from pynput import keyboard
import utils.global_variable as gv
from business.task_xyyb_theory import task_xyyb_theory
import sys
key_press_count = []
x  = int(0)
def on_press(key):
    if len(gv.HWND_CBTEXT) > 0:
        if key == keyboard.Key.ctrl_r:
            key_press_count.append(key)
            hwnd_task_str = gv.HWND_CBTEXT
            hwnd_task = hwnd_task_str.split(',')
            hwnd=hwnd_task[0]
            task=hwnd_task[1]
            print(key_press_count)
            if gv.TASK_XYYB == task:  # 判断是否为幸运硬币
                xyyb_theory = task_xyyb_theory(hwnd)
                xyyb_theory.app_exchange()

def on_release(key):
    pass

def listen():
    listener = keyboard.Listener(on_press, on_release)
    listener.start()



