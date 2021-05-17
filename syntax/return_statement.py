from .statement import Statement


class ReturnStatement(Statement):
    def __init__(self, **kwargs):
        Statement.__init__(self, **kwargs)
        self.value = kwargs['value'] if 'value' in kwargs else None
    
    def set_return_value(self, val):
        self.value = val
    
    def to_string(self):
        return f'return {self.value.to_string()}'
