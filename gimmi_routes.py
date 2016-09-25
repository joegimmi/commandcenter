'''This module ultimate creates a list of lists that are a guide. The list 
consists of entries like PU1, DO1, etc. '''

def acceptable(lst, pickup_string = 'PU', dropoff_string = 'DO'):
    '''Is the list acceptable in the sense that every DOn comes after its
    respective PUn?'''
    acceptable_list = True
    all_true = []
    for i in lst:
        #Now I am accessing individual elements
        #I need to identify every PUn in every list and then  
        length_pickup_string = len(pickup_string)
        length_dropoff_string = len(dropoff_string)
        
        #if the first strings of the list element are equal to the pickup_string,
        #then strip out the pickup_string section and determine what number index
        #it is.
        dropoff_after = False
        if i[:length_pickup_string] == pickup_string:
            index_str_format = i.strip(pickup_string)
            #Now look for the following 'DO' and make sure it is after.
            length_of_list = len(lst)
            index_of_current_element = lst.index(i)

            #Looking after the position of the current index
            for item in lst[index_of_current_element:]:
                if item[:length_dropoff_string] == dropoff_string:
                    #Now check that the index number following 'DO' is the same as 'PU'
                    do_stripped = item.strip(dropoff_string)
                    if do_stripped == index_str_format:
                        dropoff_after = True
            
            #If the DOn was found after, we have another 'true' occurrence
            all_true.append(dropoff_after)
        
        #Now check the all_true list and make sure all elements are true, 
        #Otherwise this is not an acceptable list.
        for i in all_true:
            if i == False:
                acceptable_list = False
    return(acceptable_list)
    
def return_gimmi_routes(list_of_lists):
    '''Check list of lists to strip only the sub-lists that have produce
    a True value in acceptable function. It returns a list of lists with the
    ones the individual lists that return True in acceptable().'''
    acceptable_lists = []
    for lst in list_of_lists:
        if acceptable(lst):
            acceptable_lists.append(lst)
    return acceptable_lists
    
class Gimmi_Route():
    '''The all_acceptable_routes list, because it is part of the
    class definition, is shared by all instances of this class. That means
    there is only ONE Gimmi_Route.all_acceptable_routes list,
    and if you call self.all_acceptable_routes on any one object, it will 
    refer to that single list. '''
    all_gimmi_routes = [] #PU1, PU0, etc.
    #Then I will need the list of all the pickup locations. So what does PU1 refer to?
    #I will also need the list of dropoff locations. What does DO1 refer to?
    
    def __init__(self, route, duration, distance):
        self.route = route
        self.duration = duration
        self.distance = distance
        Gimmi_Route.all_gimmi_routes.append(self)