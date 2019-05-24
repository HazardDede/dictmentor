from dictmentor import DictMentor
from dictmentor.extensions import Variables


def test_environment_with_multiple_patterns():
    jstr = '{"a": 1, "file_path": "{{var::a}}-{{var::b}}-{{var::c}}"}'
    res = DictMentor().bind(Variables(
        a='aval',
        b='bval',
        c='cval'
    )).load_yaml(jstr)

    assert res == {'a': 1, 'file_path': 'aval-bval-cval'}
