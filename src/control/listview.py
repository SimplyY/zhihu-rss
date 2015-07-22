__author__ = 'yuwei'

from PyQt5.QtCore import QObject

from src.util.my_pyqt import use_qml_fun
from src.model.noticer import Noticer

def load_noticers_listview(my_app):
    load_listview(my_app, list_items=Noticer.get_noticers(1), fun_name="updateNoticers1List", fun_parent_name="rect")
    load_listview(my_app, list_items=Noticer.get_noticers(2), fun_name="updateNoticers2List", fun_parent_name="rect")


def load_content_list(my_app, name):
    pass
    # url = find


def load_listview(my_app, list_items, fun_name, fun_parent_name):
    parent_view = my_app.root_view.findChild(QObject, fun_parent_name)
    noticers_names = [noticer.name for noticer in list_items]
    use_qml_fun(parent_view=parent_view, fun_name=fun_name, args={"names": noticers_names})
