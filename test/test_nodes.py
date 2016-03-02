
from pyapi.nodes import Node, Root
from logging import debug as D
import sys
from os.path import dirname
from pyapi.extracts import build_node

sys.path.insert(0, dirname(__file__))
from stuff.function import function  # noqa @UnresolvedImport
from stuff.klass import klass  # noqa @UnresolvedImport
from stuff import module  # noqa @UnresolvedImport


def test_Node_path_0():
    n = Node(1)
    D(n.path)


def test_Node_path_1():
    n = Node(1, name="a")
    n = Node(2, name="b", up=n)
    assert n.path == "a.b"


def test_Node_path_2():
    n = build_node(module)
    assert n.path == "stuff.module"


def test_Node_path_3():
    n = Root()
    assert n.path == None


if __name__ == "__main__":
    from logging import basicConfig, DEBUG
    basicConfig(level=DEBUG)
    test_Node_path_3()
