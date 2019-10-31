__all__ = ['SECRET']
"""Converts `secrets.json` to python's dict.
to import:
    from __jcr__.secret import SECRET
example uses:
    SECRET_KEY = SECRET['DJANGO']['SECRET_KEY']
SEE `secrets.json`
"""

import json
from collections import namedtuple
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(base_dir, 'secrets.json')


def json2obj(data):
    def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())

    return json.loads(data, object_hook=_json_object_hook)


with open(PATH, 'r') as file:
    SECRET = json.loads(file.read())
