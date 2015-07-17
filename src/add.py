__author__ = 'yuwei'


from src.util.my_pyqt import MyView, set_button, find_view
from src.util import my_json


# 增加noticer
def set_noticers(new_data, notice_method, is_remind):


# TODO 返回新的关注者datas
# def get_new_noticers_datas(new_data, old_datas):
#
#     url = new_data[0]
#     if new_data not in old_datas:
#         if url not in [data[0] for data in old_datas]: # 禁止添加重复的urls
#             new_data.append((new_data, None))
#         else:
#             pass
#
#
#     return datas



def record_add_info(root, sign_dialog):
    url_input = find_view(root, 'url_input')
    notice_method_spin = find_view(root, 'notice_method')
    is_remind_spin = find_view(root, 'is_remind')

    url = url_input.property("text")
    notice_method = notice_method_spin.property("value")
    is_remind = is_remind_spin.property("value")

    sign_dialog.close()

    new_data = [url, notice_method, is_remind, None]
    set_noticers(new_data, notice_method, is_remind)


def show_add_dialog(my_app, qml):
    add_dialog = MyView(qml)
    print('a')
    set_button(add_dialog.root, 'button',
               lambda: record_add_info(add_dialog.root, add_dialog))




