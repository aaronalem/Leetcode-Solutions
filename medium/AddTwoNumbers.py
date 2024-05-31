# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        dummy = ListNode()
        head = dummy
        carry = 0
		
		# while there are numbers in either list or something to carry
        while l1 or l2 or carry:
            x1 = 0
            x2 = 0
            if l1:
                x1 = l1.val
                l1 = l1.next
            if l2:
                x2 = l2.val
                l2 = l2.next
			
			# add the two values in the two corresponding nodes in the lists
			# and take the 10 modulo to find the number that should be in
			# that specific node.
            value = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10 # do the same and divide by 10 to find if you need to you have to carry
		
            
            dummy.next = ListNode(value)
            dummy = dummy.next
        
        return head.next