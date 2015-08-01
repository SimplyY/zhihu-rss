#!/usr/bin/env python

__author__ = 'yuwei'

import zhihu

from ..util.my_pyqt import MyView, set_button, find_view
from ..model.noticer import Noticer
from ..control.listview import load_noticers_listview


def _set_methods(root_view, new_notice_methods, checkbox_name, checkbox_value):
    is_checked = find_view(root_view, checkbox_name).property("checked")
    if is_checked:
        for act_type in zhihu.ActType:
            if act_type.value == checkbox_value:
                new_notice_methods.append(act_type)

def _set_noticer(my_app, new_notice_methods):
    name = Noticer.get_current_noticer_name(my_app.root_view)
    noticers = Noticer.get_noticers_in_json()

    for noticer in noticers:
        if noticer.name == name:
            noticer.set_notice_methods(new_notice_methods)
            Noticer.add_noticer(noticer)

    load_noticers_listview(my_app.root_view)


def change_notice_methods(my_app, change_dialog):
    root_view = change_dialog.root_view
    new_notice_methods = list()

    _set_methods(root_view, new_notice_methods, "checkBox1", 1)
    _set_methods(root_view, new_notice_methods, "checkBox2", 2)
    _set_methods(root_view, new_notice_methods, "checkBox3", 4)
    _set_methods(root_view, new_notice_methods, "checkBox4", 8)
    _set_methods(root_view, new_notice_methods, "checkBox5", 16)
    _set_methods(root_view, new_notice_methods, "checkBox6", 64)
    _set_methods(root_view, new_notice_methods, "checkBox7", 32)
    _set_methods(root_view, new_notice_methods, "checkBox8", 128)

    _set_noticer(my_app, new_notice_methods)

    change_dialog.close()


def set_notice_methods(my_app, change_dialog):
    new_notice_methods = [notice_method for notice_method in zhihu.ActType]
    _set_noticer(my_app, new_notice_methods)

    change_dialog.close()


def show_change_dialog(my_app, qml):
    change_dialog = MyView(qml)
    change_dialog.show()
    set_button(change_dialog.root_view, "button", lambda: change_notice_methods(my_app, change_dialog))
    set_button(change_dialog.root_view, "all_sel_button", lambda: set_notice_methods(my_app, change_dialog))
