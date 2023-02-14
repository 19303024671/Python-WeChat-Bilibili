# Bilibili热门信息爬取与微信自动推送

## 简介：

### 该项目使用Python语言实现以下内容：

1.爬取bilibili网站热门视频信息（目前包括视频名称，视频地址）；

![bilibili.png](https://res.craft.do/user/full/3136d9b0-de94-a82b-edbe-70f1d555ae42/doc/a2348cdc-7406-4aad-93f4-80dd64b8a22e/2cc02acf-99df-47d2-bc24-29a41711f3be)

2.自动使用微信软件将爬取到的内容分条发送到指定好友（目前是文件传输助手）。

![WeChat.png](https://res.craft.do/user/full/3136d9b0-de94-a82b-edbe-70f1d555ae42/doc/a2348cdc-7406-4aad-93f4-80dd64b8a22e/8a893c49-f63b-4b19-962e-ec26599a5025)

---

## 实现原理：

### 爬取原理：

1.借助selenium模块实现动态页面的爬取；

2.xpath解析页面，获取信息；

3.存成msg_dir字典，并返回、

### 自动发送微信信息原理：

1.导入 win32gui模块，通过微信PC端窗口的类名与窗口名获取到窗口句柄；

2.借助pywinauto.keyboard模块中的 send_keys方法实现将字符串以及控制字符（回车）发送到指定窗口；

3.进而自动发送信息。

---

## 代码文件说明：

1. ### [main.py](https://github.com/19303024671/Python-WeChat-Bilibili/blob/main/main.py)

说明：程序入口，可以直接运行

代码：

```javascript
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
```

2. ### [edge.py](https://github.com/19303024671/Python-WeChat-Bilibili/blob/main/edge.py)

说明：selenium模块的加工，可以直接返回不易被浏览器察觉的自动化对象

代码：

```javascript
from selenium import webdriver


def create_edge_driver(*, headless=False):
    options = webdriver.EdgeOptions()
    if headless:
        options.add_argument('--headless')
    options.add_argument("--disable-blink-features")
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    browser = webdriver.Edge(options=options)
    browser.execute_cdp_cmd(
        'Page.addScriptToEvaluateOnNewDocument',
        {'source': 'Object.defineProperty(navigator,"webdriver",{get:() => undefined})'}
    )
    return browser


if __name__ == '__main__':
    b = create_edge_driver()
    b.get('https://max.book118.com/html/2018/1025/8060051030001130.shtm')
```

3. ### [getwnd.py](https://github.com/19303024671/Python-WeChat-Bilibili/blob/main/getwnd.py)

说明：获取微信信息发送窗口的句柄，主要使用该文件内的get_window()方法

代码：

```javascript
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
```

4. ### [getmsg.py](https://github.com/19303024671/Python-WeChat-Bilibili/blob/main/getmsg.py)

说明：爬取bilibili网站信息的文件，文件中的get_msg()方法返回爬取到的信息的字典

代码：

```javascript
from edge import create_edge_driver
from lxml import etree


def get_msg():
    msg_dir = {}
    browser = create_edge_driver(headless=True)

    browser.get("https://www.bilibili.com/")

    page = browser.page_source
    html = etree.HTML(page)
    div_list = html.xpath("/html/body/div[2]/div[2]/main/div[2]/div/div[1]/div")
    for div in div_list:
        try:
            video_url = div.xpath("./div/div[2]/div/div/h3/a/@href")[0]
            name = div.xpath("./div/div[2]/div/div/h3/a/text()")[0]
            msg_dir.update({name: video_url})
        except:
            continue
        # /html/body/div[2]/div[2]/main/div[2]/div/div[1]/div[2]/div/div[2]"
        # /html/body/div[2]/div[2]/main/div[2]/div/div[1]/div[1]
        # /html/body/div[2]/div[2]/main/div[2]/div/div[1]/div[2]/div/div[2]/div/div/h3/a
        # /html/body/div[2]/div[2]/main/div[2]/div/div[1]/div[2]/div/div[2]/div/div/h3/a"
    return msg_dir


if __name__ == '__main__':
    print(get_msg())
```

5. ### [sendmsg.py](https://github.com/19303024671/Python-WeChat-Bilibili/blob/main/sendmsg.py)

说明：发送微信信息的文件，使用文件中的send_msg()方法发送指定一条信息

代码：

```javascript
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
```

---

## 联系我：粤地小蜜蜂

我的邮箱：QQ邮箱

CSDN主页：[CSDN](https://blog.csdn.net/m0_67194505?type=blog)

GitHub主页：[GitHub](https://github.com/19303024671)

?descriptionFromFileType=function+toLocaleUpperCase()+{+[native+code]+}+File&mimeType=application/octet-stream&fileName=Bilibili热门信息爬取与微信自动推送.md&fileType=undefined&fileExtension=md
