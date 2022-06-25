import pdfkit
import requests
from bs4 import BeautifulSoup	

def get_content_and_next_url(content): # content 为网页内容
    soup = BeautifulSoup(content)	 # 得到文档的对象

    with open('1.html', 'wb') as f:
        f.write(bytes(soup.prettify(),'UTF-8'))

    # 获取链接和销毁不必要元素
    navbar = soup.select('.navbar')
    if len(navbar):
        navbar[0].decompose()

    sidebar = soup.select('.sidebar')
    if len(sidebar):
        sidebar[0].decompose()

    page_edit = soup.select('.page-edit')
    if len(page_edit):
        page_edit[0].decompose()

    # 注意下一页链接在底部导航栏元素中,
    # 要先获取链接后,才能销毁元素,顺序不能颠倒
    next_span = soup.select(".next")
    if len(next_span):
        next_span_href = next_span[0].a['href']
    else:
        next_span_href = None

    page_meta = soup.select('.page-meta')
    if len(page_meta):
        page_meta[0].decompose()

    page_nav = soup.select('.page-nav')
    if len(page_nav):
        page_nav[0].decompose()

    with open('2.html', 'wb') as f:
        f.write(bytes(soup.prettify(),'UTF-8'))

req = requests.get('http://192.168.0.51:8892/guide/')

content = get_content_and_next_url(req.content)

pdfkit.from_file(["2.html"], 'out.pdf', configuration=pdfkit.configuration(wkhtmltopdf="D:/lib/wkhtmltopdf/bin/wkhtmltopdf.exe"))



