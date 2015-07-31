#!/usr/bin/env python
# -*- coding: utf-8 -*-

application_title = "zhihu-rss"
main_python_file = "entry.py"

import os
import sys
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

PYQT5_DIR = os.path.join(get_python_lib(), "PyQt5")

include_files = [
    ("zhihurss/res/qml/", "qml"),
    (os.path.join(PYQT5_DIR, "qml", "QtQuick"), "QtQuick"),
    (os.path.join(PYQT5_DIR, "qml", "QtQuick.2"), "QtQuick.2"),
    (os.path.join(PYQT5_DIR, "qml", "QtWebKit"), "QtWebKit")
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
