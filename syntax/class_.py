from .container import Container


class Class(Container):
    def __init__(self, init, parent):
        super().__init__(init.id, parent)
        self.init = init
    
    def __repr__(self):
        return f"[Class {self.init.id}]"
    
    def make_c_constructor(self):
        full_id = self.get_full_id()

        result = f'{full_id}* _{full_id}_init() ' + '{\n'

        result += f'\t{full_id}* self = _new_instance({full_id});\n'

        for method in self.methods:
            result += f'\tself -> {method.id} = &{method.get_full_id()};\n'

        result += '\treturn self;\n'

        result += '}\n'

        return result

    def to_c(self):
        full_id = self.get_full_id()

        result = f'// class {self.id}\n'

        result += f'typedef struct _{full_id} {full_id};\n'

        result += f'struct _{full_id} ' + '{\n'

        for method in self.methods:
            result += f'\t{method.get_pointer()};\n'

        result += '};\n'

        result += '\n'

        for method in self.methods:
            result += method.get_prototype() + ';\n'

        result += '\n'

        result += self.make_c_constructor() + '\n'
        
        for method in self.methods:
            result += method.to_c()

        return result
