/*BINARY SEARCH IMPLEMENTED IN JAVA
CONDITION THE INPUT ARRAY SHOULD BE SORTED 
time complexity is O(logn)
*/
import java.util.Scanner;

public class binarySearch {
    public static void main(String[] args) {

        int[] arr = {1,2,3,4,5,6,7,8,9,10};
        int l = 0 , h = arr.length , mid ;

        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number to be searched: ");
        int val = sc.nextInt();


        boolean y = true;
        while (y){
            if (l < h){
                mid = (l + h)/2;
                if (arr[mid] == val){
                    System.out.print(val+" is at index "+mid);
                    y = false;
                }else if(arr[mid] > val){
                    h = mid - 1;

                }else if(arr[mid] < val){
                    l = mid + 1 ;

                }
            }else{
                System.out.print("Element is absent");
                break;
            }
        }
        
       

        sc.close();
    }
    
}

/*
Output:

Enter the number to be searched: 10
10 is at index 9

Enter the number to be searched: 1
1 is at index 0

Enter the number to be searched: 11
Element is absent
*/
