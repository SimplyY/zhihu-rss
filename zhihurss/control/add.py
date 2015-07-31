__author__ = 'yuwei'

from PyQt5.QtCore import QObject, pyqtSignal, pyqtProperty

from ..util.my_pyqt import MyView, set_button, find_view, use_qml_fun
from ..util.error import UrlError
from ..util.my_thread import MyThread

from ..model.noticer import Noticer
from ..model.feeds_list import FeedsList
from . import listview


class AddedFeeds(QObject):

    def __init__(self):
        super(AddedFeeds, self).__init__()
        self.noticer = None
        self.max_feeds_num = int()
        self._getted_feeds_num = "0"
        self._is_end = False

    on_run = pyqtSignal()
    on_end = pyqtSignal()

    @pyqtProperty(str, notify=on_run)
    def getted_feeds_num(self):
        return self._getted_feeds_num

    def add_getted_feeds_num(self):
        temp = int(self._getted_feeds_num) + 1
        self._getted_feeds_num = str(temp)
        self.on_run.emit()

    @pyqtProperty(bool, notify=on_end)
    def is_end(self):
        return self._is_end

    def is_finish(self):
        self._is_end = True
        self.on_end.emit()


def record_add_info(my_app, add_dialog, error_dialog, added_feeds):

    root = add_dialog.root_view
    url_input = find_view(root, 'url_input')
    feed_num_input = find_view(root, 'feed_num_input')

    url = url_input.property("text")
    added_feeds.max_feeds_num = int(feed_num_input.property("text"))

    try:
        noticer = Noticer(url=url)
        added_feeds.noticer = noticer
    except UrlError:
        add_dialog.close()
        error_dialog.set_error_info("添加失败。错误：主页url无效！")
        error_dialog.show()

        return

    my_thread = MyThread("add_new_feedslist", add_new_feedslist, noticer, added_feeds)
    my_thread.start()


def add_new_feedslist(noticer, added_feeds):
    Noticer.add_noticer(noticer)
    FeedsList.add_feeds_list(noticer, added_feeds)


def quit_dialog(my_app, add_dialog, added_feeds):
    noticer = added_feeds.noticer
    use_qml_fun(my_app.root_view, fun_parent_name="rect", fun_name="add_new_feedslist",
                args={"feeds_list": FeedsList.get_feeds_list(noticer.name), "notice_methods": noticer.notice_methods})

    listview.load_noticers_listview(my_app.root_view)
    add_dialog.close()


def show_add_dialog(my_app, qml, error_dialog):
    add_dialog = MyView()

    added_feeds = AddedFeeds()
    add_dialog.root_context.setContextProperty("added_feeds", added_feeds)
    add_dialog.set_qml(qml)

    add_dialog.show()

    set_button(add_dialog.root_view, 'button_run',
               lambda: record_add_info(my_app, add_dialog, error_dialog, added_feeds))
    set_button(add_dialog.root_view, 'button_quit', lambda: quit_dialog(my_app, add_dialog, added_feeds))
