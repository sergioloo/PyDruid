from syntax import package


class Project:
    def __init__(self, id_):
        self.id         = id_
        self.packages   = []
    
    def __repr__(self):
        return f"""Project {self.id}:
    Packages: {self.packages}
"""
    
    def add_package(self, pkg):
        self.packages.append(pkg)
