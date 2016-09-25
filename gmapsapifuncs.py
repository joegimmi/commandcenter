'''Has 3 functions: 
managing info:
(distance, duration) from address a to address b
 - Have a list of potential routes, each list could be then inserted to the inside of the tuple. 
 It will be easiest to create objects that have the list of routes assigned as
 one of its self variables but then also have duration and distance variables. 
 They can then be sorted by those, and asked the appropiate route. This seems like a very
 natural application of object oriented programming :D 
1. returns the distance in miles between addresses/geocodes

# I need a function that returns the distance in miles between 2  
# The methods from the googlemaps module return the 
'''
import googlemaps
from guide_applier import stripper

gmaps = googlemaps.Client(key = 'AIzaSyDtAx-LFsfnceXD_w2bNIxKC4pT3yzXF58' )

def driving_results(are_address, going_address):
    '''returns a tuple with (duration, distance) in minutes and 
    miles respectively. Should add functions to make sure they are correct input bla
    bla'''
    result = gmaps.directions(are_address, going_address, mode = 'driving')
    
    
    duration_seconds = result[0]["legs"][0]['duration']['value'] #its returned in seconds
    distance_meter = result[0]["legs"][0]['distance']['value'] #its returned in meters
    
    #convert duration to minutes and convert distance to miles
    #1 mile = 1609.34 meters
    duration_minutes = duration_seconds/60
    distance_miles = distance_meter/1609.34
    
    return (duration_minutes, distance_miles)
    
def map_the_key_to_an_address(list_of_addresses, key):
    '''returns the address when provided it with pickup/dropoff address
    and the mapping key'''
    index = stripper(key, key[:2])
    return list_of_addresses[index]
    
def calculate_duration_distance_for_route(pickup_addresses_list, dropoff_addresses_list, route):
    '''It returns tuple(duration, distance for an ENTIRE route entry.
    Route is a single list of PU0s, DO1s. '''
    duration_minutes = 0.0
    distance_miles = 0.0
    
    for i in range(len(route)):
        
        if i != len(route)-1:
            if route[i][:2] =='PU':
                are_at = map_the_key_to_an_address(pickup_addresses_list, route[i])
            else:
                are_at = map_the_key_to_an_address(dropoff_addresses_list, route[i])
            if route[i + 1] == 'PU':
                going_to = map_the_key_to_an_address(pickup_addresses_list, route[i+1])
            else:
                going_to = map_the_key_to_an_address(dropoff_addresses_list, route[i+1])
            answers_tuple = driving_results(are_at, going_to) #(duration_minutes, distance_miles)
            duration_minutes = duration_minutes + answers_tuple[0]
            distance_miles = distance_miles + answers_tuple[1]
            
    return (duration_minutes, distance_miles)

#I can now calculate the (duration, distance) for a single route
#Now I need a function that those it for a list of routes

def create_dictionary_of_results(list_of_routes, pickup_list, dropoff_list):
    '''Return a dictionary that has as key the index that refers to a route on
    list_of_routes. The value of the key is the (duration, distance) tuple.'''
    
    dic = {}
    
    for i in range(len(list_of_routes)):
        #Each 'i' is an individual list route.
        dic[i] = calculate_duration_distance_for_route(pickup_list, dropoff_list, list_of_routes[i])
    
    return dic
        
#Now that I have a dictionary of results, it's time to determine the shortest one.
#What dictionary key has the smallest duration?

def determine_key_smallest_duration(dic):
    '''You enter the dictionary and it returns the tuple:
    (dictionary_key, duration, distance)'''
    smallest_tuple = (dic[0], dic[0][0], dic[0][1])
    for i in dic:
        if dic[i][0] < smallest_tuple[1]:
            smallest_tuple = (i, dic[i][0], dic[i][1])
    
    return smallest_tuple
    
def do_it_all_for_me(list_of_routes, pickup_addresses, dropoff_addresses):
    '''Takes the gimmi list of routes, pickup and dropoff address lists and 
    returns:
    dictionary of keys of the list_of_routes. 
    tuple with the key with the smallest duration. 
    This is returned as a list [dictionary, tuple]
    '''
    the_dic = create_dictionary_of_results(list_of_routes, pickup_addresses, dropoff_addresses)
    the_tuple = determine_key_smallest_duration(the_dic)
    return[the_dic, the_tuple]
    

    
 
    
if __name__ == "__main__":
    address1 = '2626 Thayer Dr Saint Joseph MI'
    address2 = '1191 Pearl St Benton Harbor MI'
    print(driving_results(address1, address2))
    type(driving_results(address1, address2))