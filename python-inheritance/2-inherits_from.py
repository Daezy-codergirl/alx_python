"""
   check if the given object is an instance of a class
   also if it is inherited from the specified class

   parameters:
   obj: any python object.
   a_class: a python class or class name to compare the type
   of the object against.

   returns:
   true if the object is an instance of the subclass of the specified subclass;
   otherwise, false.
   example:
    >>> class Animal:
    ...  pass
    ...
    >>> class Dog(Animal):
    ... pass
    ...
    >>> class Cat(Animal):
    ... pass
    ...
    >>> class Bird:
    ... pass
    ...
    >>> obj1 = Dog()
    >>> obj2 = Cat()
    >>> obj3 = Bird()
    >>>
    >>> inherits_from(obj1, Animal)
    True
    >>> inherits_from(obj2, Animal)
    True
    >>> inherits_from(obj3, Animal)
 """


def inherits_from(obj, a_class):
    """Check if the given object is an instance of the specified class
    or inherited from it."""
    return (
        issubclass(type(obj), a_class) and type(obj) != a_class
    )