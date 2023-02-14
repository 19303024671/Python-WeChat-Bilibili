import time

from getmsg import get_msg
from sendmsg import send_msg
from getwnd import get_window


def main():
    wnd = get_window()
    msg_dir = get_msg()
    names = list(msg_dir)
    urls = list(msg_dir.values())
    for i in range(len(names)):
        msg = names[i] + ":" + urls[i]
        send_msg(wnd, msg)


if __name__ == '__main__':
    main()
