# Import DictMentor and extensions
import dictmentor.extensions as ext
from dictmentor import DictMentor

import os
base_path = os.path.dirname(__file__)

yml = """
statements:
  external: "inner.yaml"
"""

result = DictMentor().bind(ext.ExternalYamlResource(base_path=base_path)).load_yaml(yml)

from pprint import pprint
pprint(result)

# Result:
# {'statements': {'inner': {'item1': None,
#                           'item2': {'price': 50},
#                           'item3': {'count': 5, 'price': 100, 'sold': 200}}}}
