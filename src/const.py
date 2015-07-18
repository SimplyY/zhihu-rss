__author__ = 'yuwei'

import os

MAIN_QML_NAME = 'main.qml'
SIGN_QML_NAME = 'sign.qml'
ADD_QML_NAME = 'add.qml'
ERROR_QML_NAME = 'error.qml'

NOTICERS_FILE = 'noticers.json'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MAIN_QML_DIR = os.path.join(BASE_DIR, 'src', 'qml', MAIN_QML_NAME)
SIGN_QML_DIR = os.path.join(BASE_DIR, 'src', 'qml', SIGN_QML_NAME)
ADD_QML_DIR = os.path.join(BASE_DIR, 'src', 'qml', ADD_QML_NAME)
ERROR_QML_DIR = os.path.join(BASE_DIR, 'src', 'qml', ERROR_QML_NAME)


NOTICERS_JSON_DIR = os.path.join(BASE_DIR, 'json', NOTICERS_FILE)

CSS_GITHUB_PATH = "https://raw.githubusercontent.com/SimplyY/save/master/github-markdown.css"
