from pyapi.extracts import build_node, get_rules, load_module
from logging import debug as D
import sys
from os.path import dirname
import pprint

sys.path.insert(0, dirname(__file__))
from stuff.function import function  # noqa @UnresolvedImport
from stuff.klass import klass  # noqa @UnresolvedImport
from stuff import module  # noqa @UnresolvedImport


def test_build_node_bool():
    node = build_node(True)
    D(node)


def test_build_node_int():
    node = build_node(1)
    D(node)


def test_build_node_str():
    node = build_node("a")
    D(node)


def test_build_node_bytes():
    node = build_node(bytes())
    D(node)


def test_build_node_object():
    node = build_node(object())
    D(node)


def test_build_node_function():
    node = build_node(function)
    D(node)


def test_build_node_class():
    node = build_node(klass)
    D(node)


def test_build_node_module():
    node = build_node(module)
    D(node)


def test_rules():
    pprint.pprint(get_rules())


def test_module_from_path():
    load_module("stuff.module")


def test_Node_path():
    load_module("stuff")

if __name__ == "__main__":
    from logging import basicConfig, DEBUG
    basicConfig(level=DEBUG)
    # test_build_node_bool()
    # test_build_node_int()
    # test_build_node_str()
    # test_build_node_bytes()
    # test_build_node_object()
    # test_build_node_function()
    # test_build_node_class()
    # test_build_node_module()
    # test_rules()
    test_module_from_path()
