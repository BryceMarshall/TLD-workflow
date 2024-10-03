from dataclasses import dataclass

@dataclass
class Tag:
    name: str
    pageId: str
    timestamp: str = None

    def __str__(self):
        return f'Tag object for {self.name}'

    def __repr__(self):
        return f'Tag {self.name}'
