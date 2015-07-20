__author__ = 'yuwei'

from .my_pyqt import MyView, find_view

class UrlError(Exception):
    pass


class ErrorDialog(MyView):
    def __init__(self):
        from src.util.const import ERROR_QML_DIR
        super().__init__(ERROR_QML_DIR)

    def set_error_info(self, error_info):
        text = find_view(self.root_content, 'errorInfoText')
        text.setProperty('text', error_info)
