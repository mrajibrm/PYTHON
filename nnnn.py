import sys 
def print_two_Smallest(no_array): 
  
    # There must be atleast two elements 
    array_size = len(no_array) 
    if array_size < 2: 
        print ("Invalid Input")
        return
  
    first = second = sys.maxsize 
    for i in range(0, array_size): 
  
        # If current element is smaller than first then update both first and second 
        if no_array[i] < first: 
            second = first 
            first = no_array[i] 
  
        # If no_array[i] is in between first and second then update second 
        elif (no_array[i] < second and no_array[i] != first): 
            second = no_array[i]; 
  
    if (second == sys.maxsize): 
        print ("No second smallest element")
    else: 
        print("[{} {}]".format(first, second))
  
# arr is a array of numbers used to find two smallest elements of an array 
arr = [12, 13, 1, 10, 34, 1] 
# Call the Function
print_two_Smallest(arr) 