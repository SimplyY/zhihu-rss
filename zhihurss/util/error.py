__author__ = 'yuwei'

from .my_pyqt import MyView, find_view

class UrlError(Exception):
    pass


class ErrorDialog(MyView):
    def __init__(self):
        from .util.const import ERROR_QML_PATH
        super().__init__(ERROR_QML_PATH)

    def set_error_info(self, error_info):
        text = find_view(self.root_view, 'errorInfoText')
        text.setProperty('text', error_info)
