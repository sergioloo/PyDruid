from .scope_node import ScopeNode


class Container:
    attributes  = []
    classes     = []
    methods     = []

    scope       = None

    def __init__(self, id_, parent=None):
        # Parent debe ser un Container
        self.scope = ScopeNode(id_, parent.scope if parent else None) 

    def add_attribute(self, attr):  
        self.scope.register(attr.init.id)
        self.attributes.append(attr)
        
    def add_method(self, method):
        self.scope.register(method.init.id)
        self.methods.append(method)

    def add_class(self, class_):
        self.scope.register(class_.init.id)
        self.classes.append(class_)
 