__author__ = 'yuwei'

import sys

from PyQt5 import QtWebKit
from PyQt5.QtCore import QUrl, QObject, QVariant, QMetaObject, Q_ARG, Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQuick import QQuickView
from PyQt5.QtQml import QQmlApplicationEngine


# 在MyApp抽象了pyqt使用qml的过程

# 使用示例
# 见main.py

class MyApp(QObject):
    def __init__(self, qml, set_context=None):
        super().__init__()
        self.app = QApplication(sys.argv)

        self.engine = QQmlApplicationEngine(self)
        self.root_context = self.engine.rootContext()

        if set_context:
            set_context(self.root_context)

        self.engine.load(QUrl.fromLocalFile(qml))
        self.root_view = self.engine.rootObjects()[0]

    @staticmethod
    def run(my_app):
        my_app.root_view.show()
        return my_app.app.exec_()


class MyView(QQuickView):
    def __init__(self, qml=None):
        super().__init__()
        self.setResizeMode(QQuickView.SizeRootObjectToView)

        self.root_context = self.rootContext()

        if qml:
            self.set_qml(qml)

    def set_qml(self, qml):
        self.setSource(QUrl.fromLocalFile(qml))
        self.root_view = self.rootObject()


def find_view(parent_view, object_name):
    return parent_view.findChild(QObject, object_name)


def set_button(parent_view, object_name, function=None):
    button = find_view(parent_view, object_name)
    if function:
        button.clicked.connect(function)


def set_menu(parent_view, object_name, function=None):
    menu = find_view(parent_view, object_name)
    if function:
        menu.triggered.connect(function)


def use_qml_fun(root_view, fun_parent_name, fun_name, args):
    parent_view = root_view.findChild(QObject, fun_parent_name)
    q_arg = QVariant(args)
    QMetaObject.invokeMethod(parent_view, fun_name, Qt.DirectConnection, Q_ARG(QVariant, q_arg))
