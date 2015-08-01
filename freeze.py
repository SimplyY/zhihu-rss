#!/usr/bin/env python
# -*- coding: utf-8 -*-

application_title = "zhihu-rss"
main_python_file = "entry.py"

import sys
import os
import shutil
from distutils.sysconfig import get_python_lib

from cx_Freeze import setup, Executable

shutil.rmtree("build", ignore_errors=True)

packages = [
    "zhihu",
    "lxml",
    "PyQt5.QtQuick",
    "PyQt5.QtCore",
    "PyQt5.QtWidgets",
    "PyQt5.QtQml",
    "PyQt5.QtNetwork"
]

QML_DIR = os.path.join(get_python_lib(), "PyQt5", 'qml')

print('check QML dir: {0}'.format(QML_DIR), '...')

if os.path.exists(QML_DIR) is False:
    print("Can't find PyQt5's QML dir automatically, Please set it dir in freeze.py")
    sys.exist(0)

print('Done.')

include_files = [
    ("zhihurss/res/qml/", "qml"),
    (os.path.join(QML_DIR, "QtQuick"), "QtQuick"),
    (os.path.join(QML_DIR, "QtQuick.2"), "QtQuick.2"),
    (os.path.join(QML_DIR, "QtWebKit"), "QtWebKit")
]

base = None

if sys.platform == "win32":
    base = "Win32GUI"

with open('README.md', 'rb') as f:
    readme = f.read().decode('utf-8')

setup(
    name=application_title,
    version="1.0.0",
    url='https://github.com/SimplyY',
    author='SimplyY',
    description="zhihu-rss",
    long_description=readme,
    options={
        "build_exe": {
            "packages": packages,
            "include_files": include_files
        }
    },
    executables=[Executable(main_python_file, base=base, targetName=application_title+'.exe')],
)
