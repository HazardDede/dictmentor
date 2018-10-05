# Import DictMentor and extensions
import dictmentor.extensions as ext
from dictmentor import DictMentor

import os
base_path = os.path.dirname(__file__)

yml = """
statements:
  all: "{{external::all.sql}}"
  single: "{{external::single.sql}}"
"""

result = DictMentor().bind(ext.ExternalResource(base_path)).load_yaml(yml)

from pprint import pprint
pprint(result)

# Result:
# {'statements': {'all': '-- Contents of all.sql\nSELECT *\nFROM foo\n;',
#                 'single': '-- Contents of single.sql\nSELECT *\nFROM foo\nWHERE id = {placeholder}\n;'}}
