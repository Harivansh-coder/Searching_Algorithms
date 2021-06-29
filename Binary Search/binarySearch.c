/*
1> Binary Search is a searching algorithm that works on Divide and Conquer principle.
2> It has an time complexity of O(logn).
3> Array should be sorted(ascending or descending).
*/

#include<stdio.h>

int binarySearch(int arr[],int l, int r,int val);

void main()
{	
	int val;
	//const int size = 10;

	int a[] = {1,2,3,4,5,6,7,8,9,10};
	printf("Enter the number to be searched: ");
	scanf("%d",&val);
	
 	int result = binarySearch(a,0,10,val);

	(result == -1)?printf("Asked number is not present in the array."):printf("%d is at index %d",val,result);

}

int binarySearch(int arr[],int l, int r,int val){
	
	if (r >= l){
		int mid = l+(r-l)/2;

		if (arr[mid] == val){
			return mid;
		}
		else if (arr[mid] > val){
			return binarySearch(arr,l,mid-1, val);
		}
		else if (arr[mid] < val){
			
			return binarySearch(arr,mid+1 ,r,val);
		}
	}
	
	return -1;
}

/*
Output:

Enter the number to be searched: 5
5 is at index 4
Enter the number to be searched: 10
10 is at index 9
Enter the number to be searched: 15
Asked number is not present in the array

*/
