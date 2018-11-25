# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 07:23:37 2018

@author: Juraj Kajaba

"""

import time

def getAllWays(avail):
    """Implwmentation if problem: Count ways to reach the n’th stair

    Possible solutions for 3,4 and 5 stairs:
        3 steps -> could be 1,1,1 or 1,2 or 2,1
        4 steps -> could be 1,1,1,1 or 1,1,2 or 1,2,1 or 2,1,1 or 2,2
        5 steps -> could be 1,1,1,1,1 or 1,1,1,2 or 1,1,2,1 or 1,2,1,1 or 2,1,1,1 or 2,2,1 or 1,2,2 or 2,1,2

    @param avail Number of stairs for whitch combinations will be returned

    """
    retVal = []
    
    if avail == 0:
        return [[]]
    
    # Get combinations for 1 step
    oneStepWays = getAllWays(avail-1)  
    for i in oneStepWays:
        retVal.append(i + [1]) # append 1 to all combinations
    
    # Get combinations for 2 steps
    if avail > 1:    
        twoStepWays = getAllWays(avail-2)
        for i in twoStepWays:
            retVal.append(i + [2]) # append 2 to all combinations
        
    return retVal


# Same solution as above but with memo used
def getAllWaysMemo(memo, avail):
    """Implementation if problem: Count ways to reach the n’th stair

    Possible solutions for 3,4 and 5 stairs:
        3 steps -> could be 1,1,1 or 1,2 or 2,1
        4 steps -> could be 1,1,1,1 or 1,1,2 or 1,2,1 or 2,1,1 or 2,2
        5 steps -> could be 1,1,1,1,1 or 1,1,1,2 or 1,1,2,1 or 1,2,1,1 or 2,1,1,1 or 2,2,1 or 1,2,2 or 2,1,2

    @param memo Memory (hashmap) where are stored already computed results in order to avoid already computed results recursively
    @param avail Number of stairs for whitch combinations will be returned

    """
    
    retVal = []
    
    if avail == 0:
        return [[]]

    # Get combinations for 1 step    
    oneStepWays = memo.get(avail-1)
    
    if oneStepWays == None:
        oneStepWays = getAllWaysMemo(memo,avail-1)  
               
    for i in oneStepWays:
        retVal.append(i + [1]) # append 1 to all combinations

    
    # Get combinations for 2 steps
    if avail > 1:    
        twoStepsWays = memo.get(avail-2)
        
        if twoStepsWays == None:                    
            twoStepsWays = getAllWaysMemo(memo,avail-2)
        
        for i in twoStepsWays:
            retVal.append(i + [2]) # append 2 to all combinations            
                
    memo[avail] = retVal        
        
    return retVal


# Test how long it will take        
steps_num = 31

start_time = time.time()
print(len(getAllWays(steps_num)))
print(time.time() - start_time)

memo = {}

start_time = time.time()
print(len(getAllWaysMemo(memo, steps_num)))
print(time.time() - start_time)

