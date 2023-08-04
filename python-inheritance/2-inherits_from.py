"""
  check if the given object is an instance of a class
  also if it is inherited from the specified class

 parameters:
 obj: any python object.
 a_class: a python class or class name to compare the type of the object against.

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
 False
 """


def inherits_from(obj, a_class):
    """ check if the given object is exactly an instance of the specified class.
        also if it is inherited from the specified class"""
    return (
        issubclass(type(obj), a_class)
          and type(obj) != a_class
    )
   