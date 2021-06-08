"""
LINEAR SEARCH IMPLEMENTED IN PYTHON
Time complexity is O(n)
Array dont need to be sorted 
"""

a = [5,6,2,3,4,7,9,2]
y = True
val = int(input("Enter the number to be searched: "))


for i in range(len(a)-1):
    if a[i] == val:
        print("{} is at index {}".format(val,i))
        y = False


if y:
    print("Not present")


"""
Output:

Enter the number to be searched: 10
Not present

Enter the number to be searched: 5
5 is at index 0

"""

