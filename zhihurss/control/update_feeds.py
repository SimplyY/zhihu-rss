#!/usr/bin/env python

import threading
import time

from ..model.feeds_list import FeedsList
from ..model.noticer import Noticer

__author__ = 'yuwei'

mutex = threading.Lock()


def update_feeds():
    with mutex:
        noticers = Noticer.get_noticers_in_json()
        FeedsList.update_feeds_lists(noticers)


class FeedUpdateThread(threading.Thread):
    def run(self):
        while True:
            update_feeds()
            time.sleep(30)


def spawn_update_thread():
    update_thread = FeedUpdateThread(name="update thread", daemon=True)
    update_thread.start()
