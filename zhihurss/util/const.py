__author__ = 'yuwei'

import os
import sys

if hasattr(sys, 'frozen'):
    BASE_DIR = os.path.dirname(sys.executable)
    QML_ROOT = os.path.join(BASE_DIR, 'qml')
else:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    QML_ROOT = os.path.join(BASE_DIR, 'res', 'qml')


NOTICERS_JSON_PATH = os.path.join(BASE_DIR, 'config', 'noticers.json')
FEEDS_JSON_PATH = os.path.join(BASE_DIR, 'cache', 'feeds.json')
PROXY_PATH = os.path.join(BASE_DIR, 'config', 'proxy.json')



MAIN_QML_PATH = os.path.join(QML_ROOT, 'main.qml')
ADD_QML_PATH = os.path.join(QML_ROOT, 'add.qml')
ERROR_QML_PATH = os.path.join(QML_ROOT, 'error.qml')
CHANGE_QML_PATH = os.path.join(QML_ROOT, 'change.qml')


CSS_GITHUB_PATH = "https://raw.githubusercontent.com/SimplyY/save/master/github-markdown.css"
