from Item import Item

avail = 25

myItems = [Item("Pizza",14,26), Item("Beer",5,15), Item("Burger",21,29)]

#print(items)

# TODO 1: tidy up code (e.g. get rid of prints) -> DONE
# TODO 2: use tuple as return value instead of array to be immutable -> DONE
# TODO 3: maybe use better variable names


def getMaxVal(items,availWeight):

    # end condition, return total value if items is empty
    if len(items) == 0:
        #return totalValue, selectedItems
        return 0, ()

    # check if it is possible to add another item
    currItem = items[0]

    # if there is no room in the bag, carry on without the item
    if currItem.weight > availWeight:
        return getMaxVal(items[1:],availWeight)


    # compute value if we take the item
    withValue, withItems = getMaxVal(items[1:], availWeight - currItem.weight)
    withValue += currItem.value
    withItems = withItems + (currItem,)

    # compute value if we don't take the item
    withoutValue, withoutItems = getMaxVal(items[1:], availWeight)

    # compare and return better option
    if withValue < withoutValue:
        return withoutValue, withoutItems
    else:
        return withValue, withItems   




print(getMaxVal(myItems,avail))

