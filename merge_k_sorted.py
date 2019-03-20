# Leetcode:https://leetcode.com/problems/merge-k-sorted-lists/
# Push first element of each list into the heap
# The minimum element i.e. the first element in the result will be the top of heap
# Pop the top of the heap, add to the list, and push the next element from the list 
# to which the popped element belonged
# Repeat till the heap is empty


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution:
    def mergeKLists(self, lists: 'List[ListNode]') -> 'ListNode':
        if len(lists) == 0:
            return []
        
        res = ListNode(None)
        curr = res
        min_heap = []
        count =0
        for i,node in enumerate(lists):
            if node:
                heapq.heappush(min_heap,(node.val,count,node))
                count +=1
        
        while len(min_heap):
            temp = heapq.heappop(min_heap)
            curr.next = ListNode(temp[0])
            curr = curr.next
            if temp[2].next:
                count += 1
                heapq.heappush(min_heap,(temp[2].next.val,count,temp[2].next))
        
        return res.next
