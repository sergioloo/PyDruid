from .symbol import Symbol


class TypeSymbol(Symbol):
    """
    The type symbol is a kind of symbol that can hold into itself definition for
    other different symbols. For example, a class would be a type symbol, because
    inside a class you can define pretty much everything, from classes to attributes.
    So, each definition of an object that would become a symbol will inherit from this
    object.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Contained objects
        self.classes    = []
        self.structs    = []
        self.enums      = []
        self.functions  = []
        self.macros     = []
        self.attributes = []
    
    def add_class(self, class_):    self.classes.append(class_)
    def add_struct(self, struct):   self.structs.append(struct)
    def add_enum(self, enum):       self.enums.append(enum)
    def add_function(self, func):   self.functions.append(func)
    def add_macro(self, macro):     self.macros.append(macro)
    def add_attribute(self, attr):  self.attributes.append(attr)
