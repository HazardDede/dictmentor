"""Package dictmentor."""

from . import extensions
from .base import DictMentor

DictMentor = DictMentor
ext = extensions  # pylint: disable=invalid-name


def version():
    """Return the version of the package."""
    return '0.2.0'
