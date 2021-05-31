from .code_node import CodeNode
from utils      import Error


class Definition(CodeNode):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def new(dh, obj, name, ls):
        for obj_ in ls:
            if obj_.name == name: Error(f"redefinition of {name}.")
        
        obj_ = obj(name=name, parent=dh)
        ls.append(obj_)
        dh.definitions.append(obj_)
        return obj_
