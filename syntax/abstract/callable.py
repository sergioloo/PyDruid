from .code_node import CodeNode


class Callable(CodeNode):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.args = []
    
    def add_arg(self, arg): self.args.append(arg)
