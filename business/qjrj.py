from pynput import keyboard
import utils.global_variable as gcb

def on_press(key):
    if key == keyboard.Key.ctrl_r:
        # if key == keyboard.Key.ctrl_l and key == keyboard.Key.alt_l and key == keyboard.KeyCode.from_char('h'):
        print("你按下了 Ctrl,窗口任务："+ gcb.HWND_CBTEXT)

def on_release(key):
    pass

def listen():
    listener = keyboard.Listener(on_press, on_release)
    listener.start()