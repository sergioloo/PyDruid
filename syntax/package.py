from .accessibility import Accessibility
from .symbol import Symbol


class Package(Symbol):
    """
    The package, as its most basic form, is pretty much a symbol whose accessibility
    is always public, because it's declared at the second level of the AST.
    So, the accessibility attribute is forced to be public at the constructor.
    It also holds all kinds of definitions, excepting attributes. Only constants.
    Because of this, among many other obvious reasons, the package doesn't inherit
    from TypeSymbol.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.accessibility = Accessibility.public()
    
        # Contained definitions
        self.classes    = []
        self.structs    = []
        self.enums      = []
        self.functions  = []
        self.macros     = []
        self.constants  = []
    
    def add_class(self, class_):    self.classes.append(class_)
    def add_struct(self, struct):   self.structs.append(struct)
    def add_enum(self, enum):       self.enums.append(enum)
    def add_function(self, func):   self.functions.append(func)
    def add_macro(self, macro):     self.macros.append(macro)
    def add_const(self, const):     self.constants.append(const)
