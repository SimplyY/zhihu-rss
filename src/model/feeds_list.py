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
#         feeds[{
#            url,
#            action
# }]
#         list
#     }
# ]


class FeedsList:
    def __init__(self, noticer=None, old_feeds_list=None, list=None):
        if not list:
            self.url = noticer.url
            self.name = noticer.name

            author = zhihu.Author(self.url)

            self.feeds = FeedsList.get_feeds(noticer, author, old_feeds_list)

            self.list = [self.url, self.name]
            self.list.extend(self.feeds)
        else:
            self.url = list[0]
            self.name = list[1]
            self.list = list
            self.feeds = list[2:]

    def get_dict(self):
        return {"url": self.url, "name": self.name, "feeds": self.feeds}

    @staticmethod
    def get_feeds_list(name):
        feeds_lists = FeedsList.get_feeds_lists_in_json()
        for feeds_list in feeds_lists:
            if feeds_list.name == name:
                return feeds_list.get_dict()
        raise "can't get a feedslist whose name is arg name"

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

            if noticer.name in [feeds_list.name for feeds_list in old_feeds_lists]:
                return old_feeds_lists

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
    def get_feeds(noticer, author, old_feeds_list=None):
        feeds = []

        latest_act_url = noticer.latest_act_url
        activities = author.activities

        for act in activities:
            # 两个截止遍历的条件
            if latest_act_url and latest_act_url == act.content.url:
                break
            if MAX_FIRST_FEED_NUM == len(feeds):
                break

            feed = FeedsList._create_feed(author, act, noticer)
            if feed:
                feeds.append(feed)

        if old_feeds_list:
            feeds.extend(old_feeds_list)

        noticer.set_latest_act_url(feeds[0]["url"])
        Noticer.add_noticer(noticer)
        return feeds

    @staticmethod
    def _create_feed(author, act, noticer):
        if noticer.notice_method == 1 and act.type not in [zhihu.ActType.ANSWER_QUESTION, zhihu.ActType.PUBLISH_POST]:
            return None

        feed = {"url": None, "action": None}

        FeedsList._set_feed_word_action(feed, author, act)
        feed["url"] = act.content.url

        return feed

    @staticmethod
    def _set_feed_word_action(feed, author, act):

        if act.type == zhihu.ActType.ANSWER_QUESTION:
            feed["action"] = ('{} 在 {} 回答了问题\n{} \n赞同数 {}'.format(author.name, str(act.time).split(" ")[0],
                                                                        act.answer.question.title,
                                                                        act.answer.upvote_num))
        elif act.type == zhihu.ActType.PUBLISH_POST:
            feed["action"] = ('{} 在 {} 在专栏\n {} 中发布了文章\n {}'.format(author.name, act.time,
                                                                          act.post.column.name, act.post.title,
                                                                              act.post.upvote_num))

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
        if not json_data:
            return []

        data = json.loads(json_data)
        feeds_lists = [FeedsList(list=feeds_list) for feeds_list in data]
        return feeds_lists
