from .code_node import CodeNode
from .package import Package


class AST(CodeNode):
    """
    This is the base of the AST. It's like the log of the tree, that holds all the
    branches. Okay. So this can hold only two things, which are whole packages and
    directives for the C preprocessor.

    To declare a directive, you must use the % character. For example:
    ```
    %include <stdio.h>
    ```

    And the rest, just are packages wich begin with the ```package``` keyword and end up
    with an END OF FILE.
    """

    def __init__(self, name):
        super().__init__(parent=None)

        self.name = name
        self.directives = []
        self.packages   = []
    
    def add_directive(self, directive):     self.directives.append(directive)
    def open_package(self, name):
        for pkg in self.packages:
            if pkg.name == name: return pkg
        
        pkg = Package(name=name, parent=self)
        self.packages.append(pkg)
        return pkg
