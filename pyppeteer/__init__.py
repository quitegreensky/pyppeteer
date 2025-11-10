#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Meta data for pyppeteer."""

import logging
import os
import platform


from appdirs import AppDirs

from importlib.metadata import version

try:
    __version__ = version(__name__)
except Exception:
    __version__ = None

def get_os_type():
    os_name = platform.system()
    if os_name == "Windows":
        return "win"
    elif os_name == "Linux":
        return "linux"
    elif os_name == "Darwin":
        return "mac"
    else:
        return os_name  # For any other OS

# old chrome version panic upon launching - this one may not match the base puppeteer version, but at least it launches
if get_os_type()=="linux":
    __chromium_revision__ = "1000000"
else:
    __chromium_revision__ = '1000027'


__base_puppeteer_version__ = 'v1.6.0'
__pyppeteer_home__ = os.environ.get('PYPPETEER_HOME', AppDirs('pyppeteer').user_data_dir)  # type: str
DEBUG = False

from pyppeteer.launcher import connect, executablePath, launch, defaultArgs  # noqa: E402; noqa: E402

version = __version__

__all__ = [
    'connect',
    'launch',
    'executablePath',
    'defaultArgs',
    'version',
]
