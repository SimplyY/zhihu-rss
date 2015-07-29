application_title = "zhihu-rss" #what you want to application to be called
main_python_file = "enter.py"

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
    description="zhihurss cx_Freeze PyQt5 script",
    options={
        "build_exe": {
            "packages": {"PyQt5.QtCore", "PyQt5.QtWidgets", "PyQt5.QtQuick", "PyQt5.QtQml"},
            "include_files": ["zhihurss/res/qml/"]}},

    executables=[Executable(main_python_file, base=base)])
