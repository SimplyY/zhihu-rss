#!/usr/bin/env python
import sys
import os
from zhihurss.main import run

__author__ = 'yuwei'

if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, os.path.join(path, "zhihurss"))
    run()
