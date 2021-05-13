class Block:
    def __init__(self):
        self.block = []
    
    def add_statement(self, stt):
        self.block.append(stt)
    
    def to_c(self):
        result = '{\n'

        for st in self.block:
            result += '\t' * (st.indent + 1) + st.to_c() + ";\n"

        result += '}\n'

        return result
