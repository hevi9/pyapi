import re


def none(name):
    return None

rule_name_map = {
    "__builtins__": none,
    "__cached__": none,
    "__file__": none,
    "__name__": none,
    "__package__": none,
    "__path__": none,
    "__spec__": none,
    "__doc__": none,
    "__loader__": none,
    "__all__": none
}

rule_name_map_re = {
    re.compile(r"^_.*"): none
}


def rule_name(name):
    # if direct name match
    if name in rule_name_map:
        return rule_name_map[name](name)

    # if RE name match
    for rex in rule_name_map_re:
        if rex.match(name):
            return rule_name_map_re[rex](name)

    return name
