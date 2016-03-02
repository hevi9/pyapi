from collections import namedtuple
import inspect
import pydoc
import logging
from . import nodes

log = logging.getLogger(__name__)
D = log.debug


Rule = namedtuple("Rule", ["applies", "factory", "priority"])
# applies: callable(obj, name=None) -> bool
# factory: callable(obj, name=None, parent=None) -> Node
# - factory or up modifier ?
# priority: rule ordering, default = 0, high 0+, low 0-
_rules = []


def register_rule(applies, factory, priority=0):
    """ """
    _rules.append(Rule(applies, factory, priority))
    _rules.sort(key=lambda rule: rule[2], reverse=True)


def get_rules():
    return _rules


def is_module(obj, name=None):
    return inspect.ismodule(obj)


def is_class(obj, name=None):
    return inspect.isclass(obj)


def is_routine(obj, name=None):
    return inspect.isroutine(obj)


def is_data(obj, name=None):
    return pydoc.isdata(obj)


def is_match(match):
    def fn(obj, name=None):
        return name == match
    return fn


def ignore(obj, up=None, name=None):
    # D("ignore %r as %r", name, obj)
    return None


def study(obj, up=None, name=None):
    D("study %r as %r", name, obj)
    return None


def operator(visible):
    def fn(obj, up=None, name=None):
        node = nodes.Function(obj, up=up, name=name)
        node.visible = visible
    return fn


def setdoc(obj, up=None, name=None):
    if up is not None:
        up._doc = pydoc.getdoc(obj)
    return None  # modifier


register_rule(is_module, nodes.Module)
register_rule(is_class, nodes.Class)
register_rule(is_routine, nodes.Function)
register_rule(is_data, nodes.Data)

# system attributes
register_rule(is_match("__class__"), ignore, +1)  # recursive !
register_rule(is_match("__dict__"), ignore, +1)
register_rule(is_match("__subclasshook__"), ignore, +1)
register_rule(is_match("__weakref__"), ignore, +1)
register_rule(is_match("__new__"), ignore, +1)
register_rule(is_match("__builtins__"), ignore, +1)
register_rule(is_match("__cached__"), ignore, +1)
register_rule(is_match("__name__"), ignore, +1)

# documentation
register_rule(is_match("__doc__"), setdoc, +1)

# object representation, considered common
register_rule(is_match("__repr__"), ignore, +1)
register_rule(is_match("__str__"), ignore, +1)
register_rule(is_match("__hash__"), ignore, +1)  # common ?


# attribute resolving methods, not visible in api
register_rule(is_match("__getattribute__"), ignore, +1)
register_rule(is_match("__getattr__"), ignore, +1)
register_rule(is_match("__setattr__"), ignore, +1)
register_rule(is_match("__delattr__"), ignore, +1)


# comparision operators
register_rule(is_match("__eq__"), operator("=="), +1)
register_rule(is_match("__ne__"), operator("!="), +1)
register_rule(is_match("__gt__"), operator(">"), +1)
register_rule(is_match("__ge__"), operator(">="), +1)
register_rule(is_match("__lt__"), operator("<"), +1)
register_rule(is_match("__le__"), operator("<="), +1)

# object relationships
register_rule(is_match("__file__"), ignore, +1)
register_rule(is_match("__package__"), ignore, +1)
register_rule(is_match("__path__"), ignore, +1)

# todo
register_rule(is_match("__dir__"), ignore, +1)
register_rule(is_match("__format__"), ignore, +1)
register_rule(is_match("__init__"), study, +1)
register_rule(is_match("__module__"), ignore, +1)
register_rule(is_match("__reduce__"), ignore, +1)
register_rule(is_match("__reduce_ex__"), ignore, +1)
register_rule(is_match("__sizeof__"), ignore, +1)
register_rule(is_match("__add__"), ignore, +1)
register_rule(is_match("__contains__"), ignore, +1)
register_rule(is_match("__spec__"), ignore, +1)
register_rule(is_match("__loader__"), ignore, +1)
register_rule(is_match("__all__"), ignore, +1)
register_rule(is_match("__initializing__"), ignore, +1)
