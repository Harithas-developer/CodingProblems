# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

  
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        ptr = head
        
        while True:
            if l1 is None and l2 is None:
                break;
            
            elif l1 is None:
                ptr.next = l2
                break
            
            elif l2 is None:
                ptr.next = l1
                break
            
            else:
                small = 0
                if l1.val < l2.val:
                    small = l1.val
                    l1 = l1.next
                else:
                    small = l2.val
                    l2 = l2.next
                
            newNode = ListNode(small)
            ptr.next = newNode
            ptr = ptr.next
            
        return head.next
                