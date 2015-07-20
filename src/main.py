__author__ = 'yuwei'

from PyQt5.QtCore import QObject, QVariant, pyqtSlot, QVariant, QMetaObject, Q_ARG, Qt, Q_RETURN_ARG

from src.control import add, sign
from src.util.my_pyqt import MyApp, ErrorDialog, set_button
from src.util.const import MAIN_QML_DIR, SIGN_QML_DIR, ADD_QML_DIR
from src.model import noticer


def set_views():
    root_view = my_app.root_view

    set_button(root_view, 'sign_button', lambda: sign.show_sign_dialog(my_app, SIGN_QML_DIR))
    set_button(root_view, 'home_button')
    set_button(root_view, 'add_button', lambda: add.show_add_dialog(my_app, ADD_QML_DIR, ErrorDialog()))
    set_button(root_view, 'remind_button')

    my_app.web_view = root_view.findChild(QObject, 'web_view')
    my_app.noticers1_model = root_view.findChild(QObject, 'noticers1_model')
    load_listview()

def append_item(name):
    return {"name": name}

def load_listview():

    noticers1_names = [noticer1.name for noticer1 in noticer.Noticer.get_noticers(1)]

    q_noticers1_names = QVariant(noticers1_names)

    QMetaObject.invokeMethod(my_app.noticers1_model, "updateNoticersList", Qt.DirectConnection,
                             Q_ARG(QVariant, q_noticers1_names))

if __name__ == '__main__':
    my_app = MyApp(qml=MAIN_QML_DIR)

    set_views()

    MyApp.run(my_app)




