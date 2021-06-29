#BINARY SEARCH IMPLEMENTED IN PYTHON
#CONDITION THE INPUT ARRAY SHOULD BE SORTED 
#time complexity is O(logn)

def binary_search(arr ,s):
    low = 0
    up = len(arr)

    y = True


    while y: 
        if low < up:
            mid = low + (up - low)//2
            if arr[mid] == s:
                print("{} is at index {}".format(s,mid)) 
                y = False
            elif arr[mid] > s:
                up = mid - 1
            elif arr[mid] < s:
                low = mid + 1
        else:
            print("Element not present")
            break

            

    



a = [1,2,3,4,5,6]

s = int(input("Enter the number to be searched: "))

binary_search(a,s)
        

#Output

#Enter the number to be searched: 5
#5 is at index 4

#Enter the number to be searched: 2
#2 is at index 1

#Enter the number to be searched: 10 
#Element not present



