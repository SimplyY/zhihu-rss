__author__ = 'yuwei'
import zhihu
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
            self.feeds = list[2:]

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
        feeds = []
        feed = {"feed_url": None, "feed_action": None}

        latest_act_url = noticer.latest_act_url
        activitys = author.activities

        if not latest_act_url:  # add feeds_list
            for act in activitys:
                if act.type not in [zhihu.ActType.ANSWER_QUESTION, zhihu.ActType.PUBLISH_POST]:
                    break

                FeedsList._set_feed_word(feeds, feed, author, act)
        else:
            for act in activitys:
                if act.type not in [zhihu.ActType.ANSWER_QUESTION, zhihu.ActType.PUBLISH_POST]:
                    break
                if latest_act_url == act.content.url:
                    break

                FeedsList._set_feed_word(feeds, feed, author, act)
            feeds.extend(old_feeds_list)

        noticer.set_latest_act_url(feeds[0]["feed_url"])
        Noticer.add_noticer(noticer)
        return feeds

    @staticmethod
    def _set_feed_word(feeds, feed, author, act):
        FeedsList._set_feed_word_action(feed, author, act)
        feed["feed_url"] = act.content.url
        feeds.append(feed)

    @staticmethod
    def _set_feed_word_action(feed, author, act):

        if act.type == zhihu.ActType.ANSWER_QUESTION:
            feed["feed_action"] = ('%s 在 %s 回答了问题\n %s \n赞同数 %d'
                                   .format(author.name, act.time, act.answer.question.title,
                                           act.answer.upvote_num))
        elif act.type == zhihu.ActType.PUBLISH_POST:
            feed["feed_action"] = ('%s 在 %s 在专栏\n %s 中发布了文章\n %s，' %
                                   (author.name, act.time, act.post.column.name,
                                    act.post.title, act.post.upvote_num))

    @staticmethod
    def del_feeds_list():
        pass

    # save and load
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
