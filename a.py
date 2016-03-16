class test(object):

    def __init__(self, value=10):
        self._x = value
    
    def x(self):
        print self._x
        return self._x

    x = property(x)