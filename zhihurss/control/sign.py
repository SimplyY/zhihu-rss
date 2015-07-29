__author__ = 'yuwei'

from zhihurss.util.web_view import load_answer

from zhihurss.util.my_pyqt import MyView, set_button, find_view
import zhihu

def get_answers(url, url_input):
    try:
        answers = zhihu.Author(url).answers
    except Exception as e:
        url_input.remove(0, 100)
        url_input.insert(0, str(e))
        return None
    return answers


def record_sign_info(my_app, root, sign_dialog):
    email_input = find_view(root, 'email_input')
    password_input = find_view(root, 'password_input')
    url_input = find_view(root, 'url_input')

    # TODO: set email and password
    email = email_input.property("text")
    password = password_input.property("text")
    url = url_input.property("text")

    answers = get_answers(url, url_input)
    answer = next(answers)

    load_answer(answer.html, my_app.web_view)

    if answers:
        sign_dialog.close()


def show_sign_dialog(my_app, qml):
    sign_dialog = MyView(qml)
    sign_dialog.show()

    set_button(sign_dialog.root_view, 'button',
               lambda: record_sign_info(my_app, sign_dialog.root_view, sign_dialog))



