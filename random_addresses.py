import random

def generate_random_numbers_for_length_of_list(list_hardcoded_locations, number_of_orders):
    '''This function accepts a hardcoded list of addresses and an integer 
    (number_of_orders) and it returns a list with random numbers. The number
    of elements on the list is equal to number_of_orders'''
    l = []
    length_of_list = len(list_hardcoded_locations)
    for i in range(number_of_orders):
        l.append(random.randint(0,length_of_list-1))
    return l
    
def generate_random_address_list(random_numbers_list, hardcoded_addresses_list, vendors = False): 
    '''On this function you feed it a list of random numbers (generated from :
    generate_random_numbers_for_length_of_list() ), the hardcoded addresses list
    from either the vendors or consumers module and let it know if you are passing
    either a vendors or consumers list. The reason you have to differentiate from
    the consumers or vendors list is because the consumers list is a list of 
    tuples (google maps api understands each tuple as a set of coordinates for a location)
    and the vendors list is a list of tuples with the first element of the tuple 
    being the name of the vendor and the second entry in the tuple is the addresses
    of that location. The function returns a random list of addresses from the 
    provided list of hardcoded addresses
        '''
    random_addresses_list = []
    if vendors == False:
        for i in range(len(random_numbers_list)):
            random_addresses_list.append(hardcoded_addresses_list[random_numbers_list[i]])
    else:    
        for i in range(len(random_numbers_list)):
            random_addresses_list.append(hardcoded_addresses_list[random_numbers_list[i]][1])
    return random_addresses_list
  

