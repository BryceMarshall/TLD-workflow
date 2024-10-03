import json
from .Page import Page
from .Tag import Tag

from dataclasses import dataclass, field


@dataclass
class Notebook:
    prefix: str
    pagedict: dict = field(default_factory=dict)

    def __post_init__(self):
        if "pages" in self.content:
            pagejson = self.content["pages"]
            self.pagedict = {p: Page(self.prefix, p) for p in pagejson}
        elif "cPages" in self.content:
            pagejson = self.content["cPages"]["pages"]
            self.pagedict = {p["id"]:Page(self.prefix, p["id"]) for p in pagejson}
        else:
            raise ValueError("No pages found in content")

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

    def get_pagenum(self, page: Page):
        return self.pagelist.index(page)

    def get_page_with_tag(self, tagname: str):
        return [p for p in self.pagelist if tagname in [t.name for t in p.tags]]

    def __repr__(self):
        pagrepr = [p for p in self.pagelist if len(p.tags) > 0]

        return f'''
        Notebook Name: {self.name}
        Number of Pages: {len(self.pages)}
        Tags: {pagrepr}
        '''
