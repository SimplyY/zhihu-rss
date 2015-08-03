#!/usr/bin/env python

__author__ = 'yuwei'

from .fs import ensure_dir
from .const import CONFIG_PATH, COOKIES_PATH

from ..model.noticer import Noticer
from ..model.feeds_list import FeedsList

from zhihu import ZhihuClient
import json

def set_config(my_app):

    ensure_dir(CONFIG_PATH)
    try:
        with open(CONFIG_PATH, 'r') as f:
            data = f.readline()
            if data:
                try:
                    config = json.loads(data)
                except ValueError:
                    return

    except FileNotFoundError:   # first run or delete config file
        with open(CONFIG_PATH, 'w'):
            pass

    if data:
        if config["is_sign"] and config["is_sign"] is not str or list:
            try:
                with open(COOKIES_PATH, 'r') as f:
                    FeedsList.client = ZhihuClient(COOKIES_PATH)
                    Noticer.client = ZhihuClient(COOKIES_PATH)
            except FileNotFoundError:   # first run or delete config file
                with open(CONFIG_PATH, 'w'):
                    pass
        else:
            FeedsList.client = ZhihuClient()
            Noticer.client = ZhihuClient()
        if config["proxy"]:
            FeedsList.client.set_proxy(config["proxy"])
            Noticer.client.set_proxy(config["proxy"])
