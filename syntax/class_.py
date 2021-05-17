from .symbol import Symbol
from .container import Container


class Class(Container):
    TM_CONSTRUCTOR      = 'constructor'

    def __init__(self, **kwargs):
        Container.__init__(self, **kwargs)
    
    def to_string(self, mode=Symbol.TM_DEFINITION):
        if mode == self.TM_PROTOTYPE:
            full_id = self.get_full_id()
            return f'typedef struct _{full_id} {full_id}; \n'

        elif mode == self.TM_DEFINITION:
            result = f'// Class {self.id}\n'
            full_id = self.get_full_id()

            # Añadir los prototipos de la clase
            result += self.to_string(Symbol.TM_PROTOTYPE)
            result += f'{full_id} *_{full_id}_init();\n'

            for mthd in self.methods:
                result += mthd.to_string(Symbol.TM_PROTOTYPE)

            result += '\n'

            # Generar la estructura de la clase
            result += f'struct _{full_id} ' + '{\n'

            for mthd in self.methods:
                result += f'\t{mthd.type} (*{mthd.id}) (); \n'
            
            result += '};\n\n'

            # Generar las definiciones de los métodos
            result += self.to_string(self.TM_CONSTRUCTOR) + '\n'

            for mthd in self.methods:
                result += mthd.to_string(Symbol.TM_DEFINITION)
            
            return result
        
        elif mode == self.TM_CONSTRUCTOR:
            full_id = self.get_full_id()
            result = f'{full_id} *_{full_id}_init() ' + '{\n'

            result += f'\t{full_id} *self = _new_instance({full_id});\n\n'

            for mthd in self.methods:
                result += f'\tself -> {mthd.id} = &{mthd.get_full_id()};\n'

            result += '\n\treturn self;\n'

            result += '}\n'

            return result
