# Import DictMentor and extensions
import dictmentor.extensions as ext
from dictmentor import DictMentor, utils

yml = """
statements:
  my_env: "{{var::my_env}}"
  home: "{{var::home}}"
  unknown: "{{var::unknown}}"
  combined: "{{var::my_env}}@{{var::home}}"
"""

var_ext = ext.Variables(
    my_env='development',
    home="/home/pi",
)
result = DictMentor().bind(var_ext).load_yaml(yml)

from pprint import pprint
pprint(result)

# Result:
# {'statements': {'combined': 'development@/home/pi',
#                 'home': '/home/pi',
#                 'my_env': 'development',
#                 'unknown': 'none'}}
