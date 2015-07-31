__author__ = 'yuwei'
import threading
import json
import os

try:
    import zhihu
except ConnectionError:
    print("connect error")
#     TODO:


from ..util.error import UrlError
from ..util.fs import ensure_dir
from ..util.const import NOTICERS_JSON_PATH
from ..util.my_pyqt import find_view


class Noticer:
    def __init__(self, url=None, noticer_list=None):
        if not noticer_list:  # 创建一个新的Noticer
            try:
                self.name = zhihu.Author(url).name
            except AttributeError:
                # TODO:create dialog
                raise UrlError
            except ValueError:
                raise UrlError

            self.notice_methods = [notice_method for notice_method in zhihu.ActType]
            notice_methods_in_json = [notice_method.value for notice_method in zhihu.ActType]
            self.url = url
            self.latest_act_url = None

        else:  # 从json里导入时
            self.url = noticer_list[0]
            notice_methods_in_json = noticer_list[1]
            self.latest_act_url = noticer_list[2]
            self.name = noticer_list[3]
            self.notice_methods = list()

            for act_type in zhihu.ActType:
                for notice_method in noticer_list[1]:
                    if act_type.value == notice_method:
                        self.notice_methods.append(act_type)

        self.list = [self.url, notice_methods_in_json, self.latest_act_url, self.name]

    noticers_json_lock = threading.RLock()

    def __str__(self):
        return str(self.list)

    def set_notice_methods(self, notice_methods):
        self.notice_methods = notice_methods
        self.list[1] = [notice_method.value for notice_method in notice_methods]

    def set_latest_act_url(self, url):
        self.latest_act_url = url
        self.list[2] = url

    @staticmethod
    def add_noticer(noticer):
        noticers = Noticer.get_noticers_in_json()
        Noticer.write_noticers_in_json(noticers, noticer)

    @staticmethod
    def del_noticer(root_view):
        name = Noticer.get_current_noticer_name(root_view)
        noticers = Noticer.get_noticers_in_json()

        for index, noticer in enumerate(noticers):
            if noticer.name == name:
                del noticers[index]

        Noticer.write_noticers_in_json(noticers)

    @staticmethod
    def get_current_noticer_name(root_view):
        name = find_view(root_view, "current_noticer_name").property("text")
        return name

    @staticmethod
    def get_noticers_in_json():
        with Noticer.noticers_json_lock:
            if not os.path.exists(NOTICERS_JSON_PATH):
                with open(NOTICERS_JSON_PATH, 'w'):
                    return []

            try:
                with open(NOTICERS_JSON_PATH, 'rb') as f:
                    file = f.read().decode('utf-8')
                    data = json.loads(file)
                    return [Noticer(noticer_list=noticer_list) for noticer_list in data]
            except FileNotFoundError:
                # TODO: log
                pass

        return []

    @staticmethod
    def write_noticers_in_json(noticers, new_noticer=None):
        if new_noticer:
            noticers = Noticer._get_new_noticers(new_noticer, noticers)

        json_data = json.dumps([noticer.list for noticer in noticers])

        with Noticer.noticers_json_lock:
            ensure_dir(NOTICERS_JSON_PATH)
            with open(NOTICERS_JSON_PATH, 'wb') as f:
                f.write(json_data.encode('utf-8'))

    @staticmethod
    def _get_new_noticers(noticer, noticers):
        if noticers:
            for index, the_noticer in enumerate(noticers):
                if noticer.url == the_noticer.url:
                    del noticers[index]
                    noticers.insert(index, noticer)
                    return noticers
            noticers.insert(0, noticer)
        else:
            noticers = [noticer]

        return noticers
