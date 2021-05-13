class Block:
    def __init__(self, scope):
        self.scope = scope
        self.block = []
    
    def add_statement(self, stt):
        self.block.append(stt)
