"""
parameters:
 obj: any python object.
 a_class: a python class or class name to compare the type of the object against.object

 returns:
  boo1: true if the object is an instance of the specified class; otherwise, false.
 
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
>>> obj1 = Dog()
>>> obj2 = Cat
>>> obj3 = Animal
>>>
>>> is_same_class(obj1, Dog)
True
>>> is_same_class(obj2, AAnimal)
True
>>> is_same_class(obj3, Cat)
False

"""
def is_kind_of_class(obj, a_class):
    """ check if the given object is exactly an instance of the specified class.
    """
    return isinstance(obj, a_class)
   