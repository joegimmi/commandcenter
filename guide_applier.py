'''This module decodes the guide created from gimmi_routes module and it translates
each possible gimmi_route into a list of totals amount of time and distance. 
It then ranks this list by the fastest route.'''

#So I have the list of lists gimmi routes. 
#I have the list of pickup_addresses
#I have the list of dropoff_addresses

#I need to be able to enter something like address('PU1') and get the address in return

def stripper(text_to_strip, identifier):
    '''Strips the text part out of an address identifier and returns the integer
    section. For example, if you enter "PU0" it will return 0 int'''
    return int(text_to_strip.strip(identifier))

#Now I need a function that relates PU with pickup addresses and DO with dropoff
#I have a list of pickupaddress and dropoff addresses, I have lists of PU0s, 
#I want to create a list of duration(minutes),distance(miles) tuples that references each
#one of those lists
#[[PU1, PU0, DO1, DO0], ...]
#Now I want to make add at the end of that list a tuple with (duration, distance).

#1. Access each list in [[PU1, PU0, DO1, DO0], ...]
#2. Relate each entry to an actual address i.e. create a function where you enter
# 'PU1' and it returns that address in the pickup lists
#3. Enter that address in the gmaps function and keep iterating through 
# [[PU1, PU0, DO1, DO0], ...] until complete and create a new dictionary that has
# the index of the list of lists of routes as key and the tuple duration, distance
# as its value. 