#!/usr/bin/python3

"""  A module that has the classe BaseGeometry """


class BaseGeometry:
    """ BaseGeometry class """

    def area(self):
        """Exception Method """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validator method """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
