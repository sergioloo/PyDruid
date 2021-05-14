from .container import Container
from .statement import Statement


class Access(Statement):
    def __init__(self, obj, member, container):
        super().__init__(self.ST_ACCESS, container)

        self.object = obj
        self.member = member

    def to_c(self):
        return f'{self.object.to_c()} -> {self.member.value}'
