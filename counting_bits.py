# Problem: https://leetcode.com/problems/counting-bits/

# Using the trick that the bitwise and between two numbers n and n-1 will result in 0 if the number of bits set in n is 1
# Else the number of bits set is more than 1. But after performing the and operation the number of bits set is decreased by 1. 
# Now the number of bits set is the number for which we have calculated the bits already since its smaller + 1

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        if num == 0:
            return [0]

        result = []
        result.append(0)
        result.append(1)
        
        for i in range(2,num+1):
            temp = i & i-1
            if temp == 0:
                result.append(1)
            else:
                result.append(result[temp]+1)
        
        return result
