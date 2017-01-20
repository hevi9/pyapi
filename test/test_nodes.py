from pyapi.nodes import Node, Root
from logging import debug as D
import sys
from os.path import dirname
from pyapi.extracts import build_node

sys.path.insert(0, dirname(__file__))
from stuff.function import function  # noqa @UnresolvedImport
from stuff.klass import klass  # noqa @UnresolvedImport
from stuff import module1  # noqa @UnresolvedImport


def dev_Node_path_0():
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


def dev_Node_path_nodes():
    r = Root()
    n1 = Node(1, up=r, name="n1")
    n2 = Node(2, up=n1, name="n2")
    n3 = Node(3, up=n2, name="n3")
    nodes = n3.path_nodes
    assert nodes[0] is r
    assert nodes[1] is n1
    assert nodes[2] is n2
    assert nodes[3] is n3



if __name__ == "__main__":
    from logging import basicConfig, DEBUG

    basicConfig(level=DEBUG)
    # test_Node_path_3()
    dev_Node_path_nodes()
