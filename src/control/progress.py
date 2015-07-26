__author__ = 'yuwei'

from src.util.const import PROGRESS_QML_DIR
from src.util.my_pyqt import MyView


def show_progress_dialog(name, amount_num):
    progress_dialog = MyView(PROGRESS_QML_DIR)
    progress_dialog.show()
    renew_noticer_data(progress_dialog.root_view, name, amount_num)
    return progress_dialog


def renew_noticer_data(root_view, name, amount_num):
    root_view.load_data({"name": name, "amount_num": amount_num})

def renew_feed_num(progress_dialog, feed_num):
    progress_dialog.root_view.load_feeds_num({"feeds_num": feed_num})
