import random 
 
def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low, high):
 
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
 
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
 

 
 
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
 
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

#  Generating array for desired output:
 
array1 = [] #Ascending order array
array3 = [] # Randomly ordered
for i in range(1,101):
    array1.append(i)
print("Before Sort array1: {}".format(array1))

def Reverse(lst):
    lst.reverse()
    return lst

array2 = Reverse(array1)
print("Before Sort array2: {}".format(array2))

for i in range(1,101): # 100 elements
    n = random.randint(1,101) # Elements in range of 100 
    array3.append(n)
print("Before Sort array3: {}".format(array3))
quickSort(array1, 0, (len(array1) - 1))
print("First 10 element of array1: {} \n Last 10 element of array1: {}".format(array1[:10],array1[-10:]))
quickSort(array2, 0, (len(array2) - 1))
print("First 10 element of array2: {} \n Last 10 element of array2: {}".format(array2[:10],array2[-10:]))
quickSort(array3, 0, (len(array3) - 1))
print("First 10 element of array3: {} \n Last 10 element of array3: {}".format(array3[:10],array3[-10:]))
