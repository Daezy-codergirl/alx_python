from rectangle import Rectangle
"""
the class Square is inheriting from Rectangle
"""

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        #size will stand for width & height
        
        super().__init__(size, size, x=0, y=0, id=None)
        # I won't change width and height to size because size isn't defined due to inheritance
        return "[Square] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)