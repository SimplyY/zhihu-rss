__author__ = 'yuwei'

import os
import sys

if hasattr(sys, 'frozen'):
    BASE_DIR = os.path.dirname(sys.executable)
    QML_ROOT = os.path.join(BASE_DIR, 'qml')
else:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    QML_ROOT = os.path.join(BASE_DIR, 'res', 'qml')


NOTICERS_FILE = os.path.join('~', '.config', 'zhihurss', 'noticers.json')
FEEDS_FILE = os.path.join('~', '.cache', 'zhihurss', 'feeds.json')


MAIN_QML_PATH = os.path.join(QML_ROOT, 'main.qml')
ADD_QML_PATH = os.path.join(QML_ROOT, 'add.qml')
ERROR_QML_PATH = os.path.join(QML_ROOT, 'error.qml')
CHANGE_QML_PATH = os.path.join(QML_ROOT, 'change.qml')


NOTICERS_JSON_PATH = os.path.expanduser(NOTICERS_FILE)
FEEDS_JSON_PATH = os.path.expanduser(FEEDS_FILE)

CSS_GITHUB_PATH = "https://raw.githubusercontent.com/SimplyY/save/master/github-markdown.css"
