"""
   a base class representing geometry.

   this class is intended to be used as a base for other geometry-related classes.
   it currently does not have any attributes or methods defined.
"""

class BaseGeometry:
    """
    a base class representing geometry.

    this class is intended to be used as a base for other geometry-related classes.
    it currently does not have any attributes or methods defined.
    """

class BaseGeometryMetaClass(type):
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    
class BaseGeometry(metaclass=BaseGeometryMetaClass):
    """
    a base class representing geometry
    """
    def __dir__(self):
        """customization of the attributes visible when calling 'dir()'
        """
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    
    def area(self):
       """
       calculate the area of the geometry.

       raises:
           NotImplementedError: this methos is not implemented in the base class.
       """
       raise Exception("area() is not implemented")