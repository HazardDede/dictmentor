import os
from tempfile import NamedTemporaryFile, TemporaryDirectory

from dictmentor.utils import FileLocator


def test_build_abs_path_with_absolute_path():
    with NamedTemporaryFile() as ntf:
        assert FileLocator()(ntf.name, ntf.name) == ntf.name
        assert FileLocator(os.path.dirname(ntf.name))(ntf.name, ntf.name) == ntf.name


def test_build_abs_path_relative_path_with_base_path_and_document_as_file():
    external_resource = 'abc/def.yaml'
    with TemporaryDirectory() as base_path:
        with NamedTemporaryFile() as document:
                assert (FileLocator(base_path)(external_resource, document.name)
                        == os.path.join(base_path, external_resource))
                assert (FileLocator(base_path, parent_overrides_base=True)(external_resource, document.name)
                        == os.path.join(os.path.dirname(document.name), external_resource))


def test_build_abs_path_relative_path_with_base_path_and_nonfile_document():
    external_resource = 'abc/def.yaml'
    with TemporaryDirectory() as base_path:
            assert (FileLocator(base_path)(external_resource, 'non_valid_path')
                    == os.path.join(base_path, external_resource))


def test_build_abs_path_relative_path_with_non_base_path_but_document_as_file():
    external_resource = 'abc/def.yaml'
    with TemporaryDirectory() as base_path:
        with NamedTemporaryFile() as document:
            assert (FileLocator()(external_resource, document.name)
                    == os.path.join(os.path.dirname(document.name), external_resource))


def test_build_abs_path_relative_path_with_non_base_path_and_nonfile_document():
    external_resource = 'abc/def.yaml'
    with TemporaryDirectory() as base_path:
            assert (FileLocator()(external_resource, 'non_valid_path')
                    == os.path.join(os.getcwd(), external_resource))