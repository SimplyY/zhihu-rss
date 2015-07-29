#!/usr/bin/env python
# -*- coding: utf-8 -*-

application_title = "zhihu-rss"
main_python_file = "scripts/zhihurss"

import sys
from cx_Freeze import setup, Executable

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
                "PyQt5.QtCore",
                "PyQt5.QtWidgets",
                "PyQt5.QtQuick",
                "PyQt5.QtQml",
            },
            "include_files": [
                "zhihurss/res/qml/",
            ]
        }
    },
    executables=[Executable(main_python_file, base=base), ],
)
