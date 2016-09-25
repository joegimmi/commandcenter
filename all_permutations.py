'''This module creates all the possible permutations of addresses INDEXs using 
colloquial names such as PU0 and DO0 for pickup address index 0 and dropoff 
address index 0. Notice how these are just permutations of those strings 
PU0, PU1, DO0, DO1, etc. These permutation then get "sniffed" for the ones
who are gimmi valid (every DOn is correctly preceded by its corresponding PUn)
although that organization is done at the XXXXXXX module. That module generates
a list of lists and those PUns, and DOns are used as guides for accessing
the pickup and dropoff lists to obtain the total travel time for each permutation
at the googlemapapi module.'''

from itertools import permutations

def generate_dummies(iterable, name, amount):
    '''Generate a list of dummy variables to test permutations'''
    for i in range(amount):
        iterable.append(name+str(i))

def all_possible_permutations(compiled_list):
    '''This functions returns a list of lists of all the possible permutations
    of the elements of compiled_list'''
    all_permutations_list = []
    permus_compiled = permutations(compiled_list)
    for i in permus_compiled:
        all_permutations_list.append(i)
    return all_permutations_list
