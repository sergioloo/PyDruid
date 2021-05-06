from utils import Error


class ContextNode:
    CNT_ROOT        = 'root file'
    CNT_PKG         = 'package'
    CNT_CLASS       = 'class'
    CNT_ATTR        = 'attribute'

    CNVB_PUBLIC     = 'public'
    CNVB_PROTECTED  = 'protected'
    CNVB_PRIVATE    = 'private'

    def __init__(self, id_, type_, visibility=CNVB_PUBLIC, parent=None):
        self.id         = id_
        self.type       = type_
        self.visibility = visibility
        self.parent     = parent

        self.indent     = parent.indent + 1 if parent else None
        self.scope      = []
    
    def register(self, id_, type_, visibility):
        self.scope.append(
            ContextNode(id_, type_, visibility)
        )
    
    def contains(self, id_):
        # Comprobar en el mismo nodo
        for cn in self.scope:
            if cn.id == id_: return True
        
        # Si no se ha encontrado, buscar en el nodo padre
        if self.parent: return self.parent.contains(id_)

        # Sino, pues que no, vaya
        return False
    
    def retrieve(self, id_, pos=None):
        # Comprobar en el mismo nodo
        for cn in self.scope:
            if cn.id == id_: return cn
        
        # Si no se ha encontrado, buscar en el nodo padre
        return self.parent.retrieve(id_, pos)

        # Si ni con esas aparece, soltar un error
        Error(f"'{id_}' was not declared in this scope.", pos=pos)
