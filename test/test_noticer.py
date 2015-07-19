from unittest import TestCase

from src.model.noticer import Noticer

__author__ = 'yuwei'


class TestNoticer(TestCase):
    # def test_get_noticers_in_json(self):
    #     noticer = Noticer('d', 'd', 'r', 'f')
    #
    #     noticers_items = Noticer.get_noticers_in_json()
    #
    #     for noticer in noticers_items:
    #         print(noticer)
    #     print(len(noticers_items))
    #
    #     Noticer.write_noticers_in_json(noticer, noticers_items)

    def test_get_noticer(self):
        noticer = Noticer.get_noticers(0)
