__author__ = 'yuwei'
from src.util import zhihu


class AnswerList:
    def __init__(self, noticer):
        self.url = noticer.url
        self.name = noticer.name
        self.answer_list = zhihu.An