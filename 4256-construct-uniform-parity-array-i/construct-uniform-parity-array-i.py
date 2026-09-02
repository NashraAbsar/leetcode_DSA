class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # Count how many odd numbers are in the array
        odd_count = sum(1 for x in nums1 if x % 2 != 0)
        n = len(nums1)
        
        # If there is only 1 element, it's already uniform parity
        if n == 1:
            return True
            
        # Case 1: Can we make all elements EVEN?
        # Possible if no odd numbers exist, or if we have at least 2 odd numbers
        # so they can subtract from each other (odd - odd = even)
        can_be_all_even = (odd_count != 1)
        
        # Case 2: Can we make all elements ODD?
        # Possible if there is at least one odd number to subtract from evens
        # (even - odd = odd)
        can_be_all_odd = (odd_count > 0)
        
        return can_be_all_even or can_be_all_odd
