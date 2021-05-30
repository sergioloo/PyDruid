from .code_node import CodeNode


class Scope(CodeNode):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.statements = []
    
    def add_statement(self, stt): self.statements.append(stt)
