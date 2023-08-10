"""
The class rectangle is inheriting from class Base
"""

class Rectangle(Base):
    """Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=o, id=None):
        """initialize the rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """get the width of the rectangle"""
            return self.__width
        
        @width.setter
        def width(self, value):
            """set the width of the rectangle"""
            self.__width = value
        