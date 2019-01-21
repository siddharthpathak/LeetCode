#Problem: https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        slow=fast=head
        
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        
        # Slow is pointing at the middle of the linked list
        # Fast is pointing at the end of the linked list
        # If fast is not pointing to None then the there are odd numboer of elements
        # We don't need to check the middle element for palindrome
        
        if fast is not None:
            slow = slow.next
        
        #Reverse the second half of the linked list
        
        current = slow
        prev = None
        
        while current is not None:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        
        current = prev
        slow = head
        
        while prev is not None:
            if slow.val != prev.val:
                return False
            slow = slow.next
            prev = prev.next
        
        return True
