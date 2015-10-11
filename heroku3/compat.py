# -*- coding: utf-8 -*-

"""
heroku3.compat
~~~~~~~~~~~~~

Compatiblity for heroku3.py.
"""
from __future__ import unicode_literals

try:
    import json
except ImportError:
    import simplejson as json
