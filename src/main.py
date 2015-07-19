__author__ = 'yuwei'

from PyQt5.QtCore import QObject

from src.control import add, sign
from src.util.my_pyqt import MyApp, ErrorDialog, set_button
from src.util.const import MAIN_QML_DIR, SIGN_QML_DIR, ADD_QML_DIR
from src.model import noticer


def set_views(root_context):
    set_button(root_context, 'sign_button', lambda: sign.show_sign_dialog(my_app, SIGN_QML_DIR))
    set_button(root_context, 'home_button')
    set_button(root_context, 'add_button', lambda: add.show_add_dialog(my_app, ADD_QML_DIR, ErrorDialog()))
    set_button(root_context, 'remind_button')

    my_app.web_view = root_context.findChild(QObject, 'web_view')


def load_listview(root_context):
    noticers1_names = [noticer1.name for noticer1 in noticer.Noticer.get_noticers(1)]

    root_context.setContextProperty('noticers1_names', noticers1_names)
    root_context.setContextProperty('noticers1_length', len(noticers1_names))
    print(len(noticers1_names), noticers1_names[0])


if __name__ == '__main__':
    my_app = MyApp(qml=MAIN_QML_DIR, set_content=load_listview)

    set_views(my_app.root_view)

    MyApp.run(my_app)




