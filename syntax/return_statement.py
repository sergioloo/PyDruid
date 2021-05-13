from .statement import Statement


class ReturnStatement(Statement):
    def __init__(self, ret_val=0):
        self.value  = ret_val
    
    def set_return_value(self, val):
        self.value = val
