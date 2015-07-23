from unittest import TestCase
from src.model.feed_list import FeedsList
from src.model.noticer import Noticer

import zhihu

__author__ = 'yuwei'

url = "http://www.zhihu.com/people/cai-tong"
class TestFeedsList(TestCase):
    def test_add_feeds(self):
        answers_urls = zhihu.Author.get_answers_urls(author_url=url)


