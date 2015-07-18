__author__ = 'yuwei'

import json
from src.main import NOTICERS_DIR


class Noticer:

    def __init__(self, url, notice_method, is_remind, latest_answer_title):
        self.url = url
        self.notice_method = notice_method
        self.is_remind = is_remind
        self.latest_answer_title = latest_answer_title
        self.list = [self.url, self.notice_method, self.is_remind, self.latest_answer_title]

    def __str__(self):
        return str(self.list)

    @staticmethod
    def init_noticer(noticer_list):
        return Noticer(noticer_list[0], noticer_list[1], noticer_list[2], noticer_list[3])

    @staticmethod
    def add_noticer(noticer):
        noticers = Noticer.get_noticers_in_json()

        Noticer.write_noticers_in_json(noticer, noticers)

    @staticmethod
    def get_noticers_in_json():
        noticers = []
        try:
            with open(NOTICERS_DIR, mode='r') as f:
                file = f.readlines()
                if not file:
                    return noticers

                data = json.loads(file[0])
                noticers = [Noticer.init_noticer(noticer_data) for noticer_data in data]

        except IOError:
            assert "can't find NOTICERS_FILE"

        return noticers

    @staticmethod
    def write_noticers_in_json(noticer, noticers):
        if noticers:
            for index, the_noticer in enumerate(noticers):
                if noticer.url == the_noticer.url:
                    del noticers[index]
                    noticers.append(noticer)
                    break
                else:
                    noticers.append(noticer)
        else:
            noticers = [noticer]

        json_data = json.dumps([noticer.list for noticer in noticers])

        with open(NOTICERS_DIR, mode='w') as f:
            f.write(json_data)

