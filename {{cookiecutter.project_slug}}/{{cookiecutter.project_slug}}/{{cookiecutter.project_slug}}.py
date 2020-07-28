# #!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Main {{ cookiecutter.project_name }} Module """
from __future__ import print_function, unicode_literals

import atexit
import inspect
import logging
import os
import platform
import re
import sys
import time
import traceback
from enum import IntEnum
import pendulum
from pathlib import Path
from typing import List, Union, TYPE_CHECKING


PYTHON2 = sys.version_info[0] < 3

if PYTHON2:
    pass
else:
    pass

if TYPE_CHECKING:
    pass


class {{ cookiecutter.project_name.replace(' ', '_') }}(object):
    def __init__(self, name='name'):
        self.name = name
        atexit.register(self._clean)

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __del__(self):
        self._clean()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._clean()

    def _clean(self):
        pass

    @classmethod
    def instantiate(cls, name=None):
        """
        Main instantiating method for the class. Use it to instantiate global logger.

        :param name: a unique logger name that is re-/used if already exists, defaults to the function path.
        :type name: str
        :return: :class:`{{ cookiecutter.project_name.replace(' ', '_') }}` instance to work with.
        :rtype: :class:`{{ cookiecutter.project_name.replace(' ', '_') }}`
        """
        return cls(name)


if __name__ == '__main__':
    print("")
