from dictmentor import DictMentor
from dictmentor.extensions import Environment
from dictmentor.utils import modified_environ


def test_environment_with_inline_default():
    jstr = '{"a": 1, "file_path": "my_file.{{env::ENVIRONMENT:=local}}.cfg"}'
    with modified_environ('ENVIRONMENT'):
        res = DictMentor().bind(Environment()).load_yaml(jstr)

    assert res == {'a': 1, 'file_path': 'my_file.local.cfg'}
