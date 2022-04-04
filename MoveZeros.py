class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        no_of_zeros = 0
        # count the no of zeros
        for i in range(len(nums)):
            if nums[i] == 0:
                no_of_zeros += 1
        # remove the no of zeros from the list
        for i in range(no_of_zeros):
            nums.remove(0)
        # append the zeros removed to end
        for i in range(no_of_zeros):
            nums.append(0)