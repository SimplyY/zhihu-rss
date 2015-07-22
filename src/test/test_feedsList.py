from unittest import TestCase
from src.model.feed_list import FeedsList
from src.model.noticer import Noticer

__author__ = 'yuwei'


class TestFeedsList(TestCase):
    def test_add_feeds(self):
        noticer = Noticer(url="http://www.zhihu.com/people/cai-tong",
                          notice_method=1, is_remind=0)
        FeedsList.add_feeds_list(noticer)
