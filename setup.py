#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import sys
import os
import re
import ast

from setuptools import setup, find_packages

if sys.argv[-1] == 'publish':
    os.system('py setup.py sdist upload')
    sys.exit()


def extract_requirements(filename='requirements.txt'):
    with open(filename, 'rb') as f_require:
        lines = f_require.read().decode('utf-8').split('\n')

    # ignore comments and empty lines
    requires = [
        line
        for line in lines
        if line and not line.strip().startswith('#')
    ]

    return requires


def extract_version():
    with open('zhihurss/__init__.py', 'rb') as f_version:
        ast_tree = re.search(
            r'__version__ = (.*)',
            f_version.read().decode('utf-8')
        ).group(1)
        if ast_tree is None:
            raise RuntimeError('Cannot find version information')
        return str(ast.literal_eval(ast_tree))

    return version


with open('README.md', 'rb') as f_readme:
    readme = f_readme.read().decode('utf-8')


version = extract_version()
requires = extract_requirements()


setup(
    name='zhihurss',
    version=version,
    description='zhihurss',
    long_description=readme,

    author='SimplyY',
    author_email='SimplyYu@163.com',
    license='GPLv3+',

    url='https://github.com/SimplyY/zhihu_rss',
    download_url='https://github.com/SimplyY/zhihu-py3/releases',

    install_requires=requires,
    packages=find_packages(),
    entry_points={
        'gui_scripts': [
            'zhihurss = zhihurss.main:run',
        ],
    },
    include_package_data=True,

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications :: Qt',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: Chinese (Simplified)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
