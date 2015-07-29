__author__ = 'yuwei'

from ..util.my_pyqt import use_qml_fun
from ..model.noticer import Noticer
from ..model.feeds_list import FeedsList


# 构造feedslists_processed
def set_noticers_data(noticers_names, unread_nums, feedslists_processed, noticers, feedslists):
    for noticer in noticers:
        for feedlists in feedslists:
            if feedlists.name == noticer.name:
                noticers_names.append(noticer.name)

                feeds = list()
                unread_num = 0

                for feed in feedlists.feeds:
                    # 根据不同的 noticer 的notice_method 筛选出相应的 feedslist
                    if feed["action_type"] in [notice_method.value for notice_method in noticer.notice_methods]:
                        feeds.append({"url": feed["url"], "action": feed["action"], "is_read": feed["is_read"]})
                        if not feed["is_read"]:
                            unread_num += 1

                unread_nums.append(unread_num)
                feedslists_processed.append({"name": noticer.name, "feeds": feeds})


def load_noticers_listview(root_view):
    noticers = Noticer.get_noticers_in_json()
    noticers_names = list()
    unread_nums = list()

    feedslists = FeedsList.get_feeds_lists_in_json()
    feedslists_processed = []

    set_noticers_data(noticers_names, unread_nums, feedslists_processed, noticers, feedslists)

    use_qml_fun(root_view, fun_parent_name="rect", fun_name="updateNoticersList",
                args={"names": noticers_names, "unread_nums": unread_nums, "feedslists": feedslists_processed})
