"""Dumping for auxilliary types that are commonly used."""

from uuid import UUID
from pathlib import (
    Path,
    PosixPath,
    PurePath,
    PurePosixPath,
    PureWindowsPath,
    WindowsPath,
)

from pydantic_yaml._yaml import yaml


def _repr_path(dumper, node):
    return dumper.represent_str(str(node))


for _typ in [
    Path,
    PosixPath,
    PurePath,
    PurePosixPath,
    PureWindowsPath,
    WindowsPath,
]:
    yaml.SafeDumper.add_representer(_typ, _repr_path)


# Fix dumping of UUID objects.


def _repr_uuid(dumper, node):
    return dumper.represent_str(str(node))


yaml.SafeDumper.add_representer(UUID, _repr_uuid)


# Fix loading of Unicode strings from Python 2.


def _py2_str(loader, node):
    """Workaround to parsing YAML files generated by Python 2"""
    return node.value


yaml.SafeLoader.add_constructor("tag:yaml.org,2002:python/unicode", _py2_str)
