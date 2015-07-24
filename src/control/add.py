__author__ = 'yuwei'


from src.util.my_pyqt import MyView, set_button, find_view, use_qml_fun
from src.util.error import UrlError
from src.util.my_thread import MyThread

from src.model.noticer import Noticer
from src.model.feeds_list import FeedsList
from src.control import listview


def record_add_info(my_app, add_dialog, error_dialog):
    root = add_dialog.root_view
    url_input = find_view(root, 'url_input')
    notice_method_spin = find_view(root, 'notice_method')
    is_remind_spin = find_view(root, 'is_remind')

    url = url_input.property("text")
    notice_method = notice_method_spin.property("value")
    is_remind = is_remind_spin.property("value")

    add_dialog.close()

    try:
        noticer = Noticer.init_noticer([url, notice_method, is_remind, None])
    except UrlError:
        error_dialog.set_error_info("添加失败。错误：主页url无效！")
        error_dialog.show()
        return
    add_new_feedslist(my_app, noticer)
    # my_thread = MyThread("add_new_feedslist", add_new_feedslist, my_app, noticer)
    # my_thread.start()

def add_new_feedslist(my_app, noticer):
    Noticer.add_noticer(noticer)
    FeedsList.add_feeds_list(noticer)

    use_qml_fun(my_app, fun_parent_name="rect", fun_name="add_new_feedslist",
                args={"feeds_list": FeedsList.get_feeds_list(noticer.name), "notice_method": noticer.notice_method})

    listview.load_listviews(my_app)



def show_add_dialog(my_app, qml, error_dialog):
    add_dialog = MyView(qml)
    add_dialog.show()
    set_button(add_dialog.root_view, 'button',
               lambda: record_add_info(my_app, add_dialog, error_dialog))




