"""
Following function returns the index of the user entered element.
Fibonacci search needs a sorted array as input
It has time complexity of O(logn)
"""

def fiboSearch(arr, x, n):
 
    # fibonacci series
    term1 = 0  
    term2 = 1  
    num = term1 + term2  
 
    while (num < n):
        term1 = term2
        term2 = num
        num = term1 + term2
 
    offset = -1
 
    while (num > 1):
        i = min(offset+term1, n-1)
 
        if (arr[i] < x):
            num = term2
            term2 = term1
            term1 = num - term2
            offset = i

        elif (arr[i] > x):
            num = term1
            term2 = term2 - term1
            term1 = num - term2
        else:
            return i
 
    
    if(term2 and arr[n-1] == x):
        return n-1
 
    # if element not found
    return -1
 
 

arr = [2,4,6,8,10,12,14,16,18,20]
x = int(input("Enter the element: "))
index = fiboSearch(arr, x,len(arr) )
if index >= 0:
  print("Found at index:",index)
else:
  print(f"{x} is not present in the array")
 
"""
# OUTPUT

    Enter the element: 20
    Found at index: 9

    Enter the element: 21
    21 is not present in the array
    
"""