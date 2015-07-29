__author__ = 'yuwei'

import os


MAIN_QML_NAME = 'main.qml'
ADD_QML_NAME = 'add.qml'
ERROR_QML_NAME = 'error.qml'
CHANGE_QML_NAME = 'change.qml'


NOTICERS_FILE = 'noticers.json'
FEEDS_FILE = 'feeds.json'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

RELAT_QML_DIR = os.path.join('src', 'res', 'qml')

MAIN_QML_DIR = os.path.join(BASE_DIR, RELAT_QML_DIR, MAIN_QML_NAME)
ADD_QML_DIR = os.path.join(BASE_DIR, RELAT_QML_DIR, ADD_QML_NAME)
ERROR_QML_DIR = os.path.join(BASE_DIR, RELAT_QML_DIR, ERROR_QML_NAME)
CHANGE_QML_DIR = os.path.join(BASE_DIR, RELAT_QML_DIR, CHANGE_QML_NAME)


NOTICERS_JSON_DIR = os.path.join(BASE_DIR, 'json', NOTICERS_FILE)
FEEDS_JSON_DIR = os.path.join(BASE_DIR, 'json', FEEDS_FILE)

CSS_GITHUB_PATH = "https://raw.githubusercontent.com/SimplyY/save/master/github-markdown.css"
