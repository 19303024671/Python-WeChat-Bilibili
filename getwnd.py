import sys
import win32gui
import win32con


def get_all_windows():
    hWnd_list = []
    win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWnd_list)
    # print(hWnd_list)
    return hWnd_list


def get_title(hwnd):
    title = win32gui.GetWindowText(hwnd)
    # print('窗口标题:%s' % title)
    return title


def get_clasname(hwnd):
    clasname = win32gui.GetClassName(hwnd)
    # print('窗口类名:%s' % clasname)
    return clasname


def get_window():
    for wnd in get_all_windows():
        # 003C051A
        if get_title(wnd) == "微信":
            if get_clasname(wnd) == "WeChatMainWndForPC":
                return wnd



