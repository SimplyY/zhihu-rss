__author__ = 'yuwei'

import json
try:
    import zhihu
except ConnectionError:
    print("connect error")
#     TODO:


from src.util.error import UrlError
from src.util.const import NOTICERS_JSON_DIR

class Noticer:
    def __init__(self, url=None, noticer_list=None):
        if not noticer_list:  # 创建一个新的Noticer
            try:
                self.name = zhihu.Author(url).name
            except AttributeError:
                # TODO:create dialog
                raise UrlError
                return

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

    def __str__(self):
        return str(self.list)

    def set_latest_act_url(self, url):
        self.latest_act_url = url
        self.list[2] = url

    @staticmethod
    def add_noticer(noticer):
        noticers = Noticer.get_noticers_in_json()
        Noticer.write_noticers_in_json(noticer, noticers)

    @staticmethod
    def del_noticer():
        pass

    @staticmethod
    def get_noticers_in_json():
        noticers = []
        try:
            with open(NOTICERS_JSON_DIR, mode='r') as f:
                file = f.readlines()
                if not file:
                    return noticers

                data = json.loads(file[0])
                noticers = [Noticer(noticer_list=noticer_list) for noticer_list in data]

        except IOError:
            noticers = None

        return noticers

    @staticmethod
    def write_noticers_in_json(noticer, noticers):
        noticers = Noticer._get_new_noticers(noticer, noticers)

        json_data = json.dumps([noticer.list for noticer in noticers])
        with open(NOTICERS_JSON_DIR, mode='w') as f:
            f.write(json_data)

    @staticmethod
    def _get_new_noticers(noticer, noticers):
        if noticers:
            for index, the_noticer in enumerate(noticers):
                if noticer.url == the_noticer.url:
                    del noticers[index]
                    noticers.append(noticer)
                    return noticers
            noticers.append(noticer)
        else:
            noticers = [noticer]

        return noticers
