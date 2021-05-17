from .node import Node


class Statement:
    def __init__(self, **kwargs):
        self.parent = kwargs['parent']
        self.indent = self.parent.indent + 1 if self.parent and hasattr(self.parent, 'indent') else 0
