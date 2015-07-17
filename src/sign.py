__author__ = 'yuwei'

from src.util.web_view import load_answer
from PyQt5.QtCore import QObject

from src.util.my_pyqt import MyView
import zhihu

def get_answers(url, url_input):
    try:
        answers = zhihu.Author(url).answers
    except Exception as e:
        url_input.remove(0, 100)
        url_input.insert(0, str(e))
        return None
    return answers


def record_sign_info(my_app, root, sign_dialog):
    email = root.findChild(QObject, 'email_input').getText(0, 100)
    password = root.findChild(QObject, 'password_input').getText(0, 100)
    url_input = root.findChild(QObject, 'url_input')
    url = url_input.getText(0, 100)

    answers = get_answers(url, url_input)
    answer = next(answers)

    load_answer(answer, my_app.web_view)

    print(email, password, url)

    if answers:
        sign_dialog.close()


def show_sign_dialog(my_app, qml):
    sign_dialog = MyView(qml)
    root = sign_dialog.root

    button = root.findChild(QObject, 'button')
    button.clicked.connect(lambda: record_sign_info(my_app, root, sign_dialog))

    sign_dialog.show()
