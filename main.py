
import time
import business.rcd as rcd

if __name__ == "__main__":
    time.sleep(3)
    hwnd = rcd.gtwh.get_Hwnd()
    rcd.recording(hwnd)
