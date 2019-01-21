#Problem: https://leetcode.com/problems/boats-to-save-people/

#Uses Greedy approach

class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """

        people.sort()
        low = 0
        ans = 0
        high = len(people)-1
        
        while low<=high:
            if people[high] + people[low] <= limit:
                low += 1
            high -= 1
            ans += 1

        return ans     
