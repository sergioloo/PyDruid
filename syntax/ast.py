from .node import Node


class AST(Node):
    def __init__(self, **kwargs):
        Node.__init__(self, **kwargs)

        self.packages = []

    def add_package(self, pkg):
        self.packages.append(pkg)
    
    def to_string(self) -> str:
        result = ''

        for pkg in self.packages:
            result += pkg.to_string()

        return result
