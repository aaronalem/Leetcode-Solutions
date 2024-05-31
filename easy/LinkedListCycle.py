# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#Iterate through the linked list and use Floyd's cycle detection algorithm to determine if there is a cycle.
#Catch AttributeError exceptions to see if the list has an end. If it does, there is no cycle


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except AttributeError:
            return False

