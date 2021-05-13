from .container     import Container


class Package(Container):
    def __init__(self, id_, parent):
        super().__init__(id_, parent)

        self.id         = id_
        self.classes    = []
        self.methods    = []

    def __repr__(self):
        return f"""
        [Package {self.id}
            Classes: {self.classes},
            Methods: {self.methods}
        ]
"""
    
    def to_c(self):
        result = f'// package {self.id}\n\n'
        for class_ in self.classes:
            result += class_.to_c()

        return result
