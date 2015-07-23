__author__ = 'yuwei'
from src.util import zhihu
import json

from src.model.noticer import Noticer
from src.util.const import FEEDS_JSON_DIR, MAX_FIRST_FEED_NUM

# 结构
# feedslists[
#     feedslist{
#         name
#         url
#         feeds{
#            url,
#            action
# }
#         list
#     }
# ]


class FeedsList:

    def __init__(self, noticer=None, old_feeds_list=None, list=None):
        if not list:
            self.url = noticer.url
            self.name = noticer.name

            author = zhihu.Author(self.url)

            if noticer.notice_method == 1:
                self.feeds = FeedsList.get_word_feeds(noticer, author, old_feeds_list)

            # elif noticer.notice_method == 2:
                # self.feeds = feeds = zhihu.Author(self.url).feeds

            self.list = [self.url, self.name]
            for feed in self.feeds:
                self.list.append(self.feeds[feed])
        else:
            self.url = list[0]
            self.name = list[1]
            self.list = list

    @staticmethod
    def renew_feeds_lists(noticers):
        # old_feeds_lists = FeedsList.get_feeds_lists_in_json()
        # new_feeds_lists = FeedsList.get_new_feeds_list(noticer, old_feeds_lists)
        pass

    @staticmethod
    def add_feeds_list(noticer):
        old_feeds_lists = FeedsList.get_feeds_lists_in_json()
        new_feeds_lists = FeedsList.get_new_feeds_list(noticer, old_feeds_lists)
        FeedsList.write_feeds_lists_in_json(new_feeds_lists)

    @staticmethod
    def get_new_feeds_list(noticers, old_feeds_lists):
        new_feeds_lists = []

        if noticers is not list:  # add feeds_list
            noticer = noticers

            feeds_list = FeedsList(noticer)

            old_feeds_lists.append(feeds_list)
            new_feeds_lists = old_feeds_lists
        else:  # renew feeds_lists
            for noticer in noticers:
                for old_feeds_list in old_feeds_lists:
                    if old_feeds_list.url == noticer.url:
                        break
            # TODO:

        return new_feeds_lists

    @staticmethod
    def get_word_feeds(noticer, author, old_feeds_list=None):
        answers = []
        # books = []
        latest_title = noticer.latest_title

        if not latest_title:  # add feeds_list
            answers = []
            for index, answer in enumerate(author.answers):
                if index < MAX_FIRST_FEED_NUM:
                    answers.append(answer)
                else:
                    break
            # books = [book.html for index, book in enumerate(author.books) if index < MAX_FIRST_FEED_NUM]
        else:
            # TODO: old_feeds_list
            for answer in author.answers:
                answers.append(answer)
                if answer.question.title == latest_title:
                    break
            # for index, book in enumerate(author.books):
            #     books.append(book)

        noticer.set_latest_title(answers[0].question.title)
        Noticer.add_noticer(noticer)
        feeds = {"answers_html": [answer.html for answer in answers]}
        return feeds

    @staticmethod
    def del_feeds_list():
        pass

    @staticmethod
    def write_feeds_lists_in_json(feeds_lists):
        data = [feeds_list.list for feeds_list in feeds_lists]

        json_data = json.dumps(data)
        with open(FEEDS_JSON_DIR, mode='w') as f:
            f.write(json_data)

    @staticmethod
    def get_feeds_lists_in_json():
        with open(FEEDS_JSON_DIR, mode='r') as f:
            json_data = f.read()

        data = json.loads(json_data)
        feeds_lists = [FeedsList(list=list) for list in data]
        return feeds_lists
