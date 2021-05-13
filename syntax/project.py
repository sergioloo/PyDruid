from .container     import Container
from .scope_node    import ScopeNode


class Project(Container):
    def __init__(self, id_):
        super().__init__(id_)

        self.id         = id_
        self.packages   = []

    def __repr__(self):
        return f"""Project {self.id}:
    Packages: {self.packages}
"""
    
    def add_package(self, pkg):
        self.packages.append(pkg)
