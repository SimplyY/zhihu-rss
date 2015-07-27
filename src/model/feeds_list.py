__author__ = 'yuwei'
import zhihu
import json
import os

from src.model.noticer import Noticer
from src.util.const import FEEDS_JSON_DIR
from src.control import progress

# 结构
# feedslists[
#     feedslist{
#         name
#         url
#         feeds[{
#            url,
#            action_type,
#            action
# }]
#         list
#     }
# ]


class FeedsList:
    def __init__(self, feed_num=100, noticer=None, old_feeds_list=None, list=None, progress_dialog=None):
        if not list:
            self.url = noticer.url
            self.name = noticer.name

            author = zhihu.Author(self.url)

            self.feeds = FeedsList.get_feeds(noticer, author, feed_num, old_feeds_list, progress_dialog=progress_dialog)

            self.list = [self.url, self.name]
            self.list.append(self.feeds)
        else:
            self.url = list[0]
            self.name = list[1]
            self.list = list
            self.feeds = list[2]

    def get_dict(self):
        return {"url": self.url, "name": self.name, "feeds": self.feeds}

    def get_unread_num(self):
        num = 0
        for feed in self.feeds:
            if not feed["is_read"]:
                num += 1
        return num

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
    def add_feeds_list(noticer, feed_num, progress_dialog=None):
        old_feeds_lists = FeedsList.get_feeds_lists_in_json()
        new_feeds_lists = FeedsList.get_new_feeds_list(noticer, feed_num, old_feeds_lists, progress_dialog=progress_dialog)
        FeedsList.write_feeds_lists_in_json(new_feeds_lists)

    @staticmethod
    def get_new_feeds_list(noticers, feed_num, old_feeds_lists, progress_dialog=None):
        new_feeds_lists = []

        if noticers is not list:  # add feeds_list
            noticer = noticers

            if noticer.name in [feeds_list.name for feeds_list in old_feeds_lists]:
                return old_feeds_lists

            feeds_list = FeedsList(noticer=noticer, feed_num=feed_num, progress_dialog=progress_dialog)

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
    def get_feeds(noticer, author, amount_num, old_feeds_list=None, progress_dialog=None):
        feeds = []
        latest_act_url = noticer.latest_act_url
        activities = author.activities

        for act in activities:
            # 两个截止遍历的条件
            if latest_act_url and latest_act_url == act.content.url:
                break
            if int(amount_num) == len(feeds):
                break

            feed = FeedsList._create_feed(author, act)
            feeds.append(feed)

            # feed_num += 1
            # progress.renew_feed_num(progress_dialog, feed_num)

        if old_feeds_list:
            feeds.extend(old_feeds_list)

        # progress_dialog.close()
        noticer.set_latest_act_url(feeds[0]["url"])
        Noticer.add_noticer(noticer)
        return feeds

    @staticmethod
    def _create_feed(author, act):
        feed = dict()

        feed["is_read"] = False
        feed["action"] = FeedsList._get_feed_act_action(author, act)
        feed["action_type"] = act.type.value
        feed["url"] = act.content.url

        return feed

    @staticmethod
    def _get_feed_act_action(author, act):
        action = str()
        if act.type == zhihu.ActType.FOLLOW_COLUMN:
            action = ('%s 在 %s 关注了专栏\n %s' %
                  (author.name, str(act.time).split(" ")[0], act.column.name))
        elif act.type == zhihu.ActType.FOLLOW_QUESTION:
            action = ('%s 在 %s 关注了问题\n %s' % (author.name, act.time, act.question.title))
        elif act.type == zhihu.ActType.ASK_QUESTION:
            action = ('%s 在 %s 提了个问题\n %s' %
                  (author.name, str(act.time).split(" ")[0], act.question.title))
        elif act.type == zhihu.ActType.UPVOTE_POST:
            action = ('%s 在 %s 赞同了专栏\n %s 中 %s 的文章\n %s' %
                  (author.name, str(act.time).split(" ")[0], act.post.column.name,
                   act.post.author.name, act.post.title))
        elif act.type == zhihu.ActType.PUBLISH_POST:
            action = ('%s 在 %s 在专栏\n %s 中发布了文章\n %s' %
                  (author.name, str(act.time).split(" ")[0], act.post.column.name,
                   act.post.title))
        elif act.type == zhihu.ActType.UPVOTE_ANSWER:
            action = ('%s 在 %s 赞同了问题\n %s \n中 %s 的回答, '
                  '此回答赞同数:%d' %
                  (author.name, str(act.time).split(" ")[0], act.answer.question.title,
                   act.answer.author.name, act.answer.upvote_num))
        elif act.type == zhihu.ActType.ANSWER_QUESTION:
            action = ('%s 在 %s 回答了问题\n %s \n此回答赞同数:%d' %
                  (author.name, str(act.time).split(" ")[0], act.answer.question.title,
                   act.answer.upvote_num))
        elif act.type == zhihu.ActType.FOLLOW_TOPIC:
            action = ('%s 在 %s \n关注了话题 %s' %
                  (author.name, str(act.time).split(" ")[0], act.topic.name))

        return action

    @staticmethod
    def del_feeds_list(name):
        feeds_lists = FeedsList.get_feeds_lists_in_json()

        for index, feeds_list in enumerate(feeds_lists):
            if feeds_list.name == name:
                del feeds_lists[index]

        FeedsList.write_feeds_lists_in_json(feeds_lists)

    # save and load
    @staticmethod
    def write_feeds_lists_in_json(feeds_lists):
        data = [feeds_list.list for feeds_list in feeds_lists]
        json_data = json.dumps(data)
        with open(FEEDS_JSON_DIR, mode='w') as f:
            f.write(json_data)

    @staticmethod
    def get_feeds_lists_in_json():
        if not os.path.exists(FEEDS_JSON_DIR):
            file = open(FEEDS_JSON_DIR, 'w')
            file.close()

        with open(FEEDS_JSON_DIR, mode='r') as f:
            json_data = f.read()
        if not json_data:
            return []

        data = json.loads(json_data)
        feeds_lists = [FeedsList(list=feeds_list) for feeds_list in data]
        return feeds_lists
