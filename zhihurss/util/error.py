__author__ = 'yuwei'

from .my_pyqt import MyView, find_view
from .const import ERROR_QML_PATH

class UrlError(Exception):
    pass


class ErrorDialog(MyView):
    def __init__(self):
        super().__init__(ERROR_QML_PATH)

    def set_error_info(self, error_info):
        text = find_view(self.root_view, 'errorInfoText')
        text.setProperty('text', error_info)
