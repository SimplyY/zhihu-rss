__author__ = 'yuwei'

import os

from PyQt5.QtCore import QObject
from src.util.my_pyqt import MyApp, set_button

from src import sign, add

MAIN_QML_NAME = 'main.qml'
SIGN_QML_NAME = 'sign.qml'
ADD_QML_NAME = 'add.qml'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIN_QML_DIR = os.path.join(BASE_DIR, 'src', 'qml', MAIN_QML_NAME)
SIGN_QML_DIR = os.path.join(BASE_DIR, 'src', 'qml', SIGN_QML_NAME)
ADD_QML_DIR = os.path.join(BASE_DIR, 'src', 'qml', ADD_QML_NAME)


def set_views(root_view):

    set_button(root_view, 'sign_button', lambda: sign.show_sign_dialog(my_app, SIGN_QML_DIR))
    set_button(root_view, 'home_button', lambda: add.show_add_dialog(my_app, ADD_QML_DIR))
    set_button(root_view, 'add_button')
    set_button(root_view, 'remind_button')

    my_app.web_view = root_view.findChild(QObject, 'web_view')


if __name__ == '__main__':
    print(MAIN_QML_DIR)
    my_app = MyApp(qml=MAIN_QML_DIR)

    set_views(my_app.root_view)

    MyApp.show(my_app)
