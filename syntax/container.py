from utils.error import Error
from .scope_node import ScopeNode


class Container:
    def __init__(self, id_, parent=None):
        # Parent debe ser un Container
        self.id     = id_
        self.parent = parent

        self.attributes = []
        self.methods    = []
        self.classes    = []

        self.indent     = 0     # TODO: Haz que esto haga algo

        self.imports    = {}

    def add_attribute(self, attr):
        attr.parent = self  
        self.attributes.append(attr)
        
    def add_method(self, method):
        method.parent = self
        self.methods.append(method)

    def add_class(self, class_):
        class_.parent = self
        self.classes.append(class_)
    
    def import_(self, obj: str):
        obj_name = obj[obj.rindex('_') + 1 : ]
        self.imports[obj_name] = obj

    def get_full_id(self) -> str:
        result = self.id

        parent = self.parent
        while parent:
            result = f'{parent.id}_{result}'
            parent = parent.parent if parent.parent.parent != None else None
        
        return result
    
    def find(self, id_):
        for class_ in self.classes: 
            if class_.id == id_: return True

        for method in self.methods:
            if method.id == id_: return True
        
        for attr in self.attributes:
            if attr.id == id_: return True

        return False
    
    def get_inner_id(self, id_):
        parent = self
        while parent:
            if id_ in parent.imports: return parent.imports[id_]
            parent = parent.parent

        if not self.find(id_): Error(f"'{id_}' was not declared in this scope.")
        return f'{self.get_full_id()}_{id_}'
