Leetcode Problem: https://leetcode.com/problems/house-robber/

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        # We need the best/highest value of the previous two houses/arrays
        # The new house can be selected or not selected
        # If selected then we ignore the previous house but take best of the one before that
        # If not selected then the best is the best of the previous one
        memo_1 = nums[0]
        memo_2 = max(memo_1,nums[1])
        
        for i in range(2,len(nums)):
            current = max(memo_1+nums[i],memo_2)
            memo_1,memo_2=memo_2,current
        
        return memo_2
