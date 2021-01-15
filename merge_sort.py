import random

def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              # The value from the left half has been used
              myList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

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
mergeSort(array1)
print("First 10 element of array1: {} \n Last 10 element of array1: {}".format(array1[:10],array1[-10:]))
mergeSort(array2)
print("First 10 element of array2: {} \n Last 10 element of array2: {}".format(array2[:10],array2[-10:]))
mergeSort(array3)
print("First 10 element of array3: {} \n Last 10 element of array3: {}".format(array3[:10],array3[-10:]))