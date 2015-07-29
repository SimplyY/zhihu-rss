#!/usr/bin/env python

import threading

from .util.my_thread import MyThread

from .model.feeds_list import FeedsList
from .model.noticer import Noticer

__author__ = 'yuwei'

mutex = threading.Lock()

def update_feeds():
    if mutex.acquire(1):
        noticers = Noticer.get_noticers_in_json()
        FeedsList.update_feeds_lists(noticers)
        mutex.release()


def _run_update():
    update_feeds()
    t = threading.Timer(30.0, _run_update)
    t.start()

def set_update_timer():
    update_thread = MyThread("update thread", _run_update)
    update_thread.start()
