from functools import total_ordering
import sys


#I used decorators for getters and setter just to practise them. I know they should not have them as I can acess them directly in Python
@total_ordering
class Item:

    def __init__(self, name, weight, value):
        self._weight = weight
        self._value = value
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def weight(self):
        return self._weight

    @property
    def value(self):        
        return self._value

    @name.setter
    def name(self, name):
        self._name = name

    @weight.setter
    def weight(self, weight):
        self._weight = weight

    @value.setter
    def value(self, value):
        self._value = value

    # To get nicer output in print function
    def __repr__(self):
        return '{}: {} {} {}'.format(self.__class__.__name__,
                                  self._name,
                                  self._weight,
                                  self._value)

    def metric1(self):
        try:
            return self._value / self._weight 
        except ZeroDivisionError as e:
            return sys.maxsize

    def metric2(self):
        return  (-1)*self._weight

    def metric3(self):
        return self._value

    # for @total_ordering decorator
    def __eq__(self, other):
        return self.metric() == other.metric()

    # for @total_ordering decorator
    def __lt__(self, other):
        return self.metric() < other.metric()
