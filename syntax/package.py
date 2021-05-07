class Package:
    def __init__(self, id_, classes, methods, attributes):
        self.id         : str       = id_
        self.classes                = classes
        self.methods                = methods
        self.attributes             = attributes
