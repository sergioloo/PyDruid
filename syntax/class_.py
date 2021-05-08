class Class:
    def __init__(self, initializer, attributes=None, methods=None):
        self.initializer    = initializer
        self.attributes     = attributes if attributes else []
        self.methods        = methods    if methods else []

    def add_attribute(self, attr):
        self.attributes.append(attr)
    
    def add_method(self, method):
        self.attributes.append(method)
