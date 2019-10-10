# -*- coding: utf-8 -*-
import doctest

class Calculator(object):
    def __init__(self, l, r):
        self.l = l
        self.r = r

    def plus(self):
        """
           >>> a = 1
           >>> b = 2
           >>> d = a+b
           >>> c = Calculator(1,2)
           >>> c.plus()
           3
        """
        return self.l + self.r

    def minus(self):
        return self.l - self.r

    def div(self):
        return self.l/self.r

    def mul(self):
        return self.l * self.r

    def get_items(self):
        return (self.l, self.r)

c = Calculator(1,2)

print(c.plus())

if __name__ == "__main__":
    #doctest.testmod(verbose = True)
    doctest.testfile("my_tests.txt",verbose = True)
