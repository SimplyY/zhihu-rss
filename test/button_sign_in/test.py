__author__ = 'yuwei'

import os
from PyQt5.QtCore import QObject


from MyApp import MyApp, MyView


MAIN_QML_NAME = 'main.qml'
SIGN_QML_NAME = 'sign.qml'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIN_QML_DIR = os.path.join(BASE_DIR, MAIN_QML_NAME)


def record_sign_info(root, sign_dialog):
    email = root.findChild(QObject, 'email_input').getText(0, 100)
    password = root.findChild(QObject, 'password_input').getText(0, 100)
    url = root.findChild(QObject, 'url_input').getText(0, 100)

    print(email, password, url)
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
