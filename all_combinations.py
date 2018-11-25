# generate all combinations of N items. This is generator/

# For N = 3 is i in binary form as follows:
#
# 000
# 001
# 010
# 011
# 100
# 101
# 110
# 111
#
# In cycle with j are bits shifted to right side. Test % 2 == 1 is testing if the last bit is 0 or 1. Only if it is 1 append item into the list
# Shortly on possitions where is one is used item on the corresponding position from input list


def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo


# for i in powerSet([1,2]):
#	print(i)


# Modification of above algorithm
# How many possible combinations exist when there are two bags? 
# Remember that a given item can only be in bag1, bag2, or neither bag -- it is not possible for an item to be present in both bags!

# This is solution where I'm only putting some items into bag1 resp. bag2
def powerSetTwoBags(items):
    N1 = len(items) // 2
    N = len(items)   
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo1 = []
        combo2 = []
        for j in range(N):
            # test bit jth of integer i
            if ((i >> j) % 2 == 1) and j < N1:
                combo1.append(items[j])
            if ((i >> j) % 2 == 1) and j >= N1:
                combo2.append(items[j])    
        yield (combo1, combo2)


#for i in powerSetTwoBags([1,2]):
#	print(i)


# Right answer is:
def yieldAllCombos(items):
    """
    Generates all combinations of N items into two bags, whereby each item is in one or zero bags.

    Yields a tuple, (bag1, bag2), where each bag is represented as a list of which item(s) are in each bag.

    There are three option how to store the items in bags:
    0 - no item in any bag
    1 - item is in bag1
    2 - item is in bag2
    3 - where item is in both bags is not valid

    e.g. combinations for two items
    00
    01
    02
    10
    11
    12
    20
    21
    22


    Therefore all possible combinations are 3**N
    """
    N = len(items)
    # Enumerate the 3**N possible combinations   
    for i in range(3**N):
        bag1 = []
        bag2 = []
        # It's quite clear, with 3**j we are just moving digit on jth place to the right and afterwards with % operator we are finding if it is either 1 or 2        
        for j in range(N):
            if (i // (3 ** j)) % 3 == 1:
                bag1.append(items[j])
            elif (i // (3 ** j)) % 3 == 2:
                bag2.append(items[j])
        yield (bag1, bag2)



for i in yieldAllCombos([1,2]):
	print(i)
