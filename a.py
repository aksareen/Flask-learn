#assign functions to variables
#Define functions inside other functions

#Functions can be passed as parameter to other functions
from functools import wraps
def tags(tag_name):
    def tags_decorator(func):
        @wraps(func)
        def wrpapped(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return wrpapped
    return tags_decorator

class Person(object):
    def __init__(self):
        self.name =  "John"
        self.family = "Doe"

    @tags("p")
    def get_fullname(self):
        st =  self.name + " " + self.family + "\n"
        return st

my_person = Person()
print my_person.get_fullname()
print my_person.get_fullname.__name__