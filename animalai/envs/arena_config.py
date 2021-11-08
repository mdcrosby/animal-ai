import yaml

from typing import List

yaml.Dumper.ignore_aliases = lambda *args: True

class Vector3(yaml.YAMLObject):
    yaml_tag = u"!Vector3"

    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self.x = x
        self.y = y
        self.z = z

class RGB(yaml.YAMLObject):
    yaml_tag = u"!RGB"

    def __init__(self, r: float = 0, g: float = 0, b: float = 0):
        self.r = r
        self.g = g
        self.b = b

class Item(yaml.YAMLObject):
    yaml_tag = u"!Item"

    def __init__(
        self,
        name: str = "",
        positions: List[Vector3] = None,
        rotations: List[float] = None,
        sizes: List[Vector3] = None,
        colors: List[RGB] = None,
    ):
        self.name = name
        self.positions = positions if positions is not None else []
        self.rotations = rotations if rotations is not None else []
        self.sizes = sizes if sizes is not None else []
        self.colors = colors if colors is not None else []


class Arena(yaml.YAMLObject):
    yaml_tag = u"!Arena"

    def __init__(
        self,
        t: int = 1000,
        items: List[Item] = None,
        pass_mark: float = 0,
        blackouts: List[int] = None,
    ):
        self.t = t
        self.items = items if items is not None else {}
        self.pass_mark = pass_mark
        self.blackouts = blackouts if blackouts is not None else []

class ArenaConfig(yaml.YAMLObject):
    yaml_tag = u"!ArenaConfig"

    def __init__(self, yaml_path: str = None):

        if yaml_path is not None:
            self.arenas = yaml.load(open(yaml_path, "r"), Loader=yaml.Loader).arenas
        else:
            self.arenas = {}

def constructor_arena(loader, node):
    fields = loader.construct_mapping(node)
    return Arena(**fields)

def constructor_item(loader, node):
    fields = loader.construct_mapping(node)
    return Item(**fields)

yaml.add_constructor(u"!Arena", constructor_arena)
yaml.add_constructor(u"!Item", constructor_item)
