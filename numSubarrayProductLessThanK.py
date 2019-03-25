# Leetcode: https://leetcode.com/problems/subarray-product-less-than-k/
    
    
def numSubarrayProductLessThanK(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """

    start,end = 0,0
    rp = 1
    result = 0

    while end < len(nums):
        rp *= nums[end]

        while start <= end and rp >= k:
            rp = rp/nums[start]
            start += 1

        result += end - start + 1
        end += 1

    return result
