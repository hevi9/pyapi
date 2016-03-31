from collections import namedtuple
import inspect
import pydoc
import logging
from . import nodes
from . import extracts
import re

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
    reo = re.compile(match)
    def fn(obj, name=None):
        return bool(reo.match(name)) if name else False
    return fn


def ignore(obj, up=None, name=None):
    # D("ignore %r as %r", name, obj)
    return None


def study(obj, up=None, name=None):
    # D("study %r as %r", name, obj)
    return None


def operator(visible):
    def fn(obj, up=None, name=None):
        node = nodes.Function(obj, up=up, name=name)
        node.operator = visible
    return fn


def setdoc(obj, up=None, name=None):
    if up is not None:
        up._doc = pydoc.getdoc(obj)
    return None  # modifier


R = register_rule

# by object type
R(is_module, nodes.Module)
R(is_class, nodes.Class)
R(is_routine, nodes.Function)
R(is_data, nodes.Data)

# ignore private _* objects
R(is_match("_[^_].*"), ignore, +1)


# system attributes
R(is_match("__class__"), ignore, +2)  # recursive !
R(is_match("__dict__"), ignore, +1)
R(is_match("__subclasshook__"), ignore, +1)
R(is_match("__weakref__"), ignore, +1)
R(is_match("__new__"), ignore, +1)
R(is_match("__builtins__"), ignore, +1)
R(is_match("__cached__"), ignore, +1)
R(is_match("__name__"), ignore, +1)
R(is_match("__slots__"), ignore, +1)

# documentation
R(is_match("__doc__"), setdoc, +1)

# object representation, considered common
R(is_match("__repr__"), ignore, +1)
R(is_match("__str__"), ignore, +1)
R(is_match("__hash__"), ignore, +1)  # common ?

# attribute resolving methods, not visible in api
R(is_match("__getattribute__"), ignore, +1)
R(is_match("__getattr__"), ignore, +1)
R(is_match("__setattr__"), ignore, +1)
R(is_match("__delattr__"), ignore, +1)

# comparision operators
R(is_match("__eq__"), operator("{s} == {x}"), +1)
R(is_match("__ne__"), operator("{s} != {x}"), +1)
R(is_match("__gt__"), operator("{s} > {x}"), +1)
R(is_match("__ge__"), operator("{s} >= {x}"), +1)
R(is_match("__lt__"), operator("{s} < {x}"), +1)
R(is_match("__le__"), operator("{s} <= {x}"), +1)

# numeric operators
R(is_match("__mul__"), operator("{s} * {x}"), +1)
R(is_match("__rmul__"), operator("{x} * {s}"), +1)
R(is_match("__neg__"), operator("-{s}"), +1)
R(is_match("__pos__"), operator("+{s}"), +1)
R(is_match("__pow__"), operator("{s} ** {x}"), +1)
R(is_match("__rpow__"), operator("{x} ** {s}"), +1)
R(is_match("__add__"), operator("{s} + {x}"), +1)
R(is_match("__radd__"), operator("{x} + {s}"), +1)
R(is_match("__sub__"), operator("{s} - {x}"), +1)
R(is_match("__rsub__"), operator("{x} - {s}"), +1)
R(is_match("__rtruediv__"), operator("{x} / {s}"), +1)
R(is_match("__truediv__"), operator("{s} / {x}"), +1)

# "buildin" operators
R(is_match("__abs__"), operator("abs({s})"), +1)

# type "conversion"
R(is_match("__bool__"), operator("bool({s})"), +1)
R(is_match("__complex__"), operator("complex({s})"), +1)


# object relationships
R(is_match("__file__"), ignore, +1)
R(is_match("__package__"), ignore, +1)
R(is_match("__path__"), ignore, +1)

# todo
R(is_match("__dir__"), study, +1)
R(is_match("__format__"), study, +1)
R(is_match("__init__"), study, +1)
R(is_match("__module__"), study, +1)
R(is_match("__reduce__"), study, +1)
R(is_match("__reduce_ex__"), study, +1)
R(is_match("__sizeof__"), study, +1)
R(is_match("__contains__"), study, +1)
R(is_match("__spec__"), study, +1)
R(is_match("__loader__"), study, +1)
R(is_match("__all__"), study, +1)
R(is_match("__initializing__"), study, +1)
R(is_match("__abstractmethods__"), study, +1)
