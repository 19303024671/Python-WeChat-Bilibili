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
