#In this file, we will call functions to calculate min and max.
#Using the code and data provided in Section 4.3, calculate:
#maximum (you can use the code provided to find the maximum of any 3 values) or call the built-in max().
#minimum (you can call the built-in min() function which accepts any number of arguments. Could you write your own minimum() function?
#Confirm you get the answers provided, e.g. the maximum(12, 27, 36) = max(12, 27, 36) = 36 and the min(15, 9, 27, 14) = 9. 

def max_min_value(*args):
    ''' Function returns the min and max
        values from the argument provided'''
    if all(type(item) in (int,float) for item in args):
    
        result=max(*args),min(*args)    
    else:
       
        return "Please only enter intger/float numbers"
    return "The max value is {} and the min value is {}.".format(result[0],result[1])
