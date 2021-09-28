/*
Implementation of binary search in javascript.
*/

function binarySearch(arr, item, start, end) {

        if (end >= start) {
          let mid = parseInt((end + start) / 2);

          if (arr[mid] == item)
              return mid;

          if (arr[mid] > item)
              return binarySearch(arr, item,start, mid - 1);

          return binarySearch(arr, item,mid + 1, end);
        }

    return -1;
}

// testing the binarySearch

var arr = [1,2,3,4,5,6,7,8,9,10];

var start = 0;
var end = arr.length;
var item = 11;
var loc = binarySearch(arr, item,start, end);

console.log(loc);
