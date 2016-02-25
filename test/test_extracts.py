from pyapi.extracts import build_node
from logging import debug as D


def test_build_node_int():
    node = build_node(1)
    D(node)


def test_build_node_bool():
    node = build_node(True)
    D(node)


def test_build_node_object():
    node = build_node(object())
    D(node)


if __name__ == "__main__":
    from logging import basicConfig, DEBUG
    basicConfig(level=DEBUG)
    # test_build_node_int()
    # test_build_node_bool()
    test_build_node_object()
