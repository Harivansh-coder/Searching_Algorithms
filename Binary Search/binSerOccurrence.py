"""
Following function returns the first or last (index) occurrence of 
the user entered element depending upone flag parameter.
If flag is 0 it returns the index of first occurrence of the element 
and else it returns last occurrence. 
"""

def binarySearch(arr ,val,flag):
    low = 0
    up = len(arr) - 1

    result = -1

    while low <= up:
        mid = low + (up - low)//2
        if arr[mid] == val:
            result = mid
            if flag == 0:
                up = mid - 1
            else :
                low = mid + 1 

        elif arr[mid] > val:
            up = mid - 1
        elif arr[mid] < val:
            low = mid + 1
        
    return result


arr = [1,2,3,4,5,6,7,8,9]
a = binarySearch(arr,int(input("Enter a number to be searched: ")),0)

if a == -1:
    print("Element not present")
else:
    print(f"Element is at {a}")

"""
# OUTPUT

Enter a number to be searched: 5
Element is at 4

Enter a number to be searched: 10
Element not present

"""


