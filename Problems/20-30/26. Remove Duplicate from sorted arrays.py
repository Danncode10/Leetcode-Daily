class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums is already sorted
        n = len(nums)
        k = 1  # where unique elemt should go

        for i in range(n - 1):
            if nums[i] != nums[i + 1]:
                nums[k] = nums[i + 1]
                r = nums[i + 1]
                k += 1

        return k

