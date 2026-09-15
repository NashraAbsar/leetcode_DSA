# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        arrayy=[]
        current=head
        while current:
            arrayy.append(current.val)
            current=current.next
        return arrayy[::]==arrayy[::-1]
        