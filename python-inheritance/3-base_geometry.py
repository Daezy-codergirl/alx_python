"""
   a base class representing geometry.

   this class is intended to be used as a base for other geometry-related classes.
   it currently does not have any attributes or methods defined.
"""

class BaseGeometry:
    """
    a base class representing geometry.
    """

class BaseGeometryMetaClass(type):
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    
class BaseGeometry(metaclass=BaseGeometryMetaClass):
    """
    a base class representing geometry
    """
    def __dir__(self):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']