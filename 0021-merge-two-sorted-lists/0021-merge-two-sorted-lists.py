# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = list1
        ptr2 = list2
        prev = ListNode() # pointer for the merged linked list
        dummy = prev # dummy pointer to return the head of the merged linked list
        
        # traverse until one of the list reaches the end
        while ptr1 and ptr2:
            if ptr1.val < ptr2.val:
                prev.next = ptr1
                ptr1 = ptr1.next
                prev = prev.next
            else:
                prev.next = ptr2
                ptr2 = ptr2.next
                prev = prev.next
        # merge the remaining linked list
        if ptr1:
            prev.next = ptr1
        else:
            prev.next = ptr2
        return dummy.next