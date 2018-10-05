import os
from dictmentor import DictMentor, extensions as ext, utils


base_path = os.path.dirname(__file__)
dm = DictMentor(
    ext.Environment(),
    ext.ExternalResource(base_path=base_path),
    ext.ExternalYamlResource(base_path=base_path)
)

yml = """
products:
    - external: item1.yaml
    - external: item2.yaml
home_directory: "{{env::HOME}}"
extraction_sql: "{{external::products.sql}}"
"""

with utils.modified_environ(HOME="/home/pi"):
    res = dm.load_yaml(yml)

from pprint import pprint
pprint(res)

# Result:
# {'extraction_sql': '-- Contents of products.sql\nSELECT *\nFROM products\n;',
#  'home_directory': '/home/pi',
#  'products': [{'item1': {'price': 50, 'stock': 100}},
#               {'item2': {'price': 99, 'stock': 10}}]}
