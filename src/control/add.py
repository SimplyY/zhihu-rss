__author__ = 'yuwei'


from src.util.my_pyqt import MyView, set_button, find_view
from src.model.noticer import Noticer
from src.util.error import UrlError


def record_add_info(root, sign_dialog, error_dialog):
    url_input = find_view(root, 'url_input')
    notice_method_spin = find_view(root, 'notice_method')
    is_remind_spin = find_view(root, 'is_remind')

    url = url_input.property("text")
    notice_method = notice_method_spin.property("value")
    is_remind = is_remind_spin.property("value")

    try:
        noticer = Noticer.init_noticer([url, notice_method, is_remind, None])
    except UrlError:
        error_dialog.set_error_info("添加失败。错误：主页url无效！")
        error_dialog.show()
        return

    Noticer.add_noticer(noticer)

    sign_dialog.close()


def show_add_dialog(my_app, qml, error_dialog):
    add_dialog = MyView(qml)
    add_dialog.show()
    print('a')
    set_button(add_dialog.root_content, 'button',
               lambda: record_add_info(add_dialog.root_content, add_dialog, error_dialog))




