from .code_node import CodeNode


class DefinitionHolder(CodeNode):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.classes = []
        self.structs = []
        self.enums   = []
        self.funcs   = []
        self.macros  = []
        self.attrs   = []

    def add_class(self, cls_):      self.classes.append(cls_)
    def add_struct(self, struct):   self.structs.append(struct)
    def add_enums(self, enum):      self.enums.append(enum)
    def add_func(self, func):       self.funcs.append(func)
    def add_macro(self, macro):     self.macros.append(macro)
    def add_attr(self, attr):       self.attrs.append(attr)
