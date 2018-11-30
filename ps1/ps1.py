###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time
import os
from collections import OrderedDict
from ps1_partition import get_partitions



#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # Create ordered list od cows (heaviest first -> reverse = True)
    ordered_cows = OrderedDict(sorted(cows.items(), key=lambda t: t[1], reverse=True))
    retVal = []

    # Pop cows from ordered_cows untill there is no cow
    while len(ordered_cows) > 0:
        totalWeight = 0
        currentTransport = []
        for cow in ordered_cows.items():            
            # Just check weight of each cow if there is not cow which could not fit
            if cow[1] > limit:
                raise ValueError("Cow '" + cow[0] + "''s weight is above the limit !")
            elif cow[1] + totalWeight < limit: # Cow fits into transporter
                currentTransport.append(cow[0])
                totalWeight += cow[1]                

        retVal.append(currentTransport)
        # Delete selected cows in this round from ordered_cows
        for i in currentTransport:
            ordered_cows.pop(i)

    return retVal


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    retVal =  None #Best combination so far

    for combination in (get_partitions(cows.keys())):
        #print(combination)
        validCombination = True
        for trip in combination:
            # For each list evaluate totalWeight. If totalWeight exceeds limit skip combination
            #print("Trip: " + str(trip))
            totalTripWeight = 0
            for cow in trip:
                totalTripWeight += cows[cow]
            if totalTripWeight > limit:
                validCombination = False
                continue

        # Compare if this combination is better than the previous one
        if validCombination == True and (retVal == None or len(combination) < len(retVal)):
            retVal = combination            
            #print("new best: " + str(retVal) + " -> " + str(len(retVal)))

    return retVal
        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""


os.chdir("c:\\Users\\255623\\Desktop\\edX\\MITx_6_00_2x\\ps1") # This is hack, just to set CWD for reading ps1_cow_data.txt file

cwd = os.getcwd()
print(cwd)

cows = load_cows("ps1_cow_data.txt")
limit=24
print(cows)


start = time.time()
print(greedy_cow_transport(cows, limit))
end = time.time()
print(end - start)


start = time.time()
print(brute_force_cow_transport(cows, limit))
end = time.time()
print(end - start)



