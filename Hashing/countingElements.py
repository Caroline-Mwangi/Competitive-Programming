# Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr. If there are duplicates in arr, count them separately.

# Example 1:

# Input: arr = [1,2,3]
# Output: 2
# Explanation: 1 and 2 are counted cause 2 and 3 are in arr.
# Example 2:

# Input: arr = [1,1,3,3,5,5,7,7]
# Output: 0
# Explanation: No numbers are counted, cause there is no 2, 4, 6, or 8 in arr.
 
# Constraints:

# 1 <= arr.length <= 1000
# 0 <= arr[i] <= 1000

class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        my_dict={}
        count = 0
        
        for i in range(len(arr)):
            x = arr[i] + 1
            my_dict[i] = x
        for key, value in my_dict.items():
            if value in arr:
                count += 1
        return count

# Time complexity: O(n^2) - A hashset can be used to reduce this to O(n) as shown below
# Space complexity: O(n)

class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        my_set=set(arr)
        count = 0
        for i in range(len(arr)):
            x = arr[i] + 1
            if x in my_set:
                count += 1
        return count