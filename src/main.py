__author____author__ = 'yuwei'

from PyQt5.QtCore import QObject, QVariant

from src.control import add, sign
from src.util.my_pyqt import MyApp, set_button, use_qml_fun
from src.util.const import MAIN_QML_DIR, SIGN_QML_DIR, ADD_QML_DIR
from src.util.error import ErrorDialog
from src.model import noticer


def set_views():
    root_view = my_app.root_view

    set_button(root_view, 'sign_button', lambda: sign.show_sign_dialog(my_app, SIGN_QML_DIR))
    set_button(root_view, 'home_button')
    set_button(root_view, 'add_button', lambda: add.show_add_dialog(my_app, ADD_QML_DIR, ErrorDialog()))
    set_button(root_view, 'remind_button')

    my_app.web_view = root_view.findChild(QObject, 'web_view')
    my_app.noticers1_model = root_view.findChild(QObject, 'noticers1_model')
    my_app.noticers2_model = root_view.findChild(QObject, 'noticers2_model')
    load_listviews()


def load_listviews():
    noticers1_names = [noticer1.name for noticer1 in noticer.Noticer.get_noticers(1)]
    use_qml_fun(parent_view=my_app.noticers1_model, fun_name="updateNoticers1List", arg=noticers1_names)

    noticer2_names = [noticer2.name for noticer2 in noticer.Noticer.get_noticers(2)]

    use_qml_fun(parent_view=my_app.noticers2_model, fun_name="updateNoticers2List", arg=noticer2_names)


if __name__ == '__main__':
    my_app = MyApp(qml=MAIN_QML_DIR)

    set_views()

    MyApp.run(my_app)




