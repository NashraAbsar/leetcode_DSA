from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        total_counts = Counter(s)
        
        # Step 1: Find the longest prefix of 'target' that we can match
        # using the available characters from 's'
        matched_prefix_len = 0
        current_counts = total_counts.copy()
        
        for char in target:
            if current_counts[char] > 0:
                current_counts[char] -= 1
                matched_prefix_len += 1
            else:
                break
                
        # Step 2: Try to find a valid pivot index from right to left
        # We start by assuming we matched up to matched_prefix_len
        for i in range(matched_prefix_len, -1, -1):
            # Recalculate remaining characters up to position i
            counts = total_counts.copy()
            for j in range(i):
                counts[target[j]] -= 1
                
            # If we are not at the end, we MUST pick a character strictly larger than target[i]
            if i < n:
                found = False
                # Try all lowercase letters strictly greater than target[i]
                for c_ord in range(ord(target[i]) + 1, ord('z') + 1):
                    char_to_pick = chr(c_ord)
                    if counts[char_to_pick] > 0:
                        # Construct the prefix up to i
                        prefix = target[:i] + char_to_pick
                        counts[char_to_pick] -= 1
                        
                        # The remaining characters should be arranged in ascending order
                        suffix = []
                        for c_ord_rem in range(ord('a'), ord('z') + 1):
                            rem_char = chr(c_ord_rem)
                            if counts[rem_char] > 0:
                                suffix.append(rem_char * counts[rem_char])
                                
                        return prefix + "".join(suffix)
            else:
                # If i == n, it means we perfectly matched the target string. 
                # But we need a string *strictly greater* than target, so matching it perfectly 
                # doesn't help us unless we can pivot at a previous index.
                continue
                
        return ""
