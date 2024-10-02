import json
from dataclasses import dataclass, field
from os import linesep

@dataclass
class Tag:
    name: str
    pageId: str
    timestamp: str = None

    def __str__(self):
        return f'Tag object for {self.name}'

    def __repr__(self):
        return f'Tag {self.name}'

@dataclass
class Page:
    prefix: str
    tags: list = field(default_factory=list)

    def __iadd__(self, tag):
        self.tags += [tag]
        return self

    def __isub__(self, tag):
        self.tags.remove(tag)
        return self

    def __repr__(self):
        return f''' {os.linesep.join(self.tags)} '''
    def __str__(self):
        return f'Data object for {self.prefix}. Tags: {self.tags or "None"}'
         

@dataclass
class Notebook:
    prefix: str
    pagedict: dict = field(default_factory=dict)


    def __post_init__(self):
        pagejson = self.content["cPages"]["pages"]
        self.pagedict = {p["id"]:Page(p["id"]) for p in pagejson}

        tagjson = self.content["pageTags"]
        for tag in tagjson:
            self.pagedict[tag["pageId"]].tags += [Tag(tag["name"], tag["pageId"], tag["timestamp"])]


    @property
    def content(self):
        with open(self.prefix + '.content', 'r') as f:
            return json.loads(f.read())

    @property
    def metadata(self):
        with open(self.prefix + '.metadata', 'r') as f:
            return json.loads(f.read())

    @property
    def filename(self):
        return self.metadata["filename"]

    @property
    def name(self):
        return self.metadata["visibleName"]

    @property
    def pages(self):
        return self.pagedict

    @property
    def pagelist(self):
        return list(self.pagedict.values())

    def __repr__(self):
        pagrepr = [p for p in self.pagelist if len(p.tags) > 0]
        return f'''
        Notebook Name: {self.name}
        Number of Pages: {len(self.pages)}
        Tags: {pagrepr}
        '''
