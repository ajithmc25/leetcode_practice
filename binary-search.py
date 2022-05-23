'''
Given an array of integers nums which is sorted in ascending order,
and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1



Constraints:

    1 <= nums.length <= 104
    -104 < nums[i], target < 104
    All the integers in nums are unique.
    nums is sorted in ascending order.

'''


from typing import List


class Solution:

    def search(self, nums: List[int], target: int, start=0, end=None) -> int:
        end = len(nums) if not end else end
        if start == end:
            return -1
        middle_raw = len(nums[start:end]) // 2
        middle = start + middle_raw
        if nums[middle] == target:
            return middle
        if middle in [0, len(nums)]:
            return -1
        if target < nums[middle]:
            return self.search(nums, target, start, middle)
        else:
            return self.search(nums, target, middle+1, end)


'''
[2,5]
0
start=0, end=2, middle=1
start=0, end=1, middle=0

[-1,0,3,5,9,12]
9
start=0, end=6, middle=3
start=4, end=6, middle=5
start=4, end=5, middle=4

[-1,0,3,5,9,12]
2
start=0, end=6, middle=3
start=0, end=3, middle=1
start=2, end=3, middle=2
start=2, end=2
'''
