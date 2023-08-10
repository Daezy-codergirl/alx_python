"""
The class rectangle is inheriting from class Base
"""

class Rectangle(Base):
    """Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """Get the width of the rectangle"""
            return self.__width
        
        @width.setter
        def width(self, value):
            """Set the width of the rectangle"""
            self.__width = value
        