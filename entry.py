#!/usr/bin/env python
import sys
import os
from zhihurss.main import run

__author__ = 'yuwei'

if __name__ == '__main__':
    if hasattr(sys, 'frozen') is False:
        path = os.path.dirname(os.path.abspath(__file__))
        sys.path.insert(0, os.path.join(path, "zhihurss"))
    elif sys.platform == 'win32':
        import win32api
        ASADMIN = 'asadmin'

        if sys.argv[-1] != ASADMIN:
            params = ' '.join(sys.argv[1:] + [ASADMIN])
            win32api.ShellExecute(0, 'runas', sys.executable, params, '', 1)
            sys.exit(0)
    run()
