"""
Difference between static and class methods in Python

Static Method:

    A static method doesn’t depend on the class itself or an instance of the class.
    It can be called on a class itself or an instance of the class.
    It's defined using the @staticmethod decorator.
    It doesn't have access to the instance (self) or the class (cls) itself.

Class Method:

    A class method is bound to the class and not the instance of the class.
    It can modify the class state that applies across all instances of the class.
    It's defined using the @classmethod decorator.
    It has access to the class (cls) but not to the instance (self).

"""