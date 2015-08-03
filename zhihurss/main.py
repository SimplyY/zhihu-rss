#!/usr/bin/env python
__author__ = 'yuwei'

from PyQt5.QtCore import QObject

from .control import add, listview
from .control.change_notice_methods import show_change_dialog
from .control.update_feeds import spawn_update_thread

from .util.my_pyqt import MyApp, set_button, set_menu
from .util.const import MAIN_QML_PATH, ADD_QML_PATH, CHANGE_QML_PATH
from .util.error import ErrorDialog
from .util.config import set_config

from .model.noticer import Noticer
from .model.feeds_list import FeedsList


def set_is_read(url):
    feeds_lists = FeedsList.get_feeds_lists_in_json()
    for feeds_list in feeds_lists:
        for index, feed in enumerate(feeds_list.feeds):
            if feed["url"] == url:
                feeds_list.feeds[index]["is_read"] = True
                FeedsList.write_feeds_lists_in_json(feeds_lists)
                return


def del_noticer(root_view):
    Noticer.del_noticer(root_view)
    name = Noticer.get_current_noticer_name(root_view)
    FeedsList.del_feeds_list(name)

    listview.load_noticers_listview(root_view)


def set_views(my_app):
    root_view = my_app.root_view

    set_button(root_view, 'add_button', lambda: add.show_add_dialog(my_app, ADD_QML_PATH, ErrorDialog()))
    set_button(root_view, 'updateButton', lambda: listview.load_noticers_listview(root_view))

    set_menu(root_view, 'change_notice_method', lambda: show_change_dialog(my_app, CHANGE_QML_PATH))
    set_menu(root_view, 'delete_noticer', lambda: del_noticer(root_view))

    my_app.web_view = root_view.findChild(QObject, 'web_view')

    root_view.sendClicked.connect(set_is_read)

    listview.load_noticers_listview(root_view)


def run():

    _my_app = MyApp(qml=MAIN_QML_PATH)
    set_config(_my_app)
    set_views(_my_app)
    spawn_update_thread()

    return MyApp.run(_my_app)

if __name__ == '__main__':
    run()
