__author__ = 'yuwei'

import sys
from PyQt5.QtCore import QUrl, QObject
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQuick import QQuickView
from PyQt5.QtQml import QQmlApplicationEngine

# 在MyApp抽象了pyqt使用qml的过程

# 使用示例
# import MyApp
#
# def set_views(root_view):
#     button = root_view.findChild(QObject, 'button')
#     button.clicked.connect(lambda: load_answer(root_view))
#
# if __name__ == '__main__':
#     my_app = MyApp(qml='test.qml')
#
#     set_views(my_app.root_view)
#
#     MyApp.show(my_app)

class MyApp(QObject):
    def __init__(self, qml):
        super().__init__()

        self.app = QApplication(sys.argv)

        self.engine = QQmlApplicationEngine(self)
        self.engine.load(QUrl(qml))
        self.root_view = self.engine.rootObjects()[0]

    @staticmethod
    def show(my_app):
        my_app.root_view.show()
        my_app.app.exec_()
        sys.exit()


class MyView(QQuickView):
    def __init__(self, qml):
        super().__init__()
        self.setResizeMode(QQuickView.SizeRootObjectToView)
        self.setSource(QUrl(qml))
        self.root_content = self.rootObject()


def find_view(parent_view, object_name):
    return parent_view.findChild(QObject, object_name)


def set_button(parent_view, object_name, function=None):
    button = find_view(parent_view, object_name)
    if function:
        button.clicked.connect(function)


class ErrorDialog(MyView):
    def __init__(self):
        from src.const import ERROR_QML_DIR
        super().__init__(ERROR_QML_DIR)

    def set_error_info(self, error_info):
        text = find_view(self.root_content, 'errorInfoText')
        text.setProperty('text', error_info)

