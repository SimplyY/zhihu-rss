__author__ = 'yuwei'


from src.util.my_pyqt import MyView, set_button, find_view

def record_add_info(root, sign_dialog):
    url_input = find_view(root, 'url_input')
    notice_method_spin = find_view(root, 'notice_method')
    is_remind_spin = find_view(root, 'is_remind')

    url = url_input.property("text")
    notice_method = notice_method_spin.property("value")
    is_remind = is_remind_spin.property("value")

    sign_dialog.close()
    print(url, notice_method, is_remind)


def show_add_dialog(my_app, qml):
    add_dialog = MyView(qml)
    print('a')
    set_button(add_dialog.root, 'button',
               lambda: record_add_info(add_dialog.root, add_dialog))




