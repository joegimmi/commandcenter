import gimmi_routes
import consumers
import vendors
import random_addresses
import all_permutations
import guide_applier

if __name__ == "__main__":
    #SETUP VARIABLES:
    NUMBER_ORDERS = 3
    print('Number of orders: ' + str(NUMBER_ORDERS))
    #END SETUP VARIABLES
    
    #GENERATING RANDOM PICKUP/DROPOFF ADDRESSES LISTS
    
    random_vendors_addresses = []
    random_consumer_addresses = []
    random_numbers_list_vendors = random_addresses.generate_random_numbers_for_length_of_list(vendors.vendors, NUMBER_ORDERS)
    random_numbers_list_consumers = random_addresses.generate_random_numbers_for_length_of_list(consumers.consumers, NUMBER_ORDERS)
    pickups = random_addresses.generate_random_address_list(random_numbers_list_vendors, vendors.vendors, vendors = True)
    dropoffs = random_addresses.generate_random_address_list(random_numbers_list_consumers, consumers.consumers, vendors = False)
    
    if len(pickups) != len(dropoffs):
        print('WARNING: discrepancy found on random generators.')
    #END OF GENERATING RANDOM PICKUP/DROPOFF ADDRESSES LISTS 
    
    #GENERATING ALL POSSIBLE PERMUTATIONS OF UPnS AND DOnS BASED ON NUMBER OF ORDERS
    PU = []
    DO = []
    all_permutations.generate_dummies(PU, 'PU', NUMBER_ORDERS)
    all_permutations.generate_dummies(DO, 'DO', NUMBER_ORDERS)
    compiled_list = PU + DO
    all_possible_permutations_list = all_permutations.all_possible_permutations(compiled_list)
    
    answer = input('Do you want to print all possible permutations and if they are gimmi acceptable? y/n')
    if answer == 'y':
        for l in all_possible_permutations_list:
            print(str(l) + ' acceptable :' + str(gimmi_routes.acceptable(l)))
            
    gimmi_route_guide = gimmi_routes.return_gimmi_routes(all_possible_permutations_list)
    print('The acceptable routes are: ')
    for i in gimmi_route_guide:
        print(i)
        
    print('####################################################################')
    print('Excuse me will I obtain the results for all the gimmi routes.')
    print('It will take a minute to make all the API requests and calculate them!')
    print('####################################################################')
    #Up to now in the command center, I have created a list of routes called
    #gimmi_route_guide.
    #Now, I am going to determine which one has the smallest duration in the
    #Following fashion:
    
    #I import gmapsapifuncs module created:
    import gmapsapifuncs
    
    all_results = gmapsapifuncs.do_it_all_for_me(gimmi_route_guide, pickups, dropoffs)
    #all_results = [the_dic, the_tuple]
    #the_tuple = (dictionary_key, duration, distance)
    if input('Do you want to see a printout of all results? y') == 'y':
        for i in all_results[0]: 
            #So 'i' is purely the dictionary key, not the dictionary itself
            #dic[i] = (duration, distance)
            print('route : ', i, ' | ', 'duration(min): ', all_results[0][i][0], ', distance(mi); ', all_results[0][i][1])
            
    print('\nThe best route is:')
    print('Route: ', all_results[1][0]) #That's giving me the best route
    print(gimmi_route_guide[all_results[1][0]] ) 
    
    print('Duration (minutes) :')
    print(all_results[1][1])
    print('Distance (miles) : ')
    print(all_results[1][2])
    print(all_results[1][1],',', all_results[1][2])
    
  