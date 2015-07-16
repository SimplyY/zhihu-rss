__author__ = 'yuwei'

import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQuick import QQuickView


# 在MyApp抽象了pyqt使用qml的过程
class MyApp:
    def __init__(self, qml):
        self.app = QApplication(sys.argv)

        self.viewer = QQuickView()
        self.viewer.setResizeMode(QQuickView.SizeRootObjectToView)
        self.viewer.setSource(QUrl(qml))

    @staticmethod
    def show(app):
        app.viewer.show()
        app.app.exec_()
        sys.exit()
