import os
from dataclasses import dataclass, field
from rmscene.scene_items import Line, Point
from rmscene import SceneTree
from rmscene import read_blocks, build_tree

@dataclass
class Page:
    parent: str
    prefix: str
    tags: list = field(default_factory=list)

    def __iadd__(self, tag):
        self.tags += [tag]
        return self

    def __isub__(self, tag):
        self.tags.remove(tag)
        return self

    @property
    def content(self):
        return open(self.parent + "/" + self.prefix + '.rm', 'rb')

    @property
    def scene(self):
        with self.content as contentfile:
            tree = SceneTree()
            blocks = read_blocks(self.content)
            build_tree(tree, blocks)
            return tree

    def __repr__(self):
        return f'''{os.linesep.join(repr(s) for s in self.tags)}'''

    def __str__(self):
        return f'Data object for {self.prefix}. Tags: {self.tags or "None"}'
