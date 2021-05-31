from .function  import Function


class Constructor(Function):
    def __init__(self, cls_, **kwargs):
        super().__init__(name='new', parent=cls_)

        self.class_id       = self.parent.get_full_id()
        self.return_value   = self.class_id

    def to_string(self) -> str:
        result = f'{self.class_id} _{self.class_id}_new () ' + '{\n'

        result += f'\t{self.class_id} self = _new_instance(_{self.class_id});\n'

        for method in self.parent.funcs:
            result += f'\tself -> {method.name} = &{method.get_full_id()};\n'

        result += '\treturn self;\n'

        result += '}\n'

        return result
