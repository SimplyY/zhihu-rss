__author__ = 'yuwei'
import zhihu
import json
import os
import threading

from .noticer import Noticer
from ..util.const import FEEDS_JSON_PATH
from ..util.fs import ensure_dir

# 结构
# feedslists[
#     feedslist{
#         name
#         url
#         feeds[feed{
#            is_read,
#            url,
#            action_type,
#            action
# }]
#         list
#     }
# ]


class FeedsList:
    def __init__(self, added_feeds=100, noticer=None, list=None):
        if not list:
            self.url = noticer.url
            self.name = noticer.name

            author = zhihu.Author(self.url)

            self.feeds = FeedsList.get_feeds(noticer, author, added_feeds)

            self.list = [self.url, self.name]
            self.list.append(self.feeds)
        else:
            self.url = list[0]
            self.name = list[1]
            self.list = list
            self.feeds = list[2]

    def get_dict(self):
        return {"url": self.url, "name": self.name, "feeds": self.feeds}

    feeds_lists_json_lock = threading.RLock()

    @staticmethod
    def get_feeds_list(name):
        feeds_lists = FeedsList.get_feeds_lists_in_json()
        for feeds_list in feeds_lists:
            if feeds_list.name == name:
                return feeds_list.get_dict()
        raise "can't get a feedslist whose name is arg name"

    @staticmethod
    def update_feeds_lists(noticers):
        old_feeds_lists = FeedsList.get_feeds_lists_in_json()
        new_feeds_lists = FeedsList.new_feeds_lists(noticers, old_feeds_lists)
        FeedsList.write_feeds_lists_in_json(new_feeds_lists)

    @staticmethod
    def new_feeds_lists(noticers, old_feeds_lists):

        for noticer in noticers:
            for index, old_feeds_list in enumerate(old_feeds_lists):
                if old_feeds_list.url == noticer.url:
                    old_feeds_lists[index] = FeedsList.get_new_feeds(noticer, old_feeds_list)
                    break

        return old_feeds_lists

    @staticmethod
    def get_new_feeds(noticer, old_feeds_list):
        latest_act_url = noticer.latest_act_url
        author = zhihu.Author(noticer.url)
        acticities = author.activities

        new_feeds = []
        for index, act in enumerate(acticities):
            # 更新完成条件
            if latest_act_url == act.content.url:
                break

            if index == 0:
                noticer.set_latest_act_url(act.content.url)
                Noticer.add_noticer(noticer)

            feed = FeedsList._create_feed(author, act)
            new_feeds.append(feed)

        for feed in reversed(new_feeds):
            old_feeds_list.feeds.insert(0, feed)

        return old_feeds_list

    @staticmethod
    def add_feeds_list(noticer, added_feeds):
        old_feeds_lists = FeedsList.get_feeds_lists_in_json()
        new_feeds_lists = FeedsList.get_added_feeds_list(noticer, added_feeds, old_feeds_lists)
        FeedsList.write_feeds_lists_in_json(new_feeds_lists)

    @staticmethod
    def get_added_feeds_list(noticer, added_feeds, old_feeds_lists):

        if noticer.name in [feeds_list.name for feeds_list in old_feeds_lists]:
            added_feeds.is_finish()
            return old_feeds_lists

        feeds_list = FeedsList(noticer=noticer, added_feeds=added_feeds)

        old_feeds_lists.append(feeds_list)
        new_feeds_lists = old_feeds_lists

        return new_feeds_lists

    @staticmethod
    def get_feeds(noticer, author, added_feeds):
        feeds = []
        activities = author.activities

        for act in activities:
            # 截止遍历的条件
            if int(added_feeds.max_feeds_num) == len(feeds):
                break

            feed = FeedsList._create_feed(author, act)
            feeds.append(feed)
            added_feeds.add_getted_feeds_num()

        added_feeds.is_finish()

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
        my_str = '<b><font size="4" color="black">「{}」</font></b>'
        my_space = '&nbsp;&nbsp;&nbsp;'
        if act.type == zhihu.ActType.FOLLOW_COLUMN:
            action = (my_space+'{} 在 {} 关注了专栏<br>'+my_str).format(author.name, str(act.time).split(" ")[0], act.column.name)
        elif act.type == zhihu.ActType.FOLLOW_QUESTION:
            action = (my_space+' {} 在 {} 关注了问题<br>'+my_str).format(author.name, act.time, act.question.title)
        elif act.type == zhihu.ActType.ASK_QUESTION:
            action = (my_space+'{} 在 {} 提了个问题<br>'+my_str).format(author.name, str(act.time).split(" ")[0], act.question.title)
        elif act.type == zhihu.ActType.UPVOTE_POST:
            action = (my_space+'{} 在 {} 赞同了专栏<br>'+my_str+'中 {} 的文章<br>'+my_str).format(author.name, str(act.time).split(" ")[0], act.post.column.name,
                   act.post.author.name, act.post.title)
        elif act.type == zhihu.ActType.PUBLISH_POST:
            action = (my_space+'{} 在 {} 在专栏<br>'+my_str+'中发布了文章<br>'+my_str).format(
                author.name, str(act.time).split(" ")[0], act.post.column.name,act.post.title)
        elif act.type == zhihu.ActType.UPVOTE_ANSWER:
            action = (my_space+'{} 在 {} 赞同了问题<br>'+my_str+'<br>'+my_space+'中 {} 的回答, '
                  '此回答赞同数:{}').format(author.name, str(act.time).split(" ")[0], act.answer.question.title,
                                 act.answer.author.name, int(act.answer.upvote_num))
        elif act.type == zhihu.ActType.ANSWER_QUESTION:
            action = (my_space+'{} 在 {} 回答了问题<br>'+my_str+'<br>'+my_space+'此回答赞同数:{}').format(
                author.name, str(act.time).split(" ")[0], act.answer.question.title, int(act.answer.upvote_num))
        elif act.type == zhihu.ActType.FOLLOW_TOPIC:
            action = (my_space+'{} 在 {} <br>'+ my_space+'关注了话题'+my_str).format(author.name, str(act.time).split(" ")[0], act.topic.name)
        return action

    @staticmethod
    def del_feeds_list(name):
        feeds_lists = FeedsList.get_feeds_lists_in_json()

        for index, feeds_list in enumerate(feeds_lists):
            if feeds_list.name == name:
                del feeds_lists[index]
                break

        FeedsList.write_feeds_lists_in_json(feeds_lists)

    # save and load
    @staticmethod
    def write_feeds_lists_in_json(feeds_lists):
        data = [feeds_list.list for feeds_list in feeds_lists]
        json_data = json.dumps(data)
        with FeedsList.feeds_lists_json_lock:
            ensure_dir(FEEDS_JSON_PATH)
            with open(FEEDS_JSON_PATH, 'wb') as f:
                f.write(json_data.encode('utf-8'))

    @staticmethod
    def get_feeds_lists_in_json():

        with FeedsList.feeds_lists_json_lock:
            if not os.path.exists(FEEDS_JSON_PATH):
                with open(FEEDS_JSON_PATH, 'w'):
                    return []
            try:
                with open(FEEDS_JSON_PATH, 'rb') as f:
                    json_data = f.read().decode('utf-8')

            except FileNotFoundError:
                return []
        if json_data:
            data = json.loads(json_data)
        else:
            return []

        return [FeedsList(list=feeds_list) for feeds_list in data]
