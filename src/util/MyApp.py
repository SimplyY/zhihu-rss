__author__ = 'yuwei'

import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQuick import QQuickView


# 在MyApp抽象了pyqt使用qml的过程

# 使用示例
# import MyApp
#
# def set_view(root_view):
#     button = root_view.findChild(QObject, 'button')
#     button.clicked.connect(lambda: load_answer(root_view))
#
# if __name__ == '__main__':
#     my_app = MyApp(qml='test.qml')
#
#     set_view(my_app.root_view)
#
#     MyApp.show(my_app)

class MyApp:
    def __init__(self, qml):
        self.app = QApplication(sys.argv)
        self.view = MyView(qml)

        self.root_view = self.view.root

    @staticmethod
    def show(my_app):
        my_app.view.show()
        my_app.app.exec_()
        sys.exit()


class MyView(QQuickView):
    def __init__(self, qml):
        super().__init__()
        self.setResizeMode(QQuickView.SizeRootObjectToView)
        self.setSource(QUrl(qml))
        self.root = self.rootObject()
