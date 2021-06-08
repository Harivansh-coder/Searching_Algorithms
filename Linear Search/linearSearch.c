/*
1> Linear Search is a searching algorithm that iterrates through the entire array in 
   search of element asked.
2> No sorted array is needed.
3> It has an time complexity of O(n).
*/
#include<stdio.h>

int linearSearch(int arr[],int s,int val);

void main()
{	

	int val;
	
	int arr[] = {1,2,3,4,6,6,4,2,62,3,5,4,7};
	
	printf("Enter the element to be searched: ");
	scanf("%d",&val);
	int result = linearSearch(arr,13,val);	
	(result == -1)?printf("The element is not present inthe array"):printf("%d is at index %d",val,result);
}


int linearSearch(int arr[],int s,int val)
{
	for (int i = 0; i < s;i++){
		if (arr[i] == val){
			return i;
		}
	}

	return -1;

}

/*

Enter the element to be searched: 1
1 is at index 0
Enter the element to be searched: 10
The element is not present inthe array
Enter the element to be searched: 5
5 is at index 10
*/
