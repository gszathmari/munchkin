# -*- coding: utf-8 -*-

import sys

def supported_python_version():
    python_version = sys.version.split()[0]
    if python_version >= "3" or python_version < "2.6":
        return False
    else:
        return True
