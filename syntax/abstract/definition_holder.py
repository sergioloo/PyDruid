from .code_node             import CodeNode


class DefinitionHolder(CodeNode):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
        self.definitions = []

        self.classes = []
        self.structs = []
        self.enums   = []
        self.funcs   = []
        self.macros  = []
        self.attrs   = []
