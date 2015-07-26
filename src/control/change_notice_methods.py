#!/usr/bin/env python

__author__ = 'yuwei'

import zhihu

from ..util.my_pyqt import MyView, set_button, find_view
from ..model.noticer import Noticer


def set_methods(root_view, new_notice_methods, checkbox_name, checkbox_value):
    is_checked = find_view(root_view, checkbox_name).property("checked")
    if is_checked:
        for act_type in zhihu.ActType:
            if act_type.value == checkbox_value:
                new_notice_methods.append(act_type)


def get_current_noticer_name(my_app):
    noticers_list_view = find_view(my_app.root_view, "noticers_list")
    noticers_model = find_view(my_app.root_view, "noticers1_model")

    current_index = noticers_list_view.property("currentIndex")
    return noticers_model.get(current_index).property("name")


def change_notice_methods(my_app, change_dialog):
    root_view = change_dialog.root_view
    new_notice_methods = list()

    set_methods(root_view, new_notice_methods, "checkBox1", 1)
    set_methods(root_view, new_notice_methods, "checkBox2", 2)
    set_methods(root_view, new_notice_methods, "checkBox3", 3)
    set_methods(root_view, new_notice_methods, "checkBox4", 4)
    set_methods(root_view, new_notice_methods, "checkBox5", 5)
    set_methods(root_view, new_notice_methods, "checkBox6", 6)
    set_methods(root_view, new_notice_methods, "checkBox7", 7)
    set_methods(root_view, new_notice_methods, "checkBox8", 8)

    name = get_current_noticer_name(my_app)

    noticers = Noticer.get_noticers_in_json()
    for noticer in noticers:
        if noticer.name == name:
            noticer.notice_methods = new_notice_methods

    change_dialog.close()


def show_change_dialog(my_app, qml):
    change_dialog = MyView(qml)
    change_dialog.show()
    set_button(change_dialog.root_view, "button", lambda: change_notice_methods(my_app, change_dialog))

