/*

*/

import java.util.Scanner;

class binSerOccur{

    private int binarySearch(int[] arr,int val,int l,int h,int flag){
        
        int result = -1;

        while (l <= h){
            int mid = l + (h - l)/2;

            if (arr[mid] == val){
                result = mid;
                if (flag == 0){
                    h = mid - 1;
                }else{
                    l = mid + 1;
                }
            }else if (arr[mid] > val){
                h = mid - 1;
            }else if (arr[mid] < val){
                l = mid + 1;
            }

        }

        return result;
    }
    public static void main(String[] args) {

        int[] arr = {1,2,3,4,5,5,6,7,8,9};
        
        System.out.print("Enter the element to be searched: ");
        Scanner sc = new Scanner(System.in);
        int val = sc.nextInt();

        binSerOccur bs = new binSerOccur();

        int r = bs.binarySearch(arr,val,0,arr.length-1,1);  // funtion call for last occurrence

        //int r = bs.binarySearch(arr,val,0,arr.length-1,0); // funtion call for first occurrence

        if (r == -1){
            System.out.print("Element not present");
        }else{
            System.out.print("Element is at index "+r);
        }

        sc.close();
        
        

    }
}

/*
# OUTPUT
# flag = 1
# gives the index of last occurrence of asked element 

    Enter the element to be searched: 5
    Element is at index 5

# flag = 0
# gives the index of first occurrence of asked element

    Enter the element to be searched: 5
    Element is at index 4

*/