class A:
    pass

class B:
    pass

class X(A, B):
    pass

class Y(B, A):
    pass

class Z(X, Y):
    """Inconsistent method resolution order for class 'Z' pylint"""
    pass

"""TypeError: Cannot create a consistent method resolution order (MRO) for bases A, B"""
