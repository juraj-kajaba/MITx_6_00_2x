from functools import total_ordering
import sys

#Global variable to be able to switch used metric. Disadvantage of this approach is that all instances of Item must use this global parameter
used_metric = 1

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
    def weight(self, name):
        self._name = name

    @weight.setter
    def weight(self, weight):
        self._weight = weight

    @value.setter
    def value(self, value):
        self._value = value

    # To get nicer output in print function
    def __repr__(self):
        return '{}: {} {} {} {}'.format(self.__class__.__name__,
                                  self._name,
                                  self._weight,
                                  self._value,
                                  self.metric())

    def metric1(self):
        try:
            return self._value / self._weight 
        except ZeroDivisionError as e:
            return sys.maxsize

    def metric2(self):
        return  (-1)*self._weight

    def metric3(self):
        return self._value

    def metric(self):
        if used_metric == 1:
            return self.metric1()
        elif used_metric == 2:
            return self.metric2()
        elif used_metric == 3:
            return self.metric3()

    # for @total_ordering decorator
    def __eq__(self, other):
        return self.metric() == other.metric()

    # for @total_ordering decorator
    def __lt__(self, other):
        return self.metric() < other.metric()



maxCost = 14
currentCost = 0


items = [Item('Dirt', 4, 0), Item("Computer", 10, 30), Item("Fork", 5, 1), Item("Problem Set", 0, -10)]

sorted_items = sorted(items,reverse=True)
items_in_the_bag = []
print(sorted_items)

#For each item, from highest metric value to lowest, add the item if there is room in the bag.
#In this approach I have not only one item of any type but a lot of them
for item in sorted_items:
    # add item into bag while it is possible, dont't accept negative metrics
    while currentCost + item.metric() <= maxCost:
        if item.metric() <= 0:
            break
        currentCost += item.metric()
        items_in_the_bag.append(item)


print(items_in_the_bag)
print(currentCost)


#In this approach I have exactly only items in list items
def getItemsOfTheBag(sorted_items):
    currentCost = 0
    items_in_the_bag = []

    for item in sorted_items:
        if currentCost + item.metric() <= maxCost:
            currentCost += item.metric()
            items_in_the_bag.append(item)
    return items_in_the_bag


items_in_the_bag = getItemsOfTheBag(sorted_items)
print(items_in_the_bag)



#In this approach I will use functionKey of sort function instead of global parameter used_metric
def getItemsOfTheBagForMetric(keyFunction):
    sorted_items = sorted(items, key = keyFunction, reverse=True)
    items_in_the_bag = getItemsOfTheBag(sorted_items)
    return items_in_the_bag


print("Metric 1:")
print(getItemsOfTheBagForMetric(Item.metric1))

print("Metric 2:")
print(getItemsOfTheBagForMetric(Item.metric2))

print("Metric 3:")
print(getItemsOfTheBagForMetric(Item.metric3))

