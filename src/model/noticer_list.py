__author__ = 'yuwei'

from PyQt5.QtCore import QAbstractListModel, QModelIndex

class NoticerList(QAbstractListModel):
    def __init__(self, noticers):
        QAbstractListModel.__init__(self)
        self.noticers = noticers

    def rowCount(self, parent=QModelIndex()):
        return len(self.noticers)

    def data(self, index):
        if index.isValid():
            return self.noticers[index.row()]
        return None


