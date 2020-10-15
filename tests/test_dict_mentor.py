import pytest

import dictmentor.extensions as ext
from dictmentor import DictMentor


def test_bind_extensions_via_init():
    env = ext.Environment()
    extres = ext.ExternalResource()

    dut = DictMentor(env, extres)
    assert len(dut._extensions) == 2
    assert dut._extensions[0] == env
    assert dut._extensions[1] == extres

    dut = DictMentor(env)
    assert len(dut._extensions) == 1
    assert dut._extensions[0] == env


def test_init_extensions_with_non_iterable():
    dut = DictMentor()
    env = ext.Environment()
    dut._init_extensions(env)
    assert len(dut._extensions) == 1
    assert dut._extensions[0] == env


def test_bind_non_extensions():
    dut = DictMentor()
    with pytest.raises(
        ValueError, 
        match='Cannot bind extension due to missing interface requirements'
    ):
        dut.bind("Not an extension")


def test_load_yaml_with_stream():
    import os
    fn = os.path.join(os.path.dirname(__file__), 'resources/simple.yaml')
    dut = DictMentor()
    with open(fn, 'r') as fp:
        dct = dut.load_yaml(fp)

    expected = dict(root=dict(a=1, b=2, c=dict(ca=31, cb=32)))
    assert dct == expected


def test_load_yaml_invalid():
    with pytest.raises(
        TypeError, 
        match="Argument '_yaml' is whether a stream, nor a file, nor a string"
    ):
        DictMentor().load_yaml(5)
