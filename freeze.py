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

platform = sys.platform

# ===== set PyQt5 dir =====

if platform == 'win32':
    PYQT5_DIR = os.path.join(get_python_lib(), "PyQt5")
elif platform == 'darwin':
    # TODO
    PYQT5_DIR = os.path.join(get_python_lib(), "PyQt5")
elif platform == 'linux':
    # TODO
    PYQT5_DIR = os.path.join(get_python_lib(), "PyQt5")

print('check PyQt5 dir: {0}'.format(PYQT5_DIR), '...')

if not os.path.exists(PYQT5_DIR):
    print("Can't find PyQt5's dir automatically, Please set it in freeze.py")
    sys.exist(0)

print('Done.')

# ===== set qml dir =====

if platform == 'win32':
    QML_DIR = os.path.join(PYQT5_DIR, 'qml')
elif platform == 'darwin':
    # TODO
    QML_DIR = ''
elif platform == 'linux':
    # TODO
    QML_DIR = ''

print('check QML dir: {0}'.format(QML_DIR), '...')

if not os.path.exists(QML_DIR):
    print("Can't find PyQt5's QML dir automatically, Please set it in freeze.py")
    sys.exist(0)

print('Done.')

# ===== setup include files =====

# ----- qt files -----

if platform == 'win32':
    qt_files_list = [
        'libEGL.dll',
        'libGLESv2.dll',
        'QtWebProcess.exe',
        'Qt5WebKitWidgets.dll',
        'Qt5MultimediaWidgets.dll',
        'Qt5OpenGL.dll',
        'Qt5PrintSupport.dll'
    ]
elif platform == 'darwin':
    pass
elif platform == 'linux':
    pass

qt_files = [os.path.join(PYQT5_DIR, filename) for filename in qt_files_list]

# ----- qml dirs -----

if platform == 'win32':
    qml_dirs_list = [
        "QtQuick",
        "QtQuick.2",
        "QtWebKit"
    ]
elif platform == 'darwin':
    # TODO
    qml_dirs_list = []
elif platform == 'linux':
    # TODO
    qml_dirs_list = []

qml_dirs = [(os.path.join(QML_DIR, dirname), dirname) for dirname in qml_dirs_list]

# ----- res files -----

res_files = [("zhihurss/res/qml/", "qml")]

# ----- platfrom extra files -----

if platform == 'win32':
    extra_files = []
elif platform == 'darwin':
    extra_files = []
elif platform == 'linux':
    extra_files = []

# ----- complete include files -----

include_files = qt_files + qml_dirs + res_files + extra_files

# ===== others =====

packages = [
    'lxml'
]

base = None
if platform == "win32":
    base = "Win32GUI"

with open('README.md', 'rb') as f:
    readme = f.read().decode('utf-8')

# ===== setup for build =====

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
            "include_files": include_files,
            "include_msvcr": True if sys.platform == 'win32' else False
        }
    },
    executables=[Executable(main_python_file, base=base, targetName=application_title+'.exe')],
)
