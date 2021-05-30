from syntax.nodes.package import Package
from syntax.abstract import CodeNode


class AST(CodeNode):
    def __init__(self, name):
        super().__init__(parent=None)

        self.name       = name
        self.packages   = []
    
    def get_package(self, name):
        for pkg in self.packages: 
            if pkg.name == name: return pkg
        
        pkg = Package(name=name, parent=self)
        self.packages.append(pkg)
        return pkg
