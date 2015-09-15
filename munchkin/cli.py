#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import munchkin

package_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, package_folder)

if __name__ == '__main__':
    sys.exit(munchkin.main(sys.argv[1:]))
