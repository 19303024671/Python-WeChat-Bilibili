import time

import win32con
import win32gui
from pywinauto.keyboard import send_keys


def send_msg(hwnd, msg):
    win32gui.SetForegroundWindow(hwnd)
    time.sleep(0.5)
    send_keys(msg)
    # 模拟键盘输入enter
    send_keys("{VK_RETURN}")


if __name__ == '__main__':
    from getwnd import get_window

    wnd = get_window()
    send_msg(wnd, "123")
