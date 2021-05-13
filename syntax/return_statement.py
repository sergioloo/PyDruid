from .statement import Statement


class ReturnStatement(Statement):
    def __init__(self, ret_val=0):
        super().__init__(self.ST_RETURN)
        self.value  = ret_val
    
    def set_return_value(self, val):
        self.value = val
    
    def to_c(self):
        return f'return {self.value.to_c()}'
