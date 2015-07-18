__author__ = 'yuwei'


from PyQt5.QtCore import QObject

from src.util.my_pyqt import MyApp, ErrorDialog, set_button

from src.const import MAIN_QML_DIR, SIGN_QML_DIR, ADD_QML_DIR

def set_views(root_content):
    from src.control import add, sign

    set_button(root_content, 'sign_button', lambda: sign.show_sign_dialog(my_app, SIGN_QML_DIR))
    set_button(root_content, 'home_button')
    set_button(root_content, 'add_button', lambda: add.show_add_dialog(my_app, ADD_QML_DIR, error_dialog))
    set_button(root_content, 'remind_button')

    my_app.web_view = root_content.findChild(QObject, 'web_view')



if __name__ == '__main__':
    my_app = MyApp(qml=MAIN_QML_DIR)

    error_dialog = ErrorDialog()
    set_views(my_app.root_view)

    MyApp.show(my_app)
