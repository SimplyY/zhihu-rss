from .util.const import CSS_GITHUB_PATH

CSS = '<link href="' + CSS_GITHUB_PATH + '" rel="stylesheet"></link>'
def load_css(html):
    index = html.find('</head>')
    new_html = html[:index] + CSS + html[index:]
    return new_html


def load_answer(html, web_view):

    new_html = load_css(html)

    web_view.loadHtml(new_html)

