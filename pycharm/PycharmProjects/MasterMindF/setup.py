from distutils.core import setup
import py2exe
import os
from pathlib import Path
from time import sleep
import sqlite3
import re

setup(zipfile=None,
      options={'py2exe': {"bundle_files": 1}},
      windows=['hack.py'])