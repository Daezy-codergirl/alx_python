"""
This class represent a square with a give size

Attribute:
_size(int): The size of the square(private attribute)
"""

class Square:
    """This class represents a Square with a given size

    Attribute:
    _size(int): The size of the square(private attribute)
    
    
    """

    def __init__(self, size=0):
         """
         Initialize a square object with an optional size

         Args:
             size(int): The size of the square(default is 0)
         Raises:
             TypeError: if size is not an integer
             ValueError: If the size is less than 0
          """
         if not isinstance(size, int):
              raise TypeError("size must be an integer")
         if size < 0:
              raise ValueError("size must be >= 0")
         self.__size = size

    @property
    def size(self):
         """
         @property decorator:
         Allows one to create getters and setters method for a private attribute. Enables controlled access to that attribute while maintaining encapsulation"""

         return self.__size
    

    @size.setter
    def size(self, value):
       """
       @size.setter:
       decorator used in conjuction with @property to define the setter method for a property"""

       if not isinstance(value, int):
            raise TypeError("size must be an integer")
       if value < 0:
            raise ValueError('size must be >= 0')
       self.__size = value


    def area(self):
         """
         calculate the area of the square
         return:
              int: The area of square
           """
         return self.__size ** 2
         return area(self.__size ** 2)
    
    def perimeter(self):
         """calculate the perimeter of the square
         return:
            int: the perimeter of the square
            """
         return 4 * self.__size
    
    def my_print(self):
         """prints the square using the '#' character. if the size is 0, it prints an empty line"""

         if self.__size == 0:
              print()
         else:
              for _ in range(self._size):
                  print("#" * self._size)
    def get_size(self):
         """ Gets size of square
         return:
         int: The size of the square
         """
         return self.__size
    
    def set_size(self, new_size):
         """ sets the size of the square to a new value

         Args:
         new_size (int): the new size to set

         Raises:
              TypeError: if the new size is not an integer
              ValueError: if the new size < 0
              """
         if not isinstance(new_size, int):
              raise TypeError("size must be an integer")
         if new_size < 0:
              raise ValueError("size must be >= 0")
         self.__size = new_size

         
    