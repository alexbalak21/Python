# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        if not l1 or not l2:
            return None
        a1 = []
        current = l1
        while current is not None:
            a1.append(current.val)
            current = current.next
        return self.lsit_to_listNode(self, a1)
    
    @staticmethod
    def lsit_to_listNode(self, arr):
        if not arr:
            return None
        return ListNode(val=arr[0], next=self.lsit_to_listNode(self, arr[1:]))

    @staticmethod
    def ListNode_to_List(self, listNode):
        lst = []
        current = listNode
        while current is not None:
            lst.append(current.val)
            current = current.next
        return lst
