from .symbol import Symbol


class Container(Symbol):
    def __init__(self, **kwargs):
        Symbol.__init__(self, **kwargs)

        self.attributes = []
        self.methods    = []
        self.classes    = []
        self.interfaces = []
        self.enums      = []
        self.structs    = []

    def add_attribute(self, attr):  self.attributes.append(attr)
    def add_method(self, mthd):     self.methods.append(mthd)
    def add_class(self, cls_):      self.classes.append(cls_)
    def add_interface(self, itrf):  self.interfaces.append(itrf)
    def add_enum(self, enum):       self.enums.append(enum)
    def add_struct(self, struct):   self.structs.append(struct)
