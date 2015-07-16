__author__ = 'yuwei'

import os

from PyQt5.QtCore import QObject
import zhihu

from .util.MyApp import MyView
from .util import MyApp
from .util.web_view import load_answer

MAIN_QML_NAME = 'main.qml'
SIGN_QML_NAME = 'sign.qml'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIN_QML_DIR = os.path.join(BASE_DIR, MAIN_QML_NAME)


def get_answers(url, url_input):
    try:
        answers = zhihu.Author(url).answers
    except Exception as e:
        url_input.remove(0, 100)
        url_input.insert(0, str(e))
        return None
    return answers



def record_sign_info(root, sign_dialog):
    email = root.findChild(QObject, 'email_input').getText(0, 100)
    password = root.findChild(QObject, 'password_input').getText(0, 100)
    url_input = root.findChild(QObject, 'url_input')
    url = url_input.getText(0, 100)

    answers = get_answers(url, url_input)
    answer = next(answers)

    load_answer()

    print(email, password, url)

    if answers:
        sign_dialog.close()


def show_sign_dialog():
    sign_dialog = MyView(SIGN_QML_NAME)
    root = sign_dialog.root

    button = root.findChild(QObject, 'button')
    button.clicked.connect(lambda: record_sign_info(root, sign_dialog))

    sign_dialog.show()


def set_view(root_view):
    button = root_view.findChild(QObject, 'sign_button')
    button.clicked.connect(show_sign_dialog)


if __name__ == '__main__':

    my_app = MyApp(qml=MAIN_QML_DIR)

    set_view(my_app.root_view)

    MyApp.show(my_app)
