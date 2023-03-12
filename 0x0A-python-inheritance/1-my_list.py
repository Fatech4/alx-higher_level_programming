#!/usr/bin/python3

""" A module that has a class and a subclass """


class MyList(list):
    """ A class that inherit from list object and define a new instance method
    """
    

    def print_sorted(self):
        """ New instance method of the subclass object """
        dlist = self.copy()
        dlist.sort()
        print(dlist)
