# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Use Floyd's cycle detection to determine if there is an cycle.
# If there is, using a pointer at the start of the list, and one at where the two pointers met, go one by one through the
# list untill the two pointers meet again. This is the start of the list
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # determine if there is a cycle using Floyd's cycle detection algo
        if not head or not head.next or not head.next.next:
            return None
        slow = head.next
        fast = head.next.next

        while slow is not fast:
            if not fast.next or not fast.next.next:
                return None
            fast = fast.next.next
            slow = slow.next

        # determine where the cycle starts
        while slow is not head:
            slow = slow.next
            head = head.next
        return slow