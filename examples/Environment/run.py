# Import DictMentor and extensions
import dictmentor.extensions as ext
from dictmentor import DictMentor, utils

yml = """
statements:
  my_env: "{{env::MY_ENV}}"
  home: "{{env::HOME}}"
  unknown: "{{env::UNKNOWN}}"
"""

# Make sure that MY_ENV is set and that UNKNOWN is unset
with utils.modified_environ("UNKNOWN", MY_ENV='development'):
    result = DictMentor().bind(ext.Environment()).load_yaml(yml)

from pprint import pprint
pprint(result)

# Result:
# {'statements': {'home': '/home/pi',
#                 'my_env': 'development',
#                 'unknown': 'none'}}
