import zhihu
import MyApp

from PyQt5.QtCore import QObject


def load_css(html):
    css = '<link href="https://raw.githubusercontent.com/SimplyY/save/master/github-markdown.css" ' \
          'rel="stylesheet"></link>'

    index = html.find('</head>')
    new_html = html[:index] + css + html[index:]
    return new_html


def get_answer(root_item):
    url = 'http://www.zhihu.com/question/31862619/answer/53611303'
    answer = zhihu.Answer(url)

    html = answer.content
    new_html = load_css(html)

    web_view = root_item.findChild(QObject, 'web_view')
    web_view.loadHtml(new_html)


def set_view(root_view):
    button = root_view.findChild(QObject, 'button')
    button.clicked.connect(lambda: get_answer(root_view))


if __name__ == '__main__':
    my_app = MyApp(qml='test.qml')

    set_view(my_app.root_view)

    MyApp.show(my_app)
