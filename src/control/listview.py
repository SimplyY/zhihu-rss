__author__ = 'yuwei'


from src.util.my_pyqt import use_qml_fun
from src.model.noticer import Noticer
from src.model.feeds_list import FeedsList

def load_listviews(root_view):
    load_notice_listview(root_view, list_items=Noticer.get_noticers_in_json(),
                         fun_name="updateNoticersList", fun_parent_name="rect")


def load_notice_listview(root_view, list_items, fun_name, fun_parent_name):
    noticers_names = [noticer.name for noticer in list_items]
    feedslists = FeedsList.get_feeds_lists_in_json()
    feedslists_sorted = []

    for name in noticers_names:
        for feedlists in feedslists:
            if feedlists.name == name:
                feedslists_sorted.append(feedlists.get_dict())

    use_qml_fun(root_view, fun_parent_name=fun_parent_name, fun_name=fun_name,
                args={"names": noticers_names, "feedslists": feedslists_sorted})
