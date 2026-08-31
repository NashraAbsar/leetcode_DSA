# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # We need at least 3 nodes to have any critical points
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        min_dist = float('inf')
        first_cp = -1
        prev_cp = -1
        
        prev = head
        curr = head.next
        curr_index = 1  # 0-indexed position tracker (head is 0, head.next is 1)
        
        while curr.next:
            nxt = curr.next
            
            # Check for local maxima or local minima
            is_maxima = curr.val > prev.val and curr.val > nxt.val
            is_minima = curr.val < prev.val and curr.val < nxt.val
            
            if is_maxima or is_minima:
                if first_cp == -1:
                    first_cp = curr_index
                else:
                    # Update minimum distance with the consecutive gap
                    min_dist = min(min_dist, curr_index - prev_cp)
                
                # Move the previous critical point tracker to current
                prev_cp = curr_index
                
            # Move pointers forward
            prev = curr
            curr = nxt
            curr_index += 1
            
        # If we found fewer than 2 critical points, return [-1, -1]
        if first_cp == prev_cp:
            return [-1, -1]
            
        max_dist = prev_cp - first_cp
        return [min_dist, max_dist]
