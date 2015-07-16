
def load_css(html):
    css = '<link href="https://raw.githubusercontent.com/SimplyY/save/master/github-markdown.css" ' \
          'rel="stylesheet"></link>'

    index = html.find('</head>')
    new_html = html[:index] + css + html[index:]
    return new_html


def load_answer(answer, web_view):

    html = answer.content
    new_html = load_css(html)

    web_view.loadHtml(new_html)

