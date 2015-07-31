#!/usr/bin/env python
import sys
import os

__author__ = 'yuwei'

if __name__ == '__main__':
    print(os.path.abspath(__file__))
    sys.path.insert(0, os.path.abspath(__file__))
