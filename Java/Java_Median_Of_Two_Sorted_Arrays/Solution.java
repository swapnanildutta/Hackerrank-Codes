/*
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000
Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
*/

import java.util.*;

public class Solution {

    public static void main(String[] args) {
      int[] nums1 = new int[] {5, 6, 7};
      int[] nums2 = new int[] {9, 10, 11};

      double result = findMedianSortedArrays(nums1, nums2);
      System.out.println("The Median is " + result);
    }

    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        //merged array
        int[] merge = new int[nums1.length + nums2.length];
        //keep track of index
        int pos = 0;
        //add values
        for (int val : nums1) {
            merge[pos] = val;
            pos++;
        }
        for (int val : nums2) {
            merge[pos] = val;
            pos++;
        }
        //sorted array
        Arrays.sort(merge);
        //find median
        double median = 0;
        if (merge.length % 2 != 0) {
            int indexOfMedian = merge.length / 2;
            median = (double) merge[indexOfMedian];
        }
        else {
            median = (double) (merge[merge.length / 2] + merge[merge.length / 2 - 1]) / 2;
        }
        return median;
    }

}