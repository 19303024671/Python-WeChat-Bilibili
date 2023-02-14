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
