"""
check if the given object is exactly an instance of the specified class.else

 parameters:
 obj: any python object.
 a_class: a python class or class name to compare the type of the object against.object

 returns:
  boo1: true if the object is an instance of the specified class; otherwise, false.
 
 example:
>>> class MyClass:
...  pass
...
>>> obj1 = MyClass()
>>> obj2 = "Hello"
>>> obj3 = 42
>>>
>>> is_same_class(obj1, MyClass)
True
>>> is_same_class(obj2, str)
True
>>> is_same_class(obj3, list)
False

"""
def is_same_class(obj, a_class):
    """ check if the given object is exactly an instance of the specified class.
    """
    return type(obj) is a_class
   