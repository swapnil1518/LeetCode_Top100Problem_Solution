# complexity of this program is n^2


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums) - 1):              # this loop will run n-1 times
            for j in range(i + 1, len(nums)):       # this loop will take next elements in array after i
                if nums[i] + nums[j] == target:     # returning index
                    return ([i, j])


# Q. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
#
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
