#!/usr/bin/env python
# -*- coding: utf-8 -*-

application_title = "zhihu-rss"
main_python_file = "entry.py"

import sys
import os
import shutil

from cx_Freeze import setup, Executable
import PyQt5

shutil.rmtree("build", ignore_errors=True)

# 非常重要：不同系统位置不同，win 用 everything 来找QtQuick.2文件最好
QML_DIR = "/usr/local/Cellar/qt5/5.4.1/qml/"

includes_files = [
    ("zhihurss/res/qml/", "qml"),
    (os.path.join(QML_DIR, "QtQuick.2"), "qml/QtQuick.2"),
    (os.path.join(QML_DIR, "QtQuick"), "qml/QtQuick"),
    (os.path.join(QML_DIR, "QtWebKit"), "qml/QtWebKit"),

]

base = None
if sys.platform == "win32":
    base = "Win32GUI"


setup(
    name=application_title,
    version="1.0.0",
    url='https://github.com/SimplyY',
    author='SimplyY',
    description="zhihu-rss",
    long_description=open('README.md', 'rb').read().decode('utf-8'),
    zip_safe=False,
    options={
        "build_exe": {
            "packages": {
                "zhihu",
                "PyQt5.QtQuick",
                "PyQt5.QtCore",
                "PyQt5.QtWidgets",
                "PyQt5.QtQml",
            },
            "include_files": includes_files
        }
    },
    executables=[Executable(main_python_file, base=base), ],
)
