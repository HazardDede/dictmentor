from dictmentor import DictMentor
from dictmentor.extensions import Environment
from dictmentor.utils import modified_environ


def test_environment_with_inline_default():
    jstr = '{"a": 1, "file_path": "my_file.{{env::ENVIRONMENT:=local}}.cfg"}'
    with modified_environ('ENVIRONMENT'):
        res = DictMentor().bind(Environment()).load_yaml(jstr)

    assert res == {'a': 1, 'file_path': 'my_file.local.cfg'}


def test_environment_with_nested_inline_default():
    jstr = '{"a": 1, "file_path": "my_file.{{env::ENVIRONMENT:={{env::DEFAULT}}.cfg}}"}'
    with modified_environ('ENVIRONMENT', DEFAULT='the_default'):
        res = DictMentor().bind(Environment()).load_yaml(jstr)

    assert res == {'a': 1, 'file_path': 'my_file.the_default.cfg'}


def test_environment_with_multiple_patterns():
    jstr = '{"a": 1, "file_path": "{{env::A}}-{{env::B}}-{{env::C}}"}'
    with modified_environ(A='aval', B='bval', C='cval'):
        res = DictMentor().bind(Environment()).load_yaml(jstr)

    assert res == {'a': 1, 'file_path': 'aval-bval-cval'}
