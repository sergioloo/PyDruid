class Package:
    def __init__(self, id_):
        self.id         = id_
        self.classes    = []
        self.methods    = []
    
    def __repr__(self):
        return f"[Package {self.id}]"

    def add_class(self, class_):
        self.classes.append(class_)
    
    def add_method(self, method):
        self.methods.append(method)
